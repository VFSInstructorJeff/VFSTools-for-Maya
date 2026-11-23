"""Names, sizes, labels and option-variable keys shared by the X-Gen Template Tool modules."""

import os
import re

WORKSPACE_CONTROL_NAME = "xGenToolsWorkspaceControl"
SCROLL_LAYOUT_NAME = "xGenToolsScrollLayout"
LEGACY_WINDOW_NAME = "xGenToolsWindow"
WINDOW_TITLE = "X-Gen Template Tool"

# Names of the individual controls in the panel (also used to find them from Qt)
MENU_TEMPLATE = "xGenToolsTemplatePath"
MENU_GENERATION_GROUP = "xGenToolsGenerationGroup"
MENU_GUIDE_GROUP = "xGenToolsGuideGroup"
MENU_FROM_PREFIX = "xGenToolsFromPrefix"
MENU_TO_PREFIX = "xGenToolsToPrefix"
MENU_MATERIAL = "xGenToolsApplyMaterial"
DROPDOWN_MENUS = (
    MENU_TEMPLATE,
    MENU_GENERATION_GROUP,
    MENU_GUIDE_GROUP,
    MENU_FROM_PREFIX,
    MENU_TO_PREFIX,
    MENU_MATERIAL,
)
STEP_1 = "xGenToolsStep1"
STEP_2 = "xGenToolsStep2"
STEP_3 = "xGenToolsStep3"
STEP_4 = "xGenToolsStep4"
STEP_5 = "xGenToolsStep5"
STEP_LABELS = (STEP_1, STEP_2, STEP_3, STEP_4, STEP_5)
BUTTON_SAVE_TEMPLATE = "xGenToolsSaveTemplateButton"
BUTTON_LOAD_TEMPLATE = "xGenToolsLoadButton"
BUTTON_CLEAN_START = "xGenToolsResetButton"
FOOTER_HELP = "xGenToolsFooterHelp"
FOOTER_AUTHOR = "xGenToolsFooterAuthor"
FOOTER_VERSION = "xGenToolsFooterVersion"

# Layout
WINDOW_WIDTH = 180
WINDOW_CONTENT_WIDTH = WINDOW_WIDTH - 10
WINDOW_HEIGHT = 700
SECTION_HEADER_HEIGHT = 25
FIELD_HEIGHT = 20
FIELD_ROW_HEIGHT = 28
ROW_NUMBER_WIDTH = 24
FOOTER_ROW_HEIGHT = 19
FOOTER_TEXT_HEIGHT = 16
FOOTER_SIDE_PADDING = 2

# Colors
CLEAN_START_HEADER_BACKGROUND = (0.82, 0.71, 0.334)
CLEAN_START_BODY_BACKGROUND = (0.30, 0.30, 0.30)
APPLY_ROW_COLOR = (0.23, 0.22, 0.40)
STEP_NUMBER_COLOR = (0.57, 0.56, 0.78)
FIELD_COLOR = (0.16, 0.16, 0.16)

# The top-level Outliner groups the workflow expects: pre-selected in fields 2 and 3 when the scene has them
GENERATION_GROUP_NAME = "GENERATION_BASES"
GUIDE_GROUP_NAME = "GUIDE_CURVES"

# Templates and scene naming
TEMPLATE_SUBDIR = os.path.join("xgen", "templates")
GEO_PATTERN = re.compile(r"^([A-Za-z])_(.+)_GEO$")
DEFAULT_XGEN_OUTPUT_RENDERER = "Arnold Renderer"

# Saved preferences (Maya optionVars)
OPTION_VAR_SAVE_TEMPLATE_PATH = "xGenTools_SaveTemplatePath"
OPTION_VAR_SAVE_TEMPLATE_DISPLAY = "xGenTools_SaveTemplateDisplay"
OPTION_VAR_GENERATION_GROUP = "xGenTools_GenerationGroup"
OPTION_VAR_GUIDE_GROUP = "xGenTools_GuideGroup"
OPTION_VAR_FROM_PREFIX = "xGenTools_FromPrefix"
OPTION_VAR_TO_PREFIX = "xGenTools_ToPrefix"
OPTION_VAR_MATERIAL = "xGenTools_Material"

# Dropdown labels
NO_CHANGE_MATERIAL = "No change"
SELECT_MATERIAL_LABEL = "Select material"
SELECT_GROUP_LABEL = "Select group"
SELECTED_TEMPLATE_LABEL = "selected template"
SELECT_PREFIX_LABEL = "Select prefix"
