"""Batch ngSkinTools layer transfer for the VFS Rigging tools.

The tool writes native ngSkinTools JSON files, one per skinned mesh, named
after its Outliner transform (for example, ``Body_low_weights.json``). It can
also match files such as ``Megaman_BodyWeights.json`` to ``Body_low``. Open it
in Maya with:

    from rigging import batch_import_export_weights
    batch_import_export_weights.show()

Import uses ngSkinTools2 to preserve the layer stack and map influences. It
initializes destination layers as needed and clears existing destination layers
before transfer, keeping the Maya "Keep existing layers" option off.
"""

import json
import os
import re

import maya.cmds as cmds
import maya.api.OpenMaya as om


WINDOW = "VFSBatchWeightsWorkspaceControl"
LEGACY_WINDOW = "VFSBatchWeightsWindow"
WINDOW_TITLE = "Import/Export Weights"
FOLDER_FIELD = "VFSBatchWeightsFolder"
MAPPING_MENU = "VFSBatchWeightsMapping"
IMPORT_BUTTON = "VFSBatchWeightsImportButton"
EXPORT_BUTTON = "VFSBatchWeightsExportButton"
FOLDER_OPTION_VAR = "VFSBatchWeightsFolder"
MAPPING_MODES = (
    "By Vertex ID",
    "Closest Point On Surface",
    "By UVs Space",
)
WINDOW_WIDTH = 175
WINDOW_CONTENT_WIDTH = WINDOW_WIDTH - 10
WINDOW_HEIGHT = 160
FIELD_HEIGHT = 20
BUTTON_HEIGHT = 25
FOOTER_ROW_HEIGHT = 19
FOOTER_TEXT_HEIGHT = 16
FOOTER_SIDE_PADDING = 2
FOOTER_BODY_BACKGROUND = (0.30, 0.30, 0.30)
FILE_SUFFIX = "_weights.json"
FORMAT_VERSION = 1


def _short_name(node):
    """Return the Outliner leaf name without its Maya namespace."""
    leaf = node.rsplit("|", 1)[-1]
    return leaf.rsplit(":", 1)[-1]


def _safe_filename(name):
    # Namespaces and DAG paths are represented in the JSON metadata, not files.
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", _short_name(name))


def _mesh_transform(shape):
    parents = cmds.listRelatives(shape, parent=True, fullPath=True) or []
    return parents[0] if parents else shape


def _scene_skinned_meshes():
    """Return (transform, shape, skinCluster) entries for meshes in the scene."""
    found = {}
    for cluster in cmds.ls(type="skinCluster") or []:
        geometries = cmds.skinCluster(cluster, query=True, geometry=True) or []
        for geometry in geometries:
            if not cmds.objExists(geometry):
                continue
            shapes = cmds.listRelatives(geometry, shapes=True, noIntermediate=True,
                                        fullPath=True, type="mesh") or []
            if cmds.nodeType(geometry) == "mesh":
                shapes = [geometry]
            for shape in shapes:
                key = shape
                if key not in found:
                    found[key] = (_mesh_transform(shape), shape, cluster)
    return list(found.values())


def _mesh_data(shape):
    """Read object-space points, one UV per vertex, and Maya's mesh triangles."""
    selection = om.MSelectionList()
    selection.add(shape)
    dag_path = selection.getDagPath(0)
    mesh_fn = om.MFnMesh(dag_path)
    points = mesh_fn.getPoints(om.MSpace.kObject)
    positions = [[float(p.x), float(p.y), float(p.z)] for p in points]

    uv_set_names = mesh_fn.getUVSetNames()
    uv_set = mesh_fn.currentUVSetName() if uv_set_names else None
    uvs = []
    if uv_set:
        for point in points:
            try:
                uv = mesh_fn.getUVAtPoint(point, om.MSpace.kObject, uv_set)
                uvs.append([float(uv[0]), float(uv[1])])
            except Exception:
                uvs.append(None)
    else:
        uvs = [None] * len(points)

    _, triangle_vertices = mesh_fn.getTriangles()
    triangles = [list(map(int, triangle_vertices[i:i + 3]))
                 for i in range(0, len(triangle_vertices), 3)]
    return positions, uvs, triangles, uv_set


def _skin_weights(cluster, shape, vertex_count):
    influences = cmds.skinCluster(cluster, query=True, influence=True) or []
    records = []
    for influence in influences:
        records.append({"name": influence, "short_name": _short_name(influence)})

    weights = []
    for index in range(vertex_count):
        values = cmds.skinPercent(cluster, "{}.vtx[{}]".format(shape, index),
                                 query=True, value=True) or []
        # Maya returns weights in the skinCluster influence order.
        weights.append([float(value) for value in values[:len(influences)]])
    return records, weights


def _weight_path(directory, transform):
    return os.path.join(directory, _safe_filename(transform) + FILE_SUFFIX)


def _weight_name_tokens(name):
    """Normalize mesh and file names for matching (Body_low ↔ Megaman_BodyWeights)."""
    stem = os.path.splitext(os.path.basename(name))[0]
    stem = re.sub(r"(?i)[_-]?weights?$", "", stem)
    tokens = set(re.findall(r"[a-z0-9]+", stem.lower()))
    return tokens - {"low", "high", "geo", "georn", "mesh", "shape", "skin"}


def _match_weight_files(meshes, directory):
    """Match exact VFS names first, then unique semantic name tokens."""
    files = sorted(os.path.join(directory, name) for name in os.listdir(directory)
                   if name.lower().endswith(".json"))
    unused = set(files)
    matches, issues = {}, []

    for transform, shape, cluster in meshes:
        exact = _weight_path(directory, transform)
        if exact in unused:
            matches[shape] = (transform, shape, cluster, exact)
            unused.remove(exact)

    for transform, shape, cluster in meshes:
        if shape in matches:
            continue
        target_tokens = _weight_name_tokens(transform)
        scored = [(len(target_tokens & _weight_name_tokens(path)), path)
                  for path in unused]
        best_score = max((score for score, _ in scored), default=0)
        best = [path for score, path in scored if score == best_score and score > 0]
        if best_score == 0:
            continue
        if len(best) != 1:
            issues.append("{}: multiple weight files match its name; skipped.".format(transform))
            continue
        path = best[0]
        matches[shape] = (transform, shape, cluster, path)
        unused.remove(path)
    return matches, issues


def export_all(directory):
    """Export every skinned mesh's ngSkinTools layers to the chosen folder.

    Returns ``(successful_paths, errors)``.
    """
    if not directory:
        raise ValueError("Choose a destination folder first.")
    directory = os.path.abspath(os.path.expanduser(directory))
    os.makedirs(directory, exist_ok=True)
    meshes = _scene_skinned_meshes()
    if not meshes:
        cmds.warning("No skinned meshes were found in the scene.")
        return [], []

    # Avoid silently overwriting files when distinct DAG nodes share a leaf name.
    names = {}
    for transform, _, _ in meshes:
        names.setdefault(_safe_filename(transform), []).append(transform)
    collisions = {name: nodes for name, nodes in names.items() if len(nodes) > 1}

    successful, errors = [], []
    for transform, shape, cluster in meshes:
        file_key = _safe_filename(transform)
        if file_key in collisions:
            errors.append("{}: duplicate Outliner leaf name; skipped to avoid overwrite.".format(transform))
            continue
        try:
            from ngSkinTools2 import api as ngst_api

            path = _weight_path(directory, transform)
            # Initialization is idempotent; create a base layer from the
            # existing skinCluster weights when there is no layer stack yet.
            layers = ngst_api.init_layers(cluster)
            if not layers.list():
                layers.add("Base Weights")
            ngst_api.export_json(cluster, file=path)
            successful.append(path)
        except Exception as exc:
            errors.append("{}: {}".format(transform, exc))
    return successful, errors


def _closest_point_triangle(point, a, b, c):
    """Return the closest point's barycentric coordinates on triangle abc."""
    # Ericson, Real-Time Collision Detection, closest-point-on-triangle regions.
    ab = [b[i] - a[i] for i in range(3)]
    ac = [c[i] - a[i] for i in range(3)]
    ap = [point[i] - a[i] for i in range(3)]
    dot = lambda x, y: sum(x[i] * y[i] for i in range(3))
    d1, d2 = dot(ab, ap), dot(ac, ap)
    if d1 <= 0.0 and d2 <= 0.0:
        return 0.0, 0.0, 0.0
    bp = [point[i] - b[i] for i in range(3)]
    d3, d4 = dot(ab, bp), dot(ac, bp)
    if d3 >= 0.0 and d4 <= d3:
        return 0.0, 1.0, 0.0
    vc = d1 * d4 - d3 * d2
    if vc <= 0.0 and d1 >= 0.0 and d3 <= 0.0:
        v = d1 / (d1 - d3)
        return 1.0 - v, v, 0.0
    cp = [point[i] - c[i] for i in range(3)]
    d5, d6 = dot(ab, cp), dot(ac, cp)
    if d6 >= 0.0 and d5 <= d6:
        return 0.0, 0.0, 1.0
    vb = d5 * d2 - d1 * d6
    if vb <= 0.0 and d2 >= 0.0 and d6 <= 0.0:
        w = d2 / (d2 - d6)
        return 1.0 - w, 0.0, w
    va = d3 * d6 - d5 * d4
    if va <= 0.0 and (d4 - d3) >= 0.0 and (d5 - d6) >= 0.0:
        w = (d4 - d3) / ((d4 - d3) + (d5 - d6))
        return 0.0, 1.0 - w, w
    denom = va + vb + vc
    if abs(denom) < 1e-20:
        return 1.0, 0.0, 0.0
    v, w = vb / denom, vc / denom
    return 1.0 - v - w, v, w


def _map_vertex_id(source, destination_count):
    if source["vertex_count"] != destination_count:
        raise ValueError("Vertex ID mapping requires matching vertex counts ({} vs {}).".format(
            source["vertex_count"], destination_count))
    return source["weights"]


def _build_triangle_tree(points, triangles):
    """Build a small AABB tree so surface remapping scales to production meshes."""
    entries = []
    for triangle in triangles:
        try:
            vertices = [points[index] for index in triangle]
        except IndexError:
            continue
        lower = [min(point[axis] for point in vertices) for axis in range(3)]
        upper = [max(point[axis] for point in vertices) for axis in range(3)]
        center = [(lower[axis] + upper[axis]) * 0.5 for axis in range(3)]
        entries.append((triangle, lower, upper, center))

    def build(items):
        lower = [min(item[1][axis] for item in items) for axis in range(3)]
        upper = [max(item[2][axis] for item in items) for axis in range(3)]
        if len(items) <= 8:
            return (lower, upper, items, None, None)
        axis = max(range(3), key=lambda i: upper[i] - lower[i])
        items.sort(key=lambda item: item[3][axis])
        middle = len(items) // 2
        return (lower, upper, None, build(items[:middle]), build(items[middle:]))

    return build(entries) if entries else None


def _box_distance_squared(point, lower, upper):
    total = 0.0
    for axis in range(3):
        if point[axis] < lower[axis]:
            delta = lower[axis] - point[axis]
        elif point[axis] > upper[axis]:
            delta = point[axis] - upper[axis]
        else:
            delta = 0.0
        total += delta * delta
    return total


def _closest_tree_match(point, tree, source_points, source_weights):
    best_distance = float("inf")
    best_weights = None

    def visit(node):
        nonlocal best_distance, best_weights
        lower, upper, items, left, right = node
        if _box_distance_squared(point, lower, upper) >= best_distance:
            return
        if items is not None:
            for triangle, _, _, _ in items:
                bary = _closest_point_triangle(
                    point, *(source_points[index] for index in triangle))
                closest = [sum(bary[j] * source_points[triangle[j]][axis]
                               for j in range(3)) for axis in range(3)]
                distance = sum((point[axis] - closest[axis]) ** 2
                                for axis in range(3))
                if distance < best_distance:
                    best_distance = distance
                    best_weights = [
                        sum(bary[j] * source_weights[triangle[j]][index]
                            for j in range(3))
                        for index in range(len(source_weights[0]))
                    ]
            return
        children = [child for child in (left, right) if child is not None]
        children.sort(key=lambda child: _box_distance_squared(point, child[0], child[1]))
        for child in children:
            visit(child)

    visit(tree)
    return best_weights


def _map_nearest_surface(source, destination_positions, use_uv=False,
                         destination_uvs=None):
    source_points = source["uvs"] if use_uv else source["positions"]
    dest_points = destination_uvs if use_uv else destination_positions
    if not source_points or any(point is None for point in source_points):
        raise ValueError("UV space mapping requires UV coordinates on both meshes.")
    if not dest_points or any(point is None for point in dest_points):
        raise ValueError("UV space mapping requires UV coordinates on both meshes.")

    # Work in 3D for the triangle helper; UV coordinates occupy the XY plane.
    source_points = [list(point[:2]) + [0.0] if use_uv else list(point)
                     for point in source_points]
    dest_points = [list(point[:2]) + [0.0] if use_uv else list(point)
                   for point in dest_points]
    triangles = source.get("triangles") or []
    if not triangles:
        raise ValueError("The source weight file contains no mesh triangles.")
    tree = _build_triangle_tree(source_points, triangles)
    if tree is None:
        raise ValueError("The source weight file contains no valid mesh triangles.")

    mapped = []
    for point in dest_points:
        best_weights = _closest_tree_match(point, tree, source_points,
                                           source["weights"])
        if best_weights is None:
            raise ValueError("Could not map a destination vertex to the source surface.")
        mapped.append(best_weights)
    return mapped


def _influence_index_map(source_influences, destination_influences):
    dest_exact = {name: index for index, name in enumerate(destination_influences)}
    dest_short = {}
    for index, name in enumerate(destination_influences):
        dest_short.setdefault(_short_name(name), []).append(index)

    mapping = []
    for source in source_influences:
        name = source.get("name", "")
        short_name = source.get("short_name") or _short_name(name)
        if name in dest_exact:
            mapping.append(dest_exact[name])
        elif len(dest_short.get(short_name, [])) == 1:
            mapping.append(dest_short[short_name][0])
        else:
            mapping.append(None)
    return mapping


def _apply_weights(cluster, shape, source, rows):
    destination_influences = cmds.skinCluster(cluster, query=True, influence=True) or []
    influence_map = _influence_index_map(source["influences"], destination_influences)
    if not any(index is not None for index in influence_map):
        raise ValueError("No source influences match this skinCluster.")

    applied = 0
    for vertex_id, source_row in enumerate(rows):
        combined = [0.0] * len(destination_influences)
        for source_index, value in enumerate(source_row):
            if source_index >= len(influence_map):
                break
            destination_index = influence_map[source_index]
            if destination_index is not None:
                combined[destination_index] += float(value)
        total = sum(combined)
        if total <= 1e-12:
            continue
        assignments = [(destination_influences[i], weight / total)
                       for i, weight in enumerate(combined) if weight > 1e-12]
        cmds.skinPercent(cluster, "{}.vtx[{}]".format(shape, vertex_id),
                         transformValue=assignments, normalize=True,
                         zeroRemainingInfluences=True)
        applied += 1
    return applied


def import_all(directory, mapping_mode=MAPPING_MODES[0]):
    """Import matching ngSkinTools or VFS JSON files for all skinned meshes.

    ngSkinTools files are transferred with their layer stack and influence map.
    Destination layers are cleared before transfer, matching the unchecked
    "Keep existing layers on destination" setting. Its transfer API initializes
    layers first when the destination skinCluster has no layer data.
    """
    if not directory or not os.path.isdir(os.path.expanduser(directory)):
        raise ValueError("Choose an existing weights folder first.")
    directory = os.path.abspath(os.path.expanduser(directory))
    if mapping_mode not in MAPPING_MODES:
        raise ValueError("Unknown mapping mode: {}".format(mapping_mode))

    meshes = _scene_skinned_meshes()
    if not meshes:
        cmds.warning("No skinned meshes were found in the scene.")
        return [], []

    matches, issues = _match_weight_files(meshes, directory)

    successful, errors = [], []
    errors.extend(issues)
    for transform, shape, cluster in meshes:
        match = matches.get(shape)
        if not match:
            continue
        path = match[3]
        try:
            with open(path, "r", encoding="utf-8") as weight_file:
                source = json.load(weight_file)
            if source.get("format") == "VFS skin weights":
                if source.get("format_version") != FORMAT_VERSION:
                    raise ValueError("Unsupported VFS weight file version: {}".format(
                        source.get("format_version")))
                destination_positions, destination_uvs, _, _ = _mesh_data(shape)
                if mapping_mode == MAPPING_MODES[2]:
                    rows = _map_vertex_id(source, len(destination_positions))
                elif mapping_mode == MAPPING_MODES[1]:
                    rows = _map_nearest_surface(source, destination_positions,
                                                use_uv=True, destination_uvs=destination_uvs)
                else:
                    rows = _map_nearest_surface(source, destination_positions)
                count = _apply_weights(cluster, shape, source, rows)
                successful.append("{} ({} vertices)".format(transform, count))
            else:
                from ngSkinTools2.api import InfluenceMappingConfig, VertexTransferMode
                from ngSkinTools2.api.import_export import FileFormat
                from ngSkinTools2.api.transfer import LayersTransfer

                modes = {
                    MAPPING_MODES[0]: VertexTransferMode.vertexId,
                    MAPPING_MODES[1]: VertexTransferMode.closestPoint,
                    MAPPING_MODES[2]: VertexTransferMode.uvSpace,
                }
                mode = modes.get(mapping_mode, VertexTransferMode.vertexId)
                if "vertex" in str(mapping_mode).lower():
                    mode = VertexTransferMode.vertexId
                elif "uv" in str(mapping_mode).lower():
                    mode = VertexTransferMode.uvSpace
                elif "closest" in str(mapping_mode).lower() or "point" in str(mapping_mode).lower() or "surface" in str(mapping_mode).lower():
                    mode = VertexTransferMode.closestPoint
                importer = LayersTransfer()
                importer.vertex_transfer_mode = mode
                importer.influences_mapping.config = InfluenceMappingConfig.transfer_defaults()
                importer.load_source_from_file(path, format=FileFormat.JSON)
                importer.target = cluster
                importer.keep_existing_layers = False
                importer.execute()
                successful.append("{} ← {}".format(transform, os.path.basename(path)))
        except Exception as exc:
            errors.append("{}: {}".format(transform, exc))
    if not successful and not errors:
        errors.append("No matching JSON weight files were found for skinned meshes in this folder.")
    return successful, errors


def _saved_folder():
    if cmds.optionVar(exists=FOLDER_OPTION_VAR):
        return (cmds.optionVar(query=FOLDER_OPTION_VAR) or "").strip()
    return ""


def _format_display_folder(path):
    path = (path or "").strip().rstrip("/\\")
    if not path:
        return ""
    leaf = os.path.basename(path)
    return f"../{leaf}" if leaf else path


def _folder_browse(*_):
    current = _saved_folder()
    result = cmds.fileDialog2(
        fileMode=3,
        caption="Choose weights folder",
        startingDirectory=current or os.path.expanduser("~"),
    )
    if result:
        full_path = result[0]
        _save_folder(full_path)
        cmds.textField(
            FOLDER_FIELD,
            edit=True,
            text=_format_display_folder(full_path),
            annotation=full_path,
        )


def _save_folder(folder):
    """Persist the selected path in Maya preferences for future sessions."""
    folder = (folder or "").strip()
    if folder and not folder.startswith("../"):
        cmds.optionVar(stringValue=(FOLDER_OPTION_VAR, folder))


def _folder_value():
    text = (cmds.textField(FOLDER_FIELD, query=True, text=True) or "").strip()
    saved = _saved_folder()
    if text.startswith("../"):
        return saved
    if text:
        _save_folder(text)
        cmds.textField(
            FOLDER_FIELD,
            edit=True,
            text=_format_display_folder(text),
            annotation=text,
        )
        return text
    return saved


def _selected_mapping():
    selected = cmds.optionMenu(MAPPING_MENU, query=True, value=True)
    return selected


def _show_result(title, successful, errors):
    lines = ["Completed: {}".format(len(successful))]
    lines.extend(successful[:12])
    if len(successful) > 12:
        lines.append("... and {} more".format(len(successful) - 12))
    if errors:
        lines.extend(["", "Issues: {}".format(len(errors))])
        lines.extend(errors[:12])
        if len(errors) > 12:
            lines.append("... and {} more".format(len(errors) - 12))
    cmds.confirmDialog(title=title, message="\n".join(lines), button=["OK"],
                       defaultButton="OK")


def _run_export(*_):
    directory = _folder_value()
    _save_folder(directory)
    try:
        paths, errors = export_all(directory)
        _show_result("Export Weights", paths, errors)
    except Exception as exc:
        cmds.confirmDialog(title="Export Weights", message=str(exc), button=["OK"])


def _run_import(*_):
    directory = _folder_value()
    _save_folder(directory)
    try:
        imported, errors = import_all(directory, _selected_mapping())
        _show_result("Import Weights", imported, errors)
    except Exception as exc:
        cmds.confirmDialog(title="Import Weights", message=str(exc), button=["OK"])


def _set_footer_text_color():
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    for control_name in ("batchWeightsFooterAuthor", "batchWeightsFooterVersion"):
        pointer = omui.MQtUtil.findControl(control_name)
        if pointer:
            label = wrap_instance(int(pointer), QtWidgets.QWidget)
            label.setStyleSheet("color: rgb(153, 153, 153);")


_DROPDOWN_HOVER_FILTERS = []


def _install_dropdown_hover_effects():
    """Lighten dropdown backgrounds slightly while hovered (matching X-Gen Template Tool)."""
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    class DropdownHoverFilter(QtCore.QObject):
        def __init__(self, widget, parent=None):
            super(DropdownHoverFilter, self).__init__(parent)
            self.widget = widget
            self.normal_style = ""

        def eventFilter(self, watched, event):
            if event.type() == QtCore.QEvent.Enter:
                self.normal_style = self.widget.styleSheet()
                self.widget.setStyleSheet(
                    self.normal_style
                    + " QComboBox { background-color: rgb(54, 54, 54); }"
                )
                self.widget.update()
            elif event.type() == QtCore.QEvent.Leave:
                self.widget.setStyleSheet(self.normal_style)
                self.widget.update()
            return False

    _DROPDOWN_HOVER_FILTERS[:] = []
    pointer = omui.MQtUtil.findControl(MAPPING_MENU)
    if pointer:
        widget = wrap_instance(int(pointer), QtWidgets.QComboBox)
        hover_filter = DropdownHoverFilter(widget, widget)
        widget.setMouseTracking(True)
        widget.installEventFilter(hover_filter)
        _DROPDOWN_HOVER_FILTERS.append(hover_filter)


_HELP_HOVER_FILTERS = []


def _install_help_hover_effect():
    """Switch help icon to help_line.png on hover (matching X-Gen Template Tool)."""
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    class HelpIconHoverFilter(QtCore.QObject):
        def __init__(self, widget, control_name, parent=None):
            super(HelpIconHoverFilter, self).__init__(parent or widget)
            self.widget = widget
            self.control_name = control_name

        def eventFilter(self, watched, event):
            if event.type() == QtCore.QEvent.Enter:
                if cmds.iconTextButton(self.control_name, exists=True):
                    cmds.iconTextButton(self.control_name, edit=True, image="help_line.png")
            elif event.type() == QtCore.QEvent.Leave:
                if cmds.iconTextButton(self.control_name, exists=True):
                    cmds.iconTextButton(self.control_name, edit=True, image="help.png")
            return False

    _HELP_HOVER_FILTERS[:] = []
    pointer = omui.MQtUtil.findControl("batchWeightsFooterHelp")
    if pointer:
        widget = wrap_instance(int(pointer), QtWidgets.QWidget)
        hover_filter = HelpIconHoverFilter(widget, "batchWeightsFooterHelp", parent=widget)
        widget.installEventFilter(hover_filter)
        _HELP_HOVER_FILTERS.append(hover_filter)


_ACTION_BUTTON_FILTERS = []


class ActionButtonPressEffect:
    """Apply explicit colors during mouse and keyboard press/release."""

    def __new__(cls, *args, **kwargs):
        try:
            from PySide6 import QtCore
        except ImportError:
            from PySide2 import QtCore

        normal_style = "QPushButton { color: %s; font-weight: %s; }" % (
            args[4], args[5]
        )

        class _Filter(QtCore.QObject):
            def __init__(self, widget, pressed_color, hover_color, pressed_text, text_color, weight, normal_style):
                super(_Filter, self).__init__(widget)
                self.widget = widget
                self.normal_style = normal_style
                self.hover_style = self._color_style(hover_color, text_color, weight)
                self.pressed_style = (
                    "QPushButton {{ background-color: rgb({}, {}, {}); "
                    "border: 1px solid rgb({}, {}, {}); "
                    "color: {}; font-weight: {}; }}".format(
                        pressed_color[0],
                        pressed_color[1],
                        pressed_color[2],
                        max(0, pressed_color[0] - 18),
                        max(0, pressed_color[1] - 18),
                        max(0, pressed_color[2] - 18),
                        pressed_text,
                        weight,
                    )
                )

            def _color_style(self, color, text, weight):
                return (
                    "QPushButton {{ background-color: rgb({}, {}, {}); "
                    "border: 1px solid rgb({}, {}, {}); color: {}; "
                    "font-weight: {}; }}".format(
                        color[0], color[1], color[2],
                        max(0, color[0] - 18),
                        max(0, color[1] - 18),
                        max(0, color[2] - 18),
                        text, weight,
                    )
                )

            def eventFilter(self, watched, event):
                event_type = event.type()
                if event_type in (QtCore.QEvent.MouseButtonPress, QtCore.QEvent.KeyPress):
                    self.widget.setStyleSheet(self.pressed_style)
                    self.widget.update()
                elif event_type in (QtCore.QEvent.Enter,):
                    self.widget.setStyleSheet(self.hover_style)
                    self.widget.update()
                elif event_type == QtCore.QEvent.Leave:
                    self.widget.setStyleSheet(self.normal_style)
                    self.widget.update()
                elif event_type in (QtCore.QEvent.MouseButtonRelease, QtCore.QEvent.KeyRelease):
                    self.widget.setStyleSheet(
                        self.hover_style if self.widget.underMouse() else self.normal_style
                    )
                    self.widget.update()
                return False

        return _Filter(*args, normal_style=normal_style, **kwargs)


def _style_action_button(
    control_name,
    pressed_color,
    hover_color,
    text_color="rgb(0, 0, 0)",
    pressed_text_color="white",
    font_weight="bold",
):
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    pointer = omui.MQtUtil.findControl(control_name)
    if not pointer:
        return
    button = wrap_instance(int(pointer), QtWidgets.QWidget)
    normal_style = "QPushButton { color: %s; font-weight: %s; }" % (
        text_color,
        font_weight,
    )
    button.setStyleSheet(normal_style)
    effect = ActionButtonPressEffect(
        button,
        pressed_color,
        hover_color,
        pressed_text_color,
        text_color,
        font_weight,
    )
    button.installEventFilter(effect)
    _ACTION_BUTTON_FILTERS.append(effect)


def _set_workspace_control_fixed_width():
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
        is_valid = shiboken6.isValid
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance
        is_valid = shiboken2.isValid

    pointer = omui.MQtUtil.findControl(WINDOW)
    if not pointer:
        return
    control = wrap_instance(int(pointer), QtWidgets.QWidget)

    def fit_floating_window():
        if not is_valid(control):
            return
        if not cmds.workspaceControl(WINDOW, query=True, exists=True):
            return
        if not cmds.workspaceControl(WINDOW, query=True, floating=True):
            return

        control.adjustSize()
        floating_window = control.window()
        floating_window.setFixedWidth(WINDOW_WIDTH)
        floating_window.adjustSize()

    def enforce_dock_width():
        if not is_valid(control):
            return
        control.setMinimumWidth(WINDOW_WIDTH)
        control.setMaximumWidth(WINDOW_WIDTH)
        control.setFixedWidth(WINDOW_WIDTH)

        parent = control.parentWidget()
        while parent:
            cname = parent.metaObject().className()
            if "Tab" in cname or "Stack" in cname:
                parent.setMinimumWidth(WINDOW_WIDTH)
                parent.setMaximumWidth(WINDOW_WIDTH)
                parent.setFixedWidth(WINDOW_WIDTH)
            elif "Splitter" in cname:
                try:
                    sizes = parent.sizes()
                    if sizes:
                        idx = -1
                        for i in range(parent.count()):
                            child = parent.widget(i)
                            if child and (child == control or child.isAncestorOf(control)):
                                idx = i
                                break
                        if idx >= 0:
                            diff = sizes[idx] - WINDOW_WIDTH
                            if diff != 0:
                                sizes[idx] = WINDOW_WIDTH
                                adj_idx = 0 if idx != 0 else (len(sizes) - 1 if len(sizes) > 1 else 0)
                                if adj_idx < len(sizes):
                                    sizes[adj_idx] += diff
                                parent.setSizes(sizes)
                except Exception:
                    pass
                break
            parent = parent.parentWidget()

    legacy_filter = control.findChild(QtCore.QObject, "batchWeightsFloatingSizeFilter")
    if legacy_filter is not None:
        legacy_filter.deleteLater()

    legacy_timer = control.findChild(QtCore.QTimer, "batchWeightsFloatingSizeTimer")
    if legacy_timer is not None:
        legacy_timer.stop()
        legacy_timer.deleteLater()

    timer_name = "batchWeightsFloatingSizeTimerV2"
    timer = control.findChild(QtCore.QTimer, timer_name)
    if timer is None:
        floating_state = {
            "value": cmds.workspaceControl(WINDOW, query=True, floating=True)
        }
        timer = QtCore.QTimer(control)
        timer.setObjectName(timer_name)
        timer.setInterval(200)

        def watch_floating_state():
            if not is_valid(control):
                return
            if not cmds.workspaceControl(WINDOW, query=True, exists=True):
                timer.stop()
                return

            is_floating = cmds.workspaceControl(WINDOW, query=True, floating=True)
            if is_floating:
                fit_floating_window()
            else:
                enforce_dock_width()
            floating_state["value"] = is_floating

        timer.timeout.connect(watch_floating_state)
        timer.start()

    enforce_dock_width()
    control.updateGeometry()
    QtWidgets.QApplication.processEvents()
    fit_floating_window()


def show():
    """Create or restore the dockable Batch Import/Export Weights panel."""
    if cmds.window(LEGACY_WINDOW, exists=True):
        cmds.deleteUI(LEGACY_WINDOW, window=True)
    if cmds.workspaceControl(WINDOW, query=True, exists=True):
        cmds.workspaceControl(
            WINDOW,
            edit=True,
            label=WINDOW_TITLE,
            restore=True,
            initialWidth=WINDOW_WIDTH,
            minimumWidth=WINDOW_WIDTH,
            widthProperty="fixed",
        )
    else:
        ui_script = "from rigging import import_export_weights as tool; tool.build_ui()"
        cmds.workspaceControl(
            WINDOW,
            label=WINDOW_TITLE,
            floating=True,
            retain=False,
            initialWidth=WINDOW_WIDTH,
            minimumWidth=WINDOW_WIDTH,
            initialHeight=WINDOW_HEIGHT,
            widthProperty="fixed",
            uiScript=ui_script,
        )
    cmds.workspaceControl(WINDOW, edit=True, label=WINDOW_TITLE)
    cmds.workspaceControl(WINDOW, edit=True, restore=True)
    cmds.workspaceControl(WINDOW, edit=True, visible=True)
    _set_workspace_control_fixed_width()
    return WINDOW


def build_ui():
    """Build the panel contents; Maya calls this when restoring its workspace."""
    cmds.columnLayout(
        adjustableColumn=True,
        rowSpacing=0,
        columnAttach=("both", 4),
    )
    cmds.rowLayout(
        numberOfColumns=2,
        adjustableColumn=2,
        columnWidth2=(24, WINDOW_CONTENT_WIDTH - 24),
        columnAttach=[(1, "both", 0), (2, "both", 0)],
        height=FIELD_HEIGHT,
    )
    cmds.iconTextButton(
        style="iconOnly",
        image="folder-open.png",
        width=22,
        height=FIELD_HEIGHT,
        command=_folder_browse,
    )
    folder = _saved_folder()
    cmds.textField(
        FOLDER_FIELD,
        text=_format_display_folder(folder),
        annotation=folder,
        height=FIELD_HEIGHT,
        changeCommand=lambda *_: _folder_value(),
    )
    cmds.setParent("..")

    cmds.separator(height=3, style="none")
    cmds.optionMenu(
        MAPPING_MENU,
        height=FIELD_HEIGHT,
        backgroundColor=(0.16, 0.16, 0.16),
        changeCommand=lambda *_: None,
    )
    for mode in MAPPING_MODES:
        cmds.menuItem(label=mode)
    _install_dropdown_hover_effects()

    cmds.separator(height=3, style="none")
    cmds.button(
        IMPORT_BUTTON,
        label="IMPORT ALL",
        height=BUTTON_HEIGHT,
        backgroundColor=(0.50, 0.70, 0.50),
        command=_run_import,
    )
    _style_action_button(
        IMPORT_BUTTON,
        pressed_color=(46, 75, 48),
        hover_color=(99, 184, 102),
        pressed_text_color="white",
    )
    cmds.separator(height=3, style="none")
    cmds.button(
        EXPORT_BUTTON,
        label="EXPORT ALL",
        height=BUTTON_HEIGHT,
        backgroundColor=(0.56, 0.56, 0.78),
        command=_run_export,
    )
    _style_action_button(
        EXPORT_BUTTON,
        pressed_color=(51, 49, 77),
        hover_color=(105, 102, 199),
        pressed_text_color="white",
    )

    # Footer
    cmds.separator(height=2, style="none")
    cmds.rowLayout(
        numberOfColumns=5,
        adjustableColumn=3,
        columnWidth5=(
            FOOTER_SIDE_PADDING,
            18,
            max(20, WINDOW_CONTENT_WIDTH - 36 - 18 - FOOTER_SIDE_PADDING * 2),
            36,
            FOOTER_SIDE_PADDING,
        ),
        columnAttach5=("both", "both", "both", "both", "both"),
        height=FOOTER_ROW_HEIGHT,
        backgroundColor=FOOTER_BODY_BACKGROUND,
    )
    cmds.text(
        label="",
        width=FOOTER_SIDE_PADDING,
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=FOOTER_BODY_BACKGROUND,
    )
    cmds.iconTextButton(
        "batchWeightsFooterHelp",
        style="iconOnly",
        image="help.png",
        width=18,
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=FOOTER_BODY_BACKGROUND,
        annotation="Batch Import/Export Weights",
    )
    cmds.text(
        "batchWeightsFooterAuthor",
        label="InstructorJeff",
        align="left",
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=FOOTER_BODY_BACKGROUND,
    )
    cmds.text(
        "batchWeightsFooterVersion",
        label="V1.00",
        align="right",
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=FOOTER_BODY_BACKGROUND,
    )
    cmds.text(
        label="",
        width=FOOTER_SIDE_PADDING,
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=FOOTER_BODY_BACKGROUND,
    )
    cmds.setParent("..")

    _set_footer_text_color()
    _install_help_hover_effect()
    cmds.setParent("..")
    _set_workspace_control_fixed_width()
    return WINDOW
