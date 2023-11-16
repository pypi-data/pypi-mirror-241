from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import Qt
from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QFrame,
    QHBoxLayout,
    QSizePolicy,
    QFormLayout,
)
from fameio.source.schema import AttributeSpecs, AttributeType

from famegui.config.style_config import LIST_ITEM_STYLE


class BlockItemWrapper(QFrame):
    """Wrapper for all types of input panels. It it used to carry children of the blocks,  gather and manage  their
    data."""

    def __init__(self, parent=None, spec=None, attr_name=None):
        super().__init__(parent)
        self.parent = parent
        self.input_widget = None
        self.specs: AttributeSpecs = spec
        self.attr_name = attr_name
        if self.specs is None:
            raise ValueError("spec is None")

        if self.specs.attr_type == AttributeType.TIME_SERIES:
            self.vertical_row = QVBoxLayout(self)
        else:
            self.vertical_row = QHBoxLayout(
                self
            )  # QVBoxLayout(self) -> for Time Series

        if attr_name is None:
            raise ValueError("attr_name is None")

        self.vertical_row.setContentsMargins(8, 8, 8, 5)

        self.setStyleSheet(
            LIST_ITEM_STYLE
        )
        self.vertical_row.setAlignment(Qt.AlignTop)

    def get_attr_full_name(self):
        return self.specs.full_name

    def get_short_attr_name(self):
        return self.attr_name

    def get_attr_spec(self):
        return self.specs

    def add_widget(self, widget):
        """Add inner widget to the block item to display other widgets like buttons, labels, etc."""
        self.vertical_row.addWidget(widget)

        self.vertical_row.setAlignment(widget, Qt.AlignTop)

    def add_input_widget(self, widget):
        self.input_widget = widget

        self.vertical_row.addWidget(self.input_widget)

    def get_data(self):
        """Group and gather all the data from the input widget."""
        data = {}
        widget = self.input_widget

        if widget:
            if widget.__class__.__name__ == "BlockItemWrapper":
                data[self.attr_name] = widget.get_data()

                return data

            if isinstance(widget, QLineEdit):
                data[self.attr_name] = widget.text()

                return data

            if widget.__class__.__name__ == "BlockTypeWrapper":
                data[self.attr_name] = widget.get_data()

                return data

            if isinstance(widget, QWidget):
                if hasattr(widget, "get_input_value"):
                    data[self.attr_name] = widget.get_input_value()
                    return data

                else:
                    raise Exception("Widget has no attribute 'get_input_value'")

        return data
