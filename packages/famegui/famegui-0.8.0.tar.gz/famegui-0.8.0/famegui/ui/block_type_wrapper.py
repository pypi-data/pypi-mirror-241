import re
from datetime import datetime

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QFrame
from fameio.source.schema import AttributeSpecs, AttributeType

from famegui.ui.block_item_wrapper import BlockItemWrapper


class BlockTypeWrapper(QFrame):
    """Wrapper for all types of Block input panels. It is used to validate input and style it accordingly to their type.
    This Wrapper is used for the BlockType input panels compared to the primitive input panels.
    """

    def __init__(
            self,
            parent=None,
            block_type_layout=None,
            spec: AttributeSpecs = None,
            attr_name=None,
            dict_data=None,
    ):
        super().__init__(parent)
        self.block_type_layout: QVBoxLayout = block_type_layout
        self.setLayout(self.block_type_layout)

        matches = re.findall(r"(?<=\.)[^.]*$", spec.full_name)

        attr_short_name = matches[0]
        self.attr_name = attr_short_name

        self.dict_data = dict_data

        self.attr_specs: AttributeSpecs = spec
        self.parent = parent
        uniq_obj_name = f"myUniqueWidget-{id(self)}"
        self.setObjectName(uniq_obj_name)
        color_str = "rgba(255, 221, 148, 0.4)"

        stylesheet = (
            f"#{uniq_obj_name} {{ background-color: {color_str};  border-radius: 5px;}}"
        )

        self.setStyleSheet(stylesheet)

    def get_attr_full_name(self):
        return self.attr_specs.full_name

    def get_attr_name(self):
        """Get the attribute short name."""
        return self.attr_name

    def _process_block_type_input(self, widget, data_list, data):
        widget: BlockTypeWrapper
        inner_data = {}
        for key, value in widget.get_data().items():
            inner_data[key] = value
        data_list.append(inner_data)

        if widget.attr_name in widget.get_data():
            inner_data = {}
            for key, value in widget.get_data().items():
                inner_data[key] = value

        if self.get_attr_name() in widget.get_data():
            for key, value in widget.get_data().items():
                data[key] = value
            return

        data[widget.get_attr_name()] = inner_data

    def _process_block_item_type_input(self, widget, data_list, data):
        widget: BlockItemWrapper

        inner_data = {}
        for key, value in widget.get_data().items():
            inner_data[key] = value

        data[widget.get_short_attr_name()] = inner_data

        if self.attr_specs.is_list:
            pass
        for key, value in widget.get_data().items():
            data[key] = value

        if self.attr_specs.is_list:
            inner_data = {}
            for key, value in widget.get_data().items():
                inner_data[key] = value
            data_list.append(inner_data)
        return

    def _process_input_panel_wrapper(self, widget, data_list, data):
        if self.attr_specs.is_list:
            data_list.append(widget.get_input_value())
        inner_data = widget.get_input_value()

        if widget.get_short_attr_name() in inner_data:
            for item_key, item_value in inner_data.items():
                data[item_key] = item_value
            return

        data[widget.get_short_attr_name()] = inner_data

    def get_data(self):
        """Group and gather all the data from the input widget."""

        data = {}
        data_list = []

        for i in range(self.layout().count()):
            item = self.layout().itemAt(i)
            if item:
                widget = item.widget()

                if widget:
                    if isinstance(widget, QLineEdit):
                        data[self.attr_name] = widget.text()

                        if self.attr_specs.is_list:
                            data_list.append(widget.text())
                        continue

                    if isinstance(widget, BlockTypeWrapper):
                        self._process_block_type_input(widget, data_list, data)

                    if isinstance(widget, BlockItemWrapper):
                        self._process_block_item_type_input(widget, data_list, data)

                    if widget.__class__.__name__ == "InputPanelWrapper":
                        self._process_input_panel_wrapper(widget, data_list, data)

        if self.attr_specs.is_list:
            return data_list

        first_key = next(iter(data))

        list_of_dicts = data[first_key]
        if not isinstance(list_of_dicts, list):
            return data
        if not self.attr_specs.has_nested_attributes:
            return data

        for attr_name, attr_spec in self.attr_specs.nested_attributes.items():
            if attr_spec.is_list:
                continue
            single_dict = {k: v for d in list_of_dicts for k, v in d.items()}
            data[first_key] = single_dict

        return data
