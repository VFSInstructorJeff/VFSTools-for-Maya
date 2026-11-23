"""Read-only questions about the Maya scene: which groups exist, which prefixes they hold, what an apply would touch."""

import maya.cmds as cmds

from characters.xgen_template.constants import GEO_PATTERN, SELECT_GROUP_LABEL


def leaf_name(node):
    return node.rsplit("|", 1)[-1]


def scene_group_names():
    """Names of the top-level groups: top-level plain transforms that hold no shapes of their own.

    Meshes, cameras, joints and the like are skipped. Every group is listed (not just the expected
    GENERATION_BASES / GUIDE_CURVES) so a mistyped group name can still be picked.
    """
    groups = []
    # Assemblies are the only DAG nodes that can qualify as top-level groups.
    # Avoid querying children and parents for every transform in a large scene.
    for node in cmds.ls(assemblies=True, long=True) or []:
        if cmds.objectType(node) != "transform":
            continue
        if cmds.listRelatives(node, children=True, shapes=True):
            continue
        groups.append(leaf_name(node))
    return sorted(groups, key=str.lower)


def scene_materials():
    return sorted(set(cmds.ls(materials=True) or []), key=str.lower)


def resolve_scene_group(value, field_name):
    matches = cmds.ls((value or "").strip(), long=True, type="transform") or []
    if len(matches) != 1:
        raise ValueError(
            "The {} group must resolve to exactly one Outliner transform.".format(
                field_name
            )
        )
    return matches[0]


def prefix_index(value, field_name):
    prefix = (value or "").strip().upper()
    if prefix.endswith("_"):
        prefix = prefix[:-1]
    if len(prefix) != 1 or prefix < "A" or prefix > "Z":
        raise ValueError(
            "{} must be one letter, optionally followed by an underscore.".format(
                field_name
            )
        )
    return ord(prefix) - ord("A")


def prefixes_for_generation_group(generation_group):
    if (
        not generation_group
        or generation_group == SELECT_GROUP_LABEL
        or not cmds.objExists(generation_group)
    ):
        return []

    try:
        generation_root = resolve_scene_group(generation_group, "Generation Bases")
    except ValueError:
        return []
    prefixes = set()
    mesh_shapes = (
        cmds.ls(
            generation_root,
            dag=True,
            type="mesh",
            noIntermediate=True,
            long=True,
        )
        or []
    )
    for shape in mesh_shapes:
        node = shape.rsplit("|", 1)[0]
        match = GEO_PATTERN.match(leaf_name(node))
        if not match:
            continue
        prefixes.add(match.group(1).upper() + "_")
    return sorted(prefixes)


def _generation_nodes_in_range(generation_root, start_index, end_index):
    """(node, base_name, letter) for each *_GEO mesh under the group whose prefix letter is in range."""
    generation_shapes = (
        cmds.ls(
            generation_root,
            dag=True,
            type="mesh",
            noIntermediate=True,
            long=True,
        )
        or []
    )
    generation_nodes = {shape.rsplit("|", 1)[0] for shape in generation_shapes}
    matching_generation_nodes = []
    for node in sorted(generation_nodes):
        base_name = leaf_name(node)
        match = GEO_PATTERN.match(base_name)
        if not match:
            continue
        letter = match.group(1).upper()
        letter_index = ord(letter) - ord("A")
        if start_index <= letter_index <= end_index:
            matching_generation_nodes.append((node, base_name, letter))

    if not matching_generation_nodes:
        raise ValueError(
            "No *_GEO meshes in '{}' matched the selected prefix range.".format(
                generation_root
            )
        )
    return matching_generation_nodes


def _guide_groups_by_name(guide_root):
    """{group name: [full paths]} for every *_CURVES group at or below the guide root."""
    guide_nodes = [guide_root] + (
        cmds.listRelatives(
            guide_root,
            allDescendents=True,
            type="transform",
            fullPath=True,
        )
        or []
    )

    guide_groups = {}
    for node in guide_nodes:
        name = leaf_name(node)
        if name.endswith("_CURVES"):
            guide_groups.setdefault(name, []).append(node)
    return guide_groups


def _curves_by_guide_group(matching_guide_paths):
    """{guide group path: sorted curve transforms} for the given *_CURVES groups."""
    guide_group_paths = set(matching_guide_paths)
    curves_by_guide_group = {}
    guide_shapes = (
        cmds.ls(
            matching_guide_paths,
            dag=True,
            type="nurbsCurve",
            noIntermediate=True,
            long=True,
        )
        or []
        if matching_guide_paths
        else []
    )
    for shape in guide_shapes:
        curve_transform = shape.rsplit("|", 1)[0]
        node = curve_transform
        while node:
            if node in guide_group_paths:
                curves_by_guide_group.setdefault(node, set()).add(curve_transform)
                break
            if "|" not in node:
                break
            node = node.rsplit("|", 1)[0]
    return {
        group_path: sorted(curve_transforms)
        for group_path, curve_transforms in curves_by_guide_group.items()
    }


def collect_apply_targets(
    generation_group,
    guide_group,
    from_prefix,
    to_prefix,
    includes_preset_guides,
):
    """Pair every *_GEO in the prefix range with its *_CURVES group; returns (generation_root, guide_root, targets)."""
    start_index = prefix_index(from_prefix, "From")
    end_index = prefix_index(to_prefix, "To")
    if start_index > end_index:
        raise ValueError("The From prefix must come before the To prefix.")

    generation_root = resolve_scene_group(generation_group, "Generation Bases")
    guide_root = resolve_scene_group(guide_group, "Guide Curves")
    matching_generation_nodes = _generation_nodes_in_range(
        generation_root, start_index, end_index
    )

    guide_groups = _guide_groups_by_name(guide_root)
    expected_guide_names = {
        base_name[:-4] + "_CURVES"
        for _node, base_name, _letter in matching_generation_nodes
    }
    matching_guide_paths = [
        group_path
        for group_name in expected_guide_names
        for group_path in guide_groups.get(group_name, [])
    ]
    curves_by_guide_group = _curves_by_guide_group(matching_guide_paths)

    targets = []
    for node, base_name, letter in matching_generation_nodes:
        expected_guide_group = base_name[:-4] + "_CURVES"
        matching_groups = guide_groups.get(expected_guide_group, [])
        if len(matching_groups) != 1:
            raise ValueError(
                "Expected one guide group named '{}' for '{}'.".format(
                    expected_guide_group, base_name
                )
            )

        curves = curves_by_guide_group.get(matching_groups[0], [])
        if not curves and not includes_preset_guides:
            raise ValueError(
                "No NURBS guide curves were found in '{}' and the template has no "
                "saved guides.".format(expected_guide_group)
            )

        targets.append(
            {
                "letter": letter,
                "base": node,
                "base_name": base_name,
                "description": base_name[:-4] + "_Description",
                "guide_group": matching_groups[0],
                "curves": curves,
            }
        )

    description_names = [target["description"] for target in targets]
    if len(description_names) != len(set(description_names)):
        raise ValueError(
            "The selected generation bases produce duplicate descriptions."
        )

    return generation_root, guide_root, targets
