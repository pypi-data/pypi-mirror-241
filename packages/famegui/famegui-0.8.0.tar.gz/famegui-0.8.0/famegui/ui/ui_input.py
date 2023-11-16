from PySide2.QtWidgets import QLineEdit, QComboBox


def set_placeholder_text(widget, text, enum_values=None):
    """Helper function to set the placeholder text of a widget."""
    if isinstance(widget, QLineEdit):
        widget: QLineEdit

        if text:
            widget.setText(str(text))

    if isinstance(widget, QComboBox):
        widget: QComboBox

        for idx, value in zip(range(widget.count()), enum_values):
            if value == text:
                widget.setCurrentIndex(idx)
                break
