"""Implementation of the X-Gen Template Tool, split by job.

The public entry point is characters.xgen_template_tool (show, save_template, apply_template, clean_start).

constants    names, sizes, labels and option-variable keys
qt           PySide6 / PySide2 compatibility helpers
prefs        option-variable (saved preference) helpers
paths        project root and template file locations
dialogs      message boxes and confirmations
scene        read-only questions about the Maya scene (groups, prefixes, apply targets)
style        Qt styling: hover / press effects, fast tooltips, fixed panel width
menus        dropdown population and remembering the user's choices
template_io  saving and loading the template .json files
apply        applying a template, and Clean Start
window       the dockable panel and its button callbacks

Dependencies only point downwards in the list above (for example scene never imports menus).
"""
