"""UCX collision-mesh renaming helper.

Moved verbatim from the old userSetup.py. It is NOT currently wired up: the scriptJob that used it
("DagObjectCreated") was commented out as not entirely reliable. To re-enable it, add that scriptJob
to vfstools.general.setup._create_script_jobs().
"""
import maya.cmds as cmds


def UCX_name_fix():
    # Define prefix and suffix
    str_ucx = "UCX_"
    suffix_str = 'None'

    # Select object created
    selection_name = cmds.ls(sl=True)
    # Check selection isn't null (.e.g: creating a camera)
    if not selection_name:
        return
    else:
        # Select only the first index so we have an actual obj instead of a list with a single value in it
        selection_name = selection_name[0]

    # Get the obj's children
    children_ls = cmds.listRelatives(selection_name, children=True, type='transform', fullPath=True)
    # Check if children are null (e.g.: creating a regular polyCube)
    if (children_ls == None):
        return

    # Check if there's only a single child
    if (len(children_ls) == 1):
        # Get grandchild from child to check what type it is
        grandchild = cmds.listRelatives(children_ls, children=True, fullPath=True)
        grandchild_type = cmds.objectType(grandchild[0])
        # If it's not a mesh or a transform, ignore it (e.g.: creating a camera, grandchild will be 'camera' type)
        if ((grandchild_type != 'mesh') and (grandchild_type != 'transform')):
            print("Not a mesh. Ignoring UCX rename function.")
            return
        if str_ucx in str(children_ls[0]):
            # Rename the child so it matches its parent
            new_child_name = (str_ucx + selection_name)
            cmds.rename(str(children_ls[0]), new_child_name)
    else:
        for index, child in enumerate(children_ls):
            # Check if children have UCX_ prefix
            if str_ucx in child:
                # Check if children index is less than 10, if so append a 0 before the suffix
                if ((index + 1) < 10):
                    suffix_str = f"_0{index + 1}"
                else:
                    suffix_str = f"_{index + 1}"
                # Rename each child in children to prefix + parentName + suffix
                new_child_name = (str_ucx + selection_name + suffix_str)
                cmds.rename(str(child), new_child_name)
