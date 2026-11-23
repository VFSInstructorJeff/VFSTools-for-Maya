"""Provide a dockable Maya interface for saving and applying XGen templates.

The tool saves the selected XGen description's settings, palette data, and
modifier information as JSON under the project's ``xgen/templates`` folder.
It can apply a saved template across selected generation bases, matching guide
curves and prefix ranges, optionally convert curves to guides, and apply a display
material. Clean Start removes descriptions from the active collection so the user
can revise curves and rebuild. The module also provides the UI callbacks and menu
refresh helpers, validates apply targets, and uses shader-cleanup helpers to avoid
leaving unused hair-physical shader nodes behind.

The implementation lives in the ``characters.xgen_template`` package (see its
docstring for the module layout); this module is the stable entry point used by the
VFS_Characters shelf button and by Maya when it restores the docked panel.
"""

from characters.xgen_template.apply import apply_template, clean_start
from characters.xgen_template.menus import (
    refresh_from_prefix_menu,
    refresh_generation_group_menu,
    refresh_guide_group_menu,
    refresh_material_menu,
    refresh_save_template_menu,
    refresh_to_prefix_menu,
)
from characters.xgen_template.template_io import save_template
from characters.xgen_template.window import (
    build_ui as _build_ui,
)  # Maya's saved panel layout calls this name
from characters.xgen_template.window import show

__all__ = [
    "_build_ui",
    "apply_template",
    "clean_start",
    "refresh_from_prefix_menu",
    "refresh_generation_group_menu",
    "refresh_guide_group_menu",
    "refresh_material_menu",
    "refresh_save_template_menu",
    "refresh_to_prefix_menu",
    "save_template",
    "show",
]

if __name__ == "__main__":
    show()
