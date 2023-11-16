from PySide2.QtGui import QPainter, QColor
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QFrame
from fameio.source.schema import AttributeSpecs

from famegui.ui.block_item_wrapper import BlockItemWrapper
from famegui.ui.block_type_wrapper import BlockTypeWrapper


class ListItem(QFrame):
    """Wrapper for all types of Sub Widgets of a List Widget."""

    def __init__(self, attr_name: str, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.attr_name = attr_name

        self.card_wrapper_layout = QVBoxLayout()
        self.setLayout(self.card_wrapper_layout)

        color = "rgba(255, 221, 148, 0.7)"
        self.setStyleSheet(
            f"ListItem {{background-color: {color};  border-radius: 5px;}}"
        )

        self.input_panel = None

    def get_attr_name(self):
        """Get the attribute short name."""
        return self.attr_name

    def set_panel_widget(self, widget):
        """Set the input panel widget."""
        self.input_panel = widget

        uniq_widget = f"myUniqueWidget-{id(self.input_panel)}"
        self.input_panel.setObjectName(uniq_widget)

        self.input_panel.update()
        self.update()

        self.layout().addWidget(widget)

    def get_attr(self) -> AttributeSpecs:
        """Get the AttributeSpecs of the input widget."""

        for i in range(self.layout().count()):
            item = self.layout().itemAt(i)
            if item:
                widget = item.widget()
                if isinstance(widget, BlockTypeWrapper):
                    widget: BlockTypeWrapper
                    return widget.attr_specs
                if isinstance(widget, BlockItemWrapper):
                    widget: BlockItemWrapper
                    return widget.get_attr_spec()
                if widget.__class__.__name__ == "InputPanelWrapper":
                    return widget.get_attribute_spec()

    def get_attribute_full_name(self) -> str:
        """Get the attribute full name."""
        for i in range(self.layout().count()):
            item = self.layout().itemAt(i)
            if item:
                widget = item.widget()
                if isinstance(widget, BlockTypeWrapper):
                    widget: BlockTypeWrapper
                    return widget.attr_specs.full_name
                if isinstance(widget, BlockItemWrapper):
                    widget: BlockItemWrapper
                    return widget.get_attr_full_name()
                if widget.__class__.__name__ == "InputPanelWrapper":
                    return widget.get_attribute_full_name()

    def _process_block_type_input(self, widget, data):
        inner_data = widget.get_data()
        for key, value in widget.get_data().items():
            inner_data[key] = value
        data[self.attr_name] = inner_data

    def _process_block_item_type_input(self, widget, data):
        for key, value in widget.get_data().items():
            data[key] = value

    def _process_input_panel_wrapper_input(self, widget, data):
        inner_data = widget.get_input_value()

        if isinstance(inner_data, dict):
            for key, value in inner_data.items():
                data[key] = value
        if isinstance(inner_data, list):
            spec = widget.get_attribute_spec()
            sepc: AttributeSpecs
            if spec.is_list:
                data[self.attr_name] = inner_data
                return
            for sub_data in inner_data:
                if isinstance(sub_data, dict):
                    for key, value in sub_data.items():
                        data[key] = value
                    continue
                data[self.attr_name] = inner_data

        return

    def get_data(self):
        """Group and gather all the data from the input widget."""

        data = {}

        for i in range(self.layout().count()):
            item = self.layout().itemAt(i)
            if item:
                widget = item.widget()

                if widget:
                    if isinstance(widget, QLineEdit):
                        data[self.attr_name] = widget.text()
                        continue

                    if isinstance(widget, BlockTypeWrapper):
                        self._process_block_type_input(widget, data)

                        continue

                    if isinstance(widget, BlockItemWrapper):
                        self._process_block_item_type_input(widget, data)

                        continue
                    if widget.__class__.__name__ == "InputPanelWrapper":
                        self._process_input_panel_wrapper_input(widget, data)

        return data
