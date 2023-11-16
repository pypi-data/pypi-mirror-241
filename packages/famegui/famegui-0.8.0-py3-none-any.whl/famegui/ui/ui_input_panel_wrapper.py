import re
import typing

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QFrame

from famegui.config.style_config import get_default_input_style, get_default_err_input_style
from famegui.ui.block_item_wrapper import BlockItemWrapper
from famegui.ui.block_type_wrapper import BlockTypeWrapper
from famegui.ui.fame_input_panels import FileChooserWidgetPanel
from fameio.source.schema import AttributeSpecs

import fameio.source.schema as schema

from famegui.ui.list_block import CustomListWidget


class InputPanelWrapper(QFrame):
    """Wrapper for all types of input panels. It is used to validate input and style it accordingly to their type."""

    def __init__(
            self,
            parent=None,
            inner_widget: typing.Optional[QWidget] = None,
            signal_to_connect: Signal = None,
            validation_error_signal: Signal = None,
            attribute: AttributeSpecs = None,
            attr_name: str = None,
    ):
        super().__init__(parent)
        self._attribute_spec: AttributeSpecs = attribute
        self._inner_widget = inner_widget
        self.info_panel = QLabel("")
        self.attr_name = attr_name
        self.original_stylesheet = None
        self.validation_error_signal = validation_error_signal
        self.setContentsMargins(0, 0, 0, 0)

        if attr_name is None:
            matches = re.findall(r"(?<=\.)[^.]*$", self._attribute_spec.full_name)

            attr_short_name = matches[0]
            self.attr_name = attr_short_name

        if not self.validation_error_signal:
            assert False, "validation_error_signal is None"

        self._init_layout()
        if inner_widget:
            self._inner_layout.addWidget(inner_widget)

        self._inner_layout.setSpacing(0)

        if signal_to_connect:
            signal_to_connect.connect(self.validate_input)
        else:
            raise ValueError("signal_to_connect is None")

        self._inner_layout.addWidget(self.info_panel)

        uniq_obj_name = f"myUniqueWidget-{id(inner_widget)}"
        inner_widget.setObjectName(uniq_obj_name)
        inner_widget.setStyleSheet(
            get_default_input_style(uniq_obj_name)
        )
        self.original_stylesheet = inner_widget.styleSheet()
        self._signal_to_connect = signal_to_connect

    def get_attribute_spec(self):
        """Return attribute spec"""
        return self._attribute_spec

    def get_short_attr_name(self):
        """Return short attribute name"""
        return self.attr_name

    def get_attribute_full_name(self) -> str:
        """Return full attribute name"""
        return self._attribute_spec.full_name

    def _init_layout(self):
        self._inner_layout = QVBoxLayout()
        self.setLayout(self._inner_layout)

        self._inner_layout.setContentsMargins(0, 0, 0, 0)
        self._inner_layout.setSpacing(0)

    def _has_more_than_two_dots(self, s: str) -> bool:
        """Helper function to get the short name of an attribute"""
        return s.count(".") > 0

    def validate_input(self):
        """validate input and style input panel accordingly to their type"""
        if self._attribute_spec.is_mandatory:
            if self.get_input_value() is None:

                if self._inner_widget:
                    if self._attribute_spec.attr_type == schema.AttributeType.BLOCK:
                        return

                    self.info_panel.setText(
                        f'<font color="red">Please fill in {self._attribute_spec.full_name}</font>'
                    )

                    if isinstance(self._inner_widget, FileChooserWidgetPanel):
                        self._inner_widget: FileChooserWidgetPanel
                        self._inner_widget.set_validation_state(False)

                    if self._inner_widget.objectName():
                        obj_name = self._inner_widget.objectName()
                        self._inner_widget.setStyleSheet(
                            get_default_err_input_style(obj_name)

                        )
                        self.validation_error_signal.emit(
                            False, self._attribute_spec.full_name
                        )

                        return False
                    uniq_obj_name = f"myUniqueWidget-{id(self._inner_widget)}"
                    self._inner_widget.setObjectName(uniq_obj_name)
                    self._inner_widget.setStyleSheet(
                        get_default_err_input_style(uniq_obj_name)

                    )
                self.validation_error_signal.emit(False, self._attribute_spec.full_name)

                return False

        self._inner_widget.setStyleSheet(self.original_stylesheet)
        self.info_panel.setText(f"")
        if isinstance(self._inner_widget, FileChooserWidgetPanel):
            self._inner_widget: FileChooserWidgetPanel
            self._inner_widget.set_validation_state(True)
        self.validation_error_signal.emit(True, self._attribute_spec.full_name)

        return True

    def convert_text_to_type(self, text: str, attr_type: schema.AttributeType):
        """Convert text to the type of attribute to save it to the scenario"""

        if not text:
            return None

        if attr_type == schema.AttributeType.INTEGER or attr_type == schema.AttributeType.LONG:
            return int(text) if text else None
        elif attr_type == schema.AttributeType.DOUBLE:
            return float(text) if text else None
        elif attr_type == schema.AttributeType.STRING:
            return text

        return text

    def get_input_value(self):
        """Get input values in form of a dict"""
        if isinstance(self._inner_widget, QLineEdit):
            return (
                self.convert_text_to_type(
                    self._inner_widget.text(), self._attribute_spec.attr_type
                )
                if self._inner_widget.text() != ""
                else None
            )
        elif isinstance(self._inner_widget, QComboBox):
            return (
                self._inner_widget.currentText()
                if self._inner_widget.currentText() != ""
                else None
            )

        elif isinstance(self._inner_widget, FileChooserWidgetPanel):
            return (
                self._inner_widget.get_path()
                if self._inner_widget.get_path() != ""
                else None
            )

        elif isinstance(self._inner_widget, BlockTypeWrapper):
            self._inner_widget: BlockTypeWrapper

            return (
                self._inner_widget.get_data()
                if self._inner_widget.get_data() != ""
                else None
            )

        elif isinstance(self._inner_widget, BlockItemWrapper):
            self._inner_widget: BlockItemWrapper
            block_item_data = self._inner_widget.get_data()

            if isinstance(block_item_data, dict):
                return (
                    self._inner_widget.get_data()
                    if self._inner_widget.get_data() != ""
                    else None
                )
            if isinstance(block_item_data, str):
                return (
                    self.convert_text_to_type(
                        self._inner_widget.get_data(), self._attribute_spec.attr_type
                    )
                    if self._inner_widget.get_data() != ""
                    else None
                )

        elif isinstance(self._inner_widget, CustomListWidget):
            self._inner_widget: CustomListWidget

            return (
                self._inner_widget.get_data()
                if self._inner_widget.get_data() != ""
                else None
            )

        else:
            return f"Soon ... {str(type(self._inner_widget))}"
