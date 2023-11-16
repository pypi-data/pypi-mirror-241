from PySide2 import QtWidgets


def gen_quick_warning_modal(current_widget, title, description):
    """Generate a minimal warning modal"""
    QtWidgets.QMessageBox.warning(current_widget, title, description)
