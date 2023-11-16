import fameio.source.schema as schema

INPUT_ATTR_TYPE_COLORS = {
    schema.AttributeType.BLOCK: (255, 221, 148, 0.7),
    schema.AttributeType.LONG: (0, 188, 180, 200),
    schema.AttributeType.INTEGER: (255, 204, 75, 200),
    schema.AttributeType.ENUM: (255, 231, 32, 200),
    schema.AttributeType.DOUBLE: (39, 78, 221, 200),
    schema.AttributeType.TIME_SERIES: (255, 169, 33, 200),
}

DEFAULT_COLOR = (39, 78, 221, 200)
BORDER = "border: 1.5px {};"
BORDER_MANDATORY = "solid black"
BORDER_STANDARD = "dashed #141414"

ERROR_TEXT_STYLE_LABEL = "QLabel { background-color : #F66257; }"

ERROR_TEXT_STYLE_LINE_EDIT = "QLineEdit { background-color : #F66257; }"

FAME_CALENDAR_INPUT_STYLE = "QLineEdit { background: '#7BDFF2'; }"

FAME_LINE_EDIT_STYLE_DEFAULT = "background-color: #f5f5f5;"

FAME_LINE_EDIT_STYLE_ERR_STATE = ("QWidget{ background-color: rgba(255, 102, 102, 150);"
                                  " border: 2px dashed red; border-radius: 5px; }")

NON_SUPPORTED_LABEL_STYLE = "QLabel { background-color : #F66257; };"

FAME_CONSOLE_STYLE = "color: #F5F5F5;"

LIST_ITEM_STYLE = "background-color: rgba(255, 221, 148, 0.4); border-radius: 5px;"

DEFAULT_INPUT_STYLE = ("QTextEdit { padding-left: 20px; padding-right: 20px; background-color: #f5f5f5; "
                       "border: 1px solid #d0d0d0; border-radius: 5px; padding: 10px; color: #333; "
                       "font-size: 12px; font-family: Arial; } QTextEdit:focus { border: 1px solid #0078d4; }"
                       " QTextEdit QScrollBar:vertical { border: none; background: #f5f5f5; width: 10px; margin: 0; }"
                       " QTextEdit QScrollBar::handle:vertical { background: #d0d0d0; min-height: 20px; }"
                       " QTextEdit QScrollBar::add-line:vertical,"
                       " QTextEdit QScrollBar::sub-line:vertical { border: none; background: none; }"
                       " QTextEdit QScrollBar:horizontal { border: none; background: #f5f5f5; height: 10px; margin: 0; }"
                       " QTextEdit QScrollBar::handle:horizontal { background: #d0d0d0; min-width: 20px; }"
                       " QTextEdit QScrollBar::add-line:horizontal,"
                       " QTextEdit QScrollBar::sub-line:horizontal { border: none; background: none; }")

REMOVE_BTN_STYLE = ("QPushButton { background-color: #D32F2F; color: white; "
                    "border: none; padding: 10px; border-radius: 5px; } "
                    "QPushButton:hover { background-color: #F44336; }"
                    " QPushButton:pressed { background-color: #B71C1C; }")

COLLAPSE_BTN_STYLE = (
    "QPushButton { background-color: #607D8B; color: white; border: none;"
    " padding: 10px; border-radius: 5px; } "
    "QPushButton:hover { background-color: #78909C; }"
    " QPushButton:pressed { background-color: #455A64; }")


def get_color_for_type(attr_spec) -> str:
    """Returns the background color for the attribute type"""
    color = INPUT_ATTR_TYPE_COLORS.get(attr_spec.attr_type, DEFAULT_COLOR)
    return f"rgba{color}"


def get_default_input_style(uniq_widget_object_name: str) -> str:
    return \
        f"""#{uniq_widget_object_name} 
        {{ background-color: rgba(183, 254, 255, 0.4);
         border: 2px dashed grey; border-radius: 5px; }}"""


def get_default_err_input_style(uniq_widget_object_name: str) -> str:
    return \
        (f"#{uniq_widget_object_name} "
         f"{{ background-color: rgba(255, 102, 102, 150);"
         f" border: 2px dashed red; border-radius: 5px; }}")


def get_border_for_type(attr_spec: schema.AttributeSpecs) -> str:
    """Returns border style depending on type"""
    border_style = BORDER_MANDATORY if attr_spec.is_mandatory else BORDER_STANDARD
    return BORDER.format(border_style)
