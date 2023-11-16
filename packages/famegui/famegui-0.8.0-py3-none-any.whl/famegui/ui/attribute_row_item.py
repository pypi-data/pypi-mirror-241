import logging
import re
import typing

import fameio.source.schema as schema
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import QSize, Signal
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QVBoxLayout, QPushButton, QLabel, QSizePolicy, QHBoxLayout
from fameio.source.scenario import Attribute
from fameio.source.schema import AttributeSpecs

from famegui.appworkingdir import AppWorkingDir
from famegui.config.static_ui_descriptions import NO_SUPPORTED_EDIT_WIDGET_TEXT
from famegui.config.style_config import get_color_for_type, get_border_for_type, ERROR_TEXT_STYLE_LABEL, \
    ERROR_TEXT_STYLE_LINE_EDIT
from famegui.ui.block_item_wrapper import BlockItemWrapper
from famegui.ui.block_type_wrapper import BlockTypeWrapper
from famegui.ui.fame_input_panels import FileChooserWidgetPanel
from famegui.ui.fame_ui_elements import QFameBoldLabel, DescriptionLabel
from famegui.ui.list_block import CustomListWidget

from famegui.ui.ui_input import set_placeholder_text
from famegui.ui.ui_input_panel_wrapper import InputPanelWrapper


class RootAttributeInputPanelWrapper(QtWidgets.QWidget):
    """Wrapper for the root level attribute input panels. It is used to toggle the visibility
    of the input panels and mange all nested input panels.
    """

    def __init__(self, row, panel, parent=None):
        super(RootAttributeInputPanelWrapper, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        layout = QVBoxLayout(self)
        self.layout = layout
        self.layout.setSpacing(10)
        self.content_frame: QtWidgets.QWidget = QtWidgets.QWidget(self)

        self.row: AttributeTreeItem = row
        button = QPushButton("Collapse/Expand")
        layout.addWidget(button)
        button.clicked.connect(self.toggle_content)
        layout.addWidget(self.content_frame)

        content_layout = QVBoxLayout(self.content_frame)

        self.panel = panel

        content_layout.addWidget(self.panel)

        self.initial_width = self.width()

        self.content_frame.setVisible(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def toggle_size_adjustment(self):
        """Toggle the size adjustment of the parent widget."""
        self.adjustSize()

        self.updateGeometry()
        self.row.setSizeHint(0, QSize(-1, 60))
        self.row.setSizeHint(1, QSize(-1, 60))
        self.parent().setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.parent().updateGeometry()
        self.parent().adjustSize()

    def toggle_content(self):
        """Toggle the visibility of the input panel by triggering layout updates."""

        if self.content_frame.isVisible():
            self.content_frame.hide()

        else:
            self.content_frame.show()

        self.parent().updateGeometry()
        self.parent().adjustSize()
        self.parent().update()

    def height(self):
        """Get the pre-calculated height of the input panel."""
        return self.content_frame.sizeHint().height() + 50


class AttributeTreeItem(QtWidgets.QTreeWidgetItem):
    """Root Holder class for all attribute tree items.
    It is used to create a tree of attributes and their input panels to access all attributes .
    """

    def __init__(
            self,
            parent: QtWidgets.QTreeWidget,
            attr_name: str,
            attr_spec: schema.AttributeSpecs,
            schema: schema.Schema,
            working_dir: AppWorkingDir,
            validation_signal: Signal = None,
            validation_error_signal: Signal = None,
            default_value=None,
    ):
        self.state_value_dict = {}
        self._attr_name = attr_name
        self._attr_spec: AttributeSpecs = attr_spec
        self.validation_signal: Signal = validation_signal
        self.validation_error_signal: Signal = validation_error_signal
        self._working_dir = working_dir
        self._default_value = default_value
        self._attr_value = None
        self._display_error = lambda has_error: None
        self.initial_height = 0
        self.schema = schema
        self.holder_widget = None

        QtWidgets.QTreeWidgetItem.__init__(self, parent, [attr_name])

        font = self.font(0)
        if self._attr_spec.is_mandatory:
            font.setBold(True)

            tooltip = self.tr("{} (mandatory)").format(self._attr_name)
        else:
            font.setItalic(True)
            tooltip = self.tr("{} (optional)").format(self._attr_name)

        self.setFont(0, font)
        self.setToolTip(0, tooltip)
        self.ui_parent = parent
        self.panel = self._create_edit_widget()

        self.holder_widget = RootAttributeInputPanelWrapper(
            self, self.panel, self.treeWidget()
        )

        color_str = get_color_for_type(self._attr_spec)

        self.holder_widget.setStyleSheet(
            f"RootAttributeInputPanelWrapper {{  background:{color_str}; border-radius: 5px;"
            "margin-top:10px; margin-bottom:30px; margin-left: 5px; margin-right: 5px; }}"
        )

        parent.setItemWidget(self, 1, self.holder_widget)
        self.holder_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def get_attr_spec(self):
        """Get the root AttributeSpecs of the row."""
        return self._attr_spec

    @property
    def attr_name(self) -> str:
        """Get the attribute short name of the root attribute ."""
        return self._attr_name

    def remove_none_values_and_empty_elements(self, item):
        """Recursively remove all None values and empty elements from a dictionary or list to clean up the data
        prepared for saving to a file
        """
        if isinstance(item, dict):
            # Handle dictionary: recursively clean its key-value pairs
            new_dict = {
                k: self.remove_none_values_and_empty_elements(v)
                for k, v in item.items()
                if v is not None
            }
            return {k: v for k, v in new_dict.items() if v not in [None, {}, []]}
        elif isinstance(item, list):
            # Handle list: recursively clean its elements
            new_list = [self.remove_none_values_and_empty_elements(v) for v in item]
            return [v for v in new_list if v not in [None, {}, []]]
        else:
            # Base case: return the item as-is
            return item

    def remove_none_values(self, d):
        """Helper function to remove None values from a dictionary."""
        if not isinstance(d, dict):
            return d
        return {k: self.remove_none_values(v) for k, v in d.items() if v is not None}

    @property
    def attr_value(self) -> typing.Any:
        """Get clean attribute value from a complete row"""

        cleaned_data = self.remove_none_values_and_empty_elements(
            self._get_data_from_input()
        )

        return cleaned_data

    @property
    def validation_error(self) -> typing.Optional[str]:
        if self._attr_spec.is_mandatory and self._attr_value is None:
            return "mandatory attribute '{}' is missing".format(self.attr_name)
        return None

    _supported_list_types = [
        schema.AttributeType.INTEGER,
        schema.AttributeType.LONG,
        schema.AttributeType.DOUBLE,
    ]

    @property
    def _attr_enum_values(self) -> typing.List[str]:
        """Returns the enum values of the attached AttributeSpecs"""
        assert self._attr_spec.attr_type == schema.AttributeType.ENUM
        assert not self._attr_spec.is_list
        assert not self._attr_spec.has_nested_attributes
        return self._attr_spec.values

    def build_parent_container(self, attr_spec_inner, attr_name: str, holder_widget) -> QtWidgets.QWidget:
        """Build a parent container for a block type attribute with an n depth of nested attributes"""

        value = attr_spec_inner.help_text or ""
        desc = DescriptionLabel(text=value)

        label = QFameBoldLabel(
            text=f"{attr_name}: {attr_spec_inner.attr_type.name} "
        )
        label.setWordWrap(True)

        parent_layout = QVBoxLayout()

        parent_container = BlockTypeWrapper(
            block_type_layout=parent_layout,
            spec=attr_spec_inner,
            attr_name=attr_name,
        )

        layout_header = QVBoxLayout()
        header_widget = QtWidgets.QWidget()

        header_widget.setLayout(layout_header)
        layout_header.insertWidget(0, label)
        layout_header.insertWidget(1, desc)

        parent_layout.insertWidget(0, header_widget)

        # Wrap holder_widget with a parent container and chevron icon

        # Set the stylesheet for the specific widget using its object name

        chevron_button = QPushButton(
            "Expand/Collapse"
        )  # Using a triangle as a placeholder for the chevron icon

        chevron_button.setCheckable(True)

        # Set the initial checked state to match the initial visibility of holder_widget
        chevron_button.setChecked(True)
        chevron_button.toggled.connect(holder_widget.setVisible)
        parent_layout.addWidget(chevron_button)
        parent_layout.addWidget(holder_widget)

        return parent_container

    def build_child_sub_block_list(self, attr_spec_inner, attr_name, holder: QVBoxLayout, list_data=None):
        """Build a child list block panel for a block"""

        preset_value_list = self.get_default_value(
            attr_spec_inner, attr_spec_inner.full_name, list_data
        )

        block_list = self.build_sub_block_list(
            attr_spec_inner, preset_value_list
        )

        dynamic_list = CustomListWidget(
            block_list, attr_spec_inner, self.schema, attr_name=attr_name
        )

        dynamic_list.row_creation_requested.connect(self._add_list_row)

        holder.set_widget(dynamic_list)

    def build_primitive_block_child(self, attr_spec_inner: AttributeSpecs, attr_name: str, holder: QVBoxLayout,
                                    list_data=None):
        """Build a primitive child input panel for a block"""
        default_row = QFameBoldLabel(
            text=f"{attr_name}: {attr_spec_inner.attr_type.name}"
        )

        default_row.setWordWrap(True)
        value = attr_spec_inner.help_text or ""

        desc = DescriptionLabel(text=value)

        parent_widget = BlockItemWrapper(spec=attr_spec_inner, attr_name=attr_name)

        parent_widget.add_widget(default_row)
        parent_widget.add_widget(desc)
        prim_widget = self.get_primitive_input_panel(attr_spec_inner, list_data)

        uniq_widget = f"myUniqueWidget-{id(parent_widget)}"

        parent_widget.setObjectName(uniq_widget)

        color_str = get_color_for_type(attr_spec_inner)

        border_style = get_border_for_type(attr_spec_inner)

        parent_widget.setStyleSheet(
            f"#{uniq_widget} {{"
            f"    background-color: {color_str};"
            f"    {border_style}"
            "    border-radius: 5px;"
            "}"
        )

        parent_widget.add_input_widget(prim_widget)

        holder.addWidget(parent_widget)

    def build_sub_block_list(self, attr_data: AttributeSpecs, list_data=None):
        """Build a list of sub blocks for a block type attribute with an n depth of nested attributes"""
        holder = QVBoxLayout()

        for item, attr_spec_inner in attr_data.nested_attributes.items():
            attr_spec_inner: AttributeSpecs

            if attr_spec_inner.attr_type == schema.AttributeType.BLOCK:
                holder_widget = self.build_sub_block_list(attr_spec_inner, list_data)

                parent_container = self.build_parent_container(
                    attr_spec_inner, item, holder_widget
                )

                input_wrapper = InputPanelWrapper(
                    inner_widget=parent_container,
                    signal_to_connect=self.validation_signal,
                    validation_error_signal=self.validation_error_signal,
                    attr_name=item,
                    attribute=attr_spec_inner,
                )

                holder.addWidget(input_wrapper)
                continue

            if attr_spec_inner.is_list:
                self.build_child_sub_block_list(attr_spec_inner, item, holder, list_data)

                continue

            self.build_primitive_block_child(attr_spec_inner, item, holder, list_data)

            ## here

        default_data_dict = self.get_default_value(
            attr_data, self._attr_spec.full_name, list_data
        )

        holder_wrapper = BlockTypeWrapper(
            block_type_layout=holder,
            spec=attr_data,
            attr_name=self.attr_name,
            dict_data=default_data_dict,
        )

        return holder_wrapper

    def get_list_capable_int_or_long_input_panel(self, spec: AttributeSpecs, nested_list):
        preset_value = str(
            self.get_default_value(spec, spec.full_name, nested_list)
        )

        line_edit = self._create_line_edit("0", None)
        line_edit.setText(preset_value)
        line_edit.setValidator(QtGui.QIntValidator())

        input_wrapper = InputPanelWrapper(
            inner_widget=line_edit,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def get_list_capable_time_series_input_panel(self, spec: AttributeSpecs, nested_list):
        preset_value = self.get_default_value(spec, spec.full_name, nested_list)

        file_chooser = FileChooserWidgetPanel(
            self._working_dir,
            spec.attr_type.name,
            preset_value,
            self.ui_parent,
        )

        self._display_error = file_chooser.display_error

        input_wrapper = InputPanelWrapper(
            inner_widget=file_chooser,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def get_list_capable_enum_input_panel(self, spec: AttributeSpecs, nested_list):
        combo_box = QtWidgets.QComboBox()
        enum_values = spec.values

        combo_box.addItems(enum_values)
        if len(enum_values) == 1:
            combo_box.setCurrentIndex(0)
            self._attr_value = enum_values[0]
        else:
            combo_box.setCurrentIndex(-1)

        preset_value = self.get_default_value(spec, spec.full_name, nested_list)

        set_placeholder_text(combo_box, preset_value, enum_values)

        input_wrapper = InputPanelWrapper(
            inner_widget=combo_box,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def get_list_capable_double_input_panel(self, spec: AttributeSpecs, nested_list):
        preset_value = str(
            self.get_default_value(spec, spec.full_name, nested_list)
        )

        line_edit = self._create_line_edit(preset_value, None)

        line_edit.setText(preset_value)
        validator = QtGui.QDoubleValidator()
        # accept '.' as decimal separator
        validator.setLocale(QtCore.QLocale.English)
        line_edit.setValidator(validator)

        input_wrapper = InputPanelWrapper(
            inner_widget=line_edit,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )

        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def get_primitive_input_panel(self, spec, nested_list):
        """Get a primitive input panel for a given attribute spec"""
        if spec.attr_type == schema.AttributeType.ENUM:

            return self.get_list_capable_enum_input_panel(spec, nested_list)


        elif spec.attr_type == schema.AttributeType.TIME_SERIES:

            return self.get_list_capable_time_series_input_panel(spec, nested_list)

        elif (
                spec.attr_type == schema.AttributeType.INTEGER
                or spec.attr_type == schema.AttributeType.LONG
        ):

            return self.get_list_capable_int_or_long_input_panel(spec, nested_list)

        elif spec.attr_type == schema.AttributeType.DOUBLE:

            return self.get_list_capable_double_input_panel(spec, nested_list)

        elif spec.attr_type == schema.AttributeType.BLOCK:

            return self.build_scroll_block_edit_widget(spec, nested_list)

    def _add_list_row(self, spec: AttributeSpecs, widget: QtWidgets.QWidget):
        """Add a new row to a list after the user clicked the add button"""
        widget: CustomListWidget
        block_list = self.build_sub_block_list(spec)

        input_wrapper = InputPanelWrapper(
            inner_widget=block_list,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )

        widget.set_widget(input_wrapper)

        self.ui_parent.update()

    def _create_edit_widget(self) -> QtWidgets.QWidget:
        """Create a input panel edit widget for the attribute"""
        spec = self._attr_spec

        if spec.is_list:
            return self.build_list_edit_widget(spec)

        if spec.attr_type == schema.AttributeType.ENUM:

            return self.build_enum_chooser_input_panel(spec)

        elif spec.attr_type == schema.AttributeType.TIME_SERIES:

            return self.build_time_series_edit_widget(spec)

        # INT INPUT PANEL

        elif (
                spec.attr_type == schema.AttributeType.INTEGER
                or spec.attr_type == schema.AttributeType.LONG
        ):
            return self.build_int_or_long_edit_widget(spec)

        # DOUBLE  INPUT PANEL
        elif spec.attr_type == schema.AttributeType.DOUBLE:

            return self.build_double_edit_widget(spec)

        elif spec.attr_type == schema.AttributeType.BLOCK:

            return self.build_block_edit_widget(spec)

    def build_block_edit_widget(self, spec: AttributeSpecs):
        block_list = self.build_sub_block_list(spec)

        input_wrapper = InputPanelWrapper(
            inner_widget=block_list,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def build_double_edit_widget(self, spec: AttributeSpecs):
        preset_value = self.get_default_value(spec, spec.full_name)

        line_edit = self._create_line_edit(preset_value, None)

        line_edit.setText(preset_value)
        validator = QtGui.QDoubleValidator()
        # accept '.' as decimal separator
        validator.setLocale(QtCore.QLocale.English)
        line_edit.setValidator(validator)

        input_wrapper = InputPanelWrapper(
            inner_widget=line_edit,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}

        return input_wrapper

    def build_enum_chooser_input_panel(self, spec: AttributeSpecs):
        combo_box = QtWidgets.QComboBox()
        enum_values = self._attr_enum_values
        combo_box.addItems(enum_values)
        if len(enum_values) == 1:
            combo_box.setCurrentIndex(0)
            self._attr_value = enum_values[0]
        else:
            combo_box.setCurrentIndex(-1)

        preset_value = self.get_default_value(
            spec,
            spec.full_name,
        )

        set_placeholder_text(combo_box, preset_value, enum_values)

        input_wrapper = InputPanelWrapper(
            inner_widget=combo_box,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}

        return input_wrapper

    def build_scroll_block_edit_widget(self, spec: AttributeSpecs, nested_list):
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        block_list = self.build_sub_block_list(spec, nested_list)

        scroll_area.setLayout(block_list)

        input_wrapper = InputPanelWrapper(
            inner_widget=block_list,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def build_time_series_edit_widget(self, spec: AttributeSpecs):
        preset_value = self.get_default_value(spec, spec.full_name)

        file_chooser = FileChooserWidgetPanel(
            self._working_dir, spec.attr_type.name, preset_value, self.treeWidget()
        )

        self._display_error = file_chooser.display_error

        input_wrapper = InputPanelWrapper(
            inner_widget=file_chooser,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def build_int_or_long_edit_widget(self, spec: AttributeSpecs):
        line_edit = self._create_line_edit("0", None)
        preset_value = self.get_default_value(spec, spec.full_name)
        line_edit.setText(preset_value)
        line_edit.setValidator(QtGui.QIntValidator())

        input_wrapper = InputPanelWrapper(
            inner_widget=line_edit,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def build_list_edit_widget(self, spec: AttributeSpecs):
        preset_value = self.get_nested_list_data()

        if preset_value is None:
            preset_value = []

        for item, idx in zip(preset_value, range(len(preset_value))):
            item: dict
            for k, v in item.items():
                v: Attribute

        if isinstance(preset_value, list):
            dynamic_list = None

            for item, idx in zip(preset_value, range(len(preset_value))):
                if idx == 0:
                    block_list = self.build_sub_block_list(spec, [item])

                    dynamic_list = CustomListWidget(
                        block_list, spec, self.schema, self.attr_name
                    )
                    continue

                item: dict

                block_list = self.build_sub_block_list(spec, [item])

                input_wrapper = InputPanelWrapper(
                    inner_widget=block_list,
                    validation_error_signal=self.validation_error_signal,
                    signal_to_connect=self.validation_signal,
                    attribute=spec,
                )

                dynamic_list.set_widget(input_wrapper)

            if dynamic_list is None:
                block_list = self.build_sub_block_list(spec)

                dynamic_list = CustomListWidget(
                    block_list, spec, self.schema, self.attr_name
                )

            dynamic_list.row_creation_requested.connect(self._add_list_row)

            input_wrapper = InputPanelWrapper(
                inner_widget=dynamic_list,
                validation_error_signal=self.validation_error_signal,
                signal_to_connect=self.validation_signal,
                attribute=spec,
            )

            self.state_value_dict = {spec.full_name: input_wrapper}

            return input_wrapper

        block_list = self.build_sub_block_list(spec, preset_value)

        dynamic_list = CustomListWidget(
            block_list, spec, self.schema, self.attr_name
        )

        dynamic_list.row_creation_requested.connect(self._add_list_row)

        input_wrapper = InputPanelWrapper(
            inner_widget=dynamic_list,
            validation_error_signal=self.validation_error_signal,
            signal_to_connect=self.validation_signal,
            attribute=spec,
        )
        self.state_value_dict = {spec.full_name: input_wrapper}
        return input_wrapper

    def search_attr_recursively(self, attr: Attribute, attr_full_name: str):
        """Search for a specific and primitive  nested attribute recursively"""
        for nested_key, nested_item in attr.nested.items():
            nested_item: Attribute

            if attr_full_name == str(nested_key):
                return nested_item

            if nested_item.has_nested:
                temp_result = self.search_attr_recursively(nested_item, attr_full_name)
                if temp_result:
                    return temp_result
                continue

        return None

    def recursive_search(self, data, key):
        """Search for a specific and primitive  nested attribute recursively for any data type"""
        if isinstance(data, list):
            for item in data:
                result = self.recursive_search(item, key)
                if result:
                    return result
        elif isinstance(data, dict):
            if key in data:
                return data[key]
            for k, v in data.items():
                result = self.recursive_search(v, key)
                v: Attribute
                if v.has_nested:
                    result = self.recursive_search(v.nested, key)

                if result:
                    return result
        return None

    def get_nested_list_data(self):
        """Get the nested list data from the root attribute spec
        Since one row can have multiple nested lists,
        we need to get the data from the root attribute spec and then search for the specific nested list data recursively
        """
        if self._default_value:
            if self._default_value.has_nested_list:
                nested_list = self._default_value.nested_list

                return nested_list
        return None

    def get_default_value(
            self, spec: AttributeSpecs, attr_full_name, nested_list_data=None
    ):
        """Get the saved value for a given attribute spec ( if it exists)"""
        self._default_value: Attribute

        if nested_list_data:
            matches = re.findall(r"(?<=\.)[^.]*$", attr_full_name)

            attr_short_name = matches[0]

            result = self.recursive_search(nested_list_data, attr_short_name)
            if result:
                return str(result.value)

        if self._default_value:
            if self._default_value.has_nested_list:
                matches = re.findall(r"(?<=\.)[^.]*$", attr_full_name)

                attr_short_name = matches[0]

                nested_list = self._default_value.nested_list

                result = self.recursive_search(nested_list, attr_short_name)
                if result:
                    if result.has_value:
                        return str(result.value)

                return None

        matches = re.findall(r"(?<=\.)[^.]*$", attr_full_name)

        attr_short_name = matches[0]

        if self._default_value:
            if self._default_value.has_nested:
                search_attr_recursively = self.search_attr_recursively(
                    self._default_value, attr_short_name
                )

                if search_attr_recursively:
                    if search_attr_recursively.has_value:
                        return str(search_attr_recursively.value)

        spec_attr_fallback_value = ""

        if not self._default_value:
            return spec_attr_fallback_value

        default_value = ""

        self._default_value: Attribute

        if self._default_value.has_nested:
            for nested_key, nested_item in self._default_value.nested.items():
                nested_item: Attribute

                if attr_full_name.__contains__(str(nested_key)):
                    if nested_item.has_value:
                        default_value = nested_item.value

                    return str(default_value)

        if self._default_value.has_value:
            default_value = str(self._default_value.value)

        default_value = (
            default_value if default_value is not None else spec_attr_fallback_value
        )

        return str(default_value)

    def _create_line_edit(self, placeholder_text: str, handler) -> QtWidgets.QLineEdit:
        """Create a line edit widget for the attribute"""
        line_edit = QtWidgets.QLineEdit()
        line_edit.setText(placeholder_text)
        self._display_error = (
            lambda has_error: line_edit.setStyleSheet(
                ERROR_TEXT_STYLE_LINE_EDIT
            )
            if has_error
            else line_edit.setStyleSheet("")
        )
        return line_edit

    def _create_unsupported_edit_widget(self, type_name: str) -> QtWidgets.QLabel:
        """Create a label widget for an unsupported attribute type (Leave for future implementation for new kinds of
        attributes)"""

        logging.error(
            NO_SUPPORTED_EDIT_WIDGET_TEXT.format(
                type_name
            )
        )
        label = QtWidgets.QLabel()
        label.setText(
            self.tr(NO_SUPPORTED_EDIT_WIDGET_TEXT.format(type_name))
        )
        label.setStyleSheet(ERROR_TEXT_STYLE_LABEL)
        return label

    def _get_data_from_input(self):
        """Get the data from the input panel"""

        attr_data = self.panel.get_input_value()

        return attr_data

    def tr(self, msg: str) -> str:
        return QtCore.QCoreApplication.translate("AttributeTreeItem", msg)
