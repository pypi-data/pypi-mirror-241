import logging
import os

from PySide2 import QtWidgets, QtCore, QtUiTools
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QPushButton, QComboBox, QDateTimeEdit

from famegui.config.runtime_consts import UPDATED_CONTRACT_KEY, OLD_CONTRACT_KEY
from famegui.maincontroller import MainController
from famegui.models import Contract, Scenario, Agent
from famegui.ui.fame_input_panels import (
    get_string_chooser_panel,
    FameCalendarInputPanelWidget,
)
from famegui.ui.fame_ui_elements import QFameBoldLabel
from famegui.ui.quick_modals import gen_quick_warning_modal
from famegui.utils import contract_fields_to_natural_types

DISPLAY_DATE_FORMAT = "yyyy-MM-dd"

DISPLAY_DATETIME_FORMAT = "yyyy-MM-dd HH:mm:ss"


class EditContractDialog(QtWidgets.QDialog):
    """Dialog for editing a contract"""

    on_contract_edited = QtCore.Signal(dict)

    def __init__(
            self,
            selected_contract: Contract,
            scenario: Scenario,
            controller: MainController,
            on_contract_edited_slot,
            parent=None,
    ):
        super(EditContractDialog, self).__init__(parent)

        # Set up the user interface from Designer
        self._selected_contract = selected_contract
        self._scenario = scenario
        self._controller = controller
        self.on_contract_edited.connect(on_contract_edited_slot)

        # Load UI
        loader = QtUiTools.QUiLoader()
        file = QFile(os.path.join(os.path.dirname(__file__), "edit_contract_dialog.ui"))
        file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(file, self)

        file.close()

        self._input_fields = []
        self.ui.verticalLayout: QtWidgets.QVBoxLayout

        self._init_static_ui()
        self._generate_input_items()
        self.create_btn_panel()

        self.ui.exec_()

    def setup_text_content(self):
        """Set up the headline content of the dialog"""
        title = QLabel(
            f"Edit Contract"
            f"\nProduct Name: {self._selected_contract.product_name}"
            f"\nSender Id: {self._selected_contract.sender_id}"
            f"\nReceiver Id: {self._selected_contract.receiver_id}",
            self,
        )

        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.ui.verticalLayout.addWidget(title)

        description = QLabel("Leave blank if no value is required", self)
        description.setWordWrap(True)

        self.ui.verticalLayout.addWidget(description)

    def setup_layout(self):
        """Set up the layout frame of the dialog"""
        self.ui.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.ui.verticalLayout.setSpacing(20)

    def _init_static_ui(self):
        """Set up the static UI elements of the dialog"""
        self.setup_layout()
        self.setup_text_content()

    def _construct_product_chooser(self, layout, field_name):
        """construct product chooser widget"""
        sender_type = self._scenario.schema.agent_type_from_name(
            self._controller.get_agent_ctrl(self._selected_contract.sender_id).type_name
        )

        sender_type_products = sender_type.products
        (
            inner_layout,
            comboBox,
        ) = get_string_chooser_panel(sender_type_products, Contract._KEY_PRODUCT)

        layout.addLayout(inner_layout)
        self._input_fields.append((field_name, comboBox))

    def _construct_date_time_chooser(self, layout, field_name, contract_data):
        """construct product time chooser widget"""

        saved_fame_datetime = None
        if field_name in contract_data:
            saved_fame_datetime = contract_data[field_name]

        fame_calender_input_panel = FameCalendarInputPanelWidget(
            self, field_name, saved_fame_datetime
        )
        (
            inner_layout,
            date_time_edit,
        ) = fame_calender_input_panel.get_input_related_widgets()
        layout.addWidget(fame_calender_input_panel)

        self._input_fields.append((field_name, date_time_edit))

    def _construct_default_input_field(self, layout, field_name, contract_data):
        """construct default input field"""
        label = QFameBoldLabel(text=field_name)
        label.setMinimumWidth(int(self.width() * 0.3))  # Set the maximum width to 30% of the dialog's width
        label.setMaximumWidth(int(self.width() * 0.3))  # Set the maximum width to 30% of the dialog's width
        label.setWordWrap(True)  # Enable word wrap

        input_field = QLineEdit()

        if field_name in contract_data:
            input_field.setText(str(contract_data[field_name]))

        inner_layout = QHBoxLayout()
        inner_layout.addWidget(label)
        inner_layout.addWidget(input_field)

        layout.addLayout(inner_layout)
        self._input_fields.append((field_name, input_field))

    def _generate_input_items(self):
        """Entry point for generating input items"""

        layout = self.ui.verticalLayout
        contract_data = self._selected_contract.to_dict()

        # Create input rows dynamically based on the item list
        for field_name in self._selected_contract.get_fields_to_edit():
            if field_name == Contract._KEY_PRODUCT:
                self._construct_product_chooser(layout, field_name)

                continue

            field_type = self._selected_contract.get_field_type(field_name)

            if field_type == self._selected_contract.FIELD_TYPE_DATE_TIME:
                self._construct_date_time_chooser(layout, field_name, contract_data)

                continue
            self._construct_default_input_field(layout, field_name, contract_data)

        layout.addStretch()

    def create_btn_panel(self):
        """Construct the button panel"""
        cancel_button = QPushButton("Cancel", self)
        confirm_button = QPushButton("Confirm", self)
        cancel_button.clicked.connect(self.cancel)
        confirm_button.clicked.connect(self.confirm)

        # Create a QHBoxLayout for the buttons
        button_layout = QHBoxLayout()

        # Add the buttons to the button layout
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(confirm_button)

        self.ui.verticalLayout.addLayout(button_layout)

    def init_ui(self):
        input = QLineEdit(self)
        self.ui.verticalLayout.addWidget(input)

    def cancel(self):
        """Cancel the applied changes and close the dialog"""
        self.ui.close()

    def _check_if_agent_exists(self, agent_id) -> bool:

        if not self._scenario.agent_exists(agent_id):
            gen_quick_warning_modal(
                self, "Agent does not exist", "Agent with id " + str(agent_id) + " does not exist"
            )
            return False

        return True

    def _check_for_product_support(self, agent: Agent) -> bool:

        if not self._scenario.schema.agent_supports_product(
                self._scenario.schema.agent_types[agent.type_name], self._selected_contract.product_name
        ):
            message = f"Agent with id '{str(agent.id)}' does not support the product: {self._selected_contract.product_name}"
            gen_quick_warning_modal(self, "Sender does not support product", message)
            return False
        return True

    def confirm(self):
        """Confirm the applied changes and close the dialog"""
        data_dict = {}

        for field_name, input_field in self._input_fields:
            if isinstance(input_field, QLineEdit):
                input_field: QLineEdit
                data_dict[field_name] = input_field.text()

                try:
                    input_data = int(input_field.text())
                except Exception as exce:
                    logging.debug(F"OPTIONAL FIELD NOT SET {str(exce)}")
                    continue

                if field_name == Contract._KEY_SENDER or field_name == Contract._KEY_SENDER:
                    if not self._scenario.agent_exists(input_data):
                        if not self._check_if_agent_exists(input_data):
                            return

                    agent: Agent = self._scenario.get_agent_by_id(input_data)

                    if not self._check_for_product_support(agent):
                        return

            if isinstance(input_field, QDateTimeEdit):
                input_field: QDateTimeEdit
                data_dict[field_name] = input_field.dateTime().toString(DISPLAY_DATETIME_FORMAT)
            if isinstance(input_field, QComboBox):
                input_field: QComboBox
                data_dict[field_name] = input_field.currentText()

        old_agent_dict = self._selected_contract.to_dict()

        dict_to_send = {
            OLD_CONTRACT_KEY: old_agent_dict.copy(),
        }

        for key, value in data_dict.items():
            old_agent_dict[key] = value
        old_agent_dict = contract_fields_to_natural_types(
            old_agent_dict, self._selected_contract
        )
        updated_contract = Contract.from_dict(old_agent_dict)

        dict_to_send[UPDATED_CONTRACT_KEY] = updated_contract.to_dict()

        self._scenario.update_contract(
            old_contract=self._selected_contract, updated_contract=updated_contract
        )
        self._controller.set_unsaved_changes(True)
        self.on_contract_edited.emit(dict_to_send)
        self.ui.accept()

    @staticmethod
    def select_date(date, line_edit):
        selected_date = date.toString(DISPLAY_DATE_FORMAT)
        line_edit.setText(selected_date)
