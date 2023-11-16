from typing import List

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QLineEdit, QDialog
from famegui import models

from famegui.agent_controller import AgentController
from famegui.dialogs.dialog_newcontract import DialogNewContract
from famegui.generated.ui_dialog_newcontract import Ui_DialogNewContract
from famegui.ui.quick_modals import gen_quick_warning_modal


class DialogNewMultiContract(DialogNewContract):
    """Dialog for creating a multi contract"""
    fame_to_datetime_conversion_triggered: bool = False

    def _configure_line_edit_for_unsigned_int(self, line_edit: QLineEdit):
        line_edit.setText("0")
        regex_uint64 = QtCore.QRegExp("\\d{1,20}")
        line_edit.setValidator(QtGui.QRegExpValidator(regex_uint64))
        line_edit.textChanged.connect(self._update_ok_button_status)

    def _configure_line_edit_for_signed_int(self, line_edit: QLineEdit):
        line_edit.setText("0")
        regex_uint64 = QtCore.QRegExp("-?\\d{1,20}")
        line_edit.setValidator(QtGui.QRegExpValidator(regex_uint64))
        line_edit.textChanged.connect(self._update_ok_button_status)

    def _configure_line_edit_for_optional_signed_int(self, line_edit: QLineEdit):
        line_edit.setText("")
        line_edit.setPlaceholderText(self.tr("optional"))
        regex_uint64 = QtCore.QRegExp("-?\\d{0,20}")
        line_edit.setValidator(QtGui.QRegExpValidator(regex_uint64))

    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    def format_list_item_sender(self, display_id, agent_type_name):
        return f"<li>Sender: agent <b>{display_id}</b> of type <b>{agent_type_name}</b></li> \n"

    def format_list_item_receiver(self, display_id, agent_type_name):
        return f"<li>Receiver: agent <b>{display_id}</b> of type <b>{agent_type_name}</b></li> \n"

    def _is_not_valid_contract_relation(self) -> bool:
        return len(self._sender) > 1 and len(self._receiver) != len(self._sender)

    def __init__(
            self,
            sender: [],
            receiver: [],
            schema: models.Schema,
            parent=None,
    ):
        QDialog.__init__(self, parent)
        self._ui = Ui_DialogNewContract()
        self._ui.setupUi(self)
        self._sender: [AgentController] = sender
        self._receiver: [AgentController] = receiver
        self._schema: models.Schema = schema

        self.setWindowTitle(self.tr("New contract"))
        sender_items = " ".join([self.format_list_item_sender(x.display_id, x.type_name) for x in self._sender])
        receiver_items = " ".join([self.format_list_item_receiver(x.display_id, x.type_name) for x in self._receiver])

        list_inner = sender_items + receiver_items

        self._ui.labelDescr.setText(
            self.tr(
                "<html><head/><body>"
                "<p>Create new contract between multiple Agents :</p>"
                f"<ul>{list_inner}"
                "</body></html>"
            )
        )

        # fill possible products to select based on the sender schema agent type


        if self._is_not_valid_contract_relation():
            gen_quick_warning_modal(
                self,
                "Validation failure",
                "The selected agents are not corresponding a one to many or  one to one schema \n\n",

            )

            QTimer.singleShot(0, self.close)  # delay close to avoid the dialog to be shown

            return

        final_sender_product_names = self._schema.get_all_products_for_type(self._sender[0].type_name)

        self._ui.comboBoxProduct.addItems(list(set(final_sender_product_names)))

        # force the user to select a product except if only one is available
        if self._ui.comboBoxProduct.count() != 1:
            self._ui.comboBoxProduct.setCurrentIndex(-1)

        self._ui.comboBoxProduct.currentIndexChanged.connect(self._update_ok_button_status)
        self._update_ok_button_status()

        self._prep_input_line_edits()

        self._prep_date_time_fields()

        # fill possible products to select based on the sender schema agent type

        # force the user to select a product except if only one is available
        if self._ui.comboBoxProduct.count() != 1:
            self._ui.comboBoxProduct.setCurrentIndex(-1)

        # connect
        self._connect_slots()

    def _connect_slots(self):
        '''connect event listeners'''
        self._ui.comboBoxProduct.currentIndexChanged.connect(self._update_ok_button_status)
        self._update_ok_button_status()
        self._ui.lineFirstDeliveryTime.textChanged.connect(self._update_fame_time_text_areas)
        self._ui.lineExpirationTime.textChanged.connect(self._update_fame_time_text_areas)

    def _prep_date_time_fields(self):
        '''configure date time fields'''
        self._ui.lineFirstDeliveryNonFameTime.setCalendarPopup(True)
        self._ui.lineFirstDeliveryNonFameTime.setDisplayFormat(self.WIDGET_DATE_FORMAT)
        self._ui.lineFirstDeliveryNonFameTime.dateTimeChanged.connect(self._update_fame_times)

        self._ui.lineExpirationTimeNonFameTime.setCalendarPopup(True)
        self._ui.lineExpirationTimeNonFameTime.setDisplayFormat(self.WIDGET_DATE_FORMAT)
        self._ui.lineExpirationTimeNonFameTime.dateTimeChanged.connect(self._update_fame_times)

    def _prep_input_line_edits(self):
        '''accept uint64 numbers as specified in protobuf schema'''
        self._configure_line_edit_for_unsigned_int(self._ui.lineDeliveryInterval)
        self._configure_line_edit_for_signed_int(self._ui.lineFirstDeliveryTime)
        self._configure_line_edit_for_optional_signed_int(self._ui.lineExpirationTime)

    def _gen_one_to_many_contract_relationship(self, sender, expiration_time) -> List[models.Contract]:

        return [
            models.Contract(
                sender.id,
                recv.id,
                self._ui.comboBoxProduct.currentText(),
                int(self._ui.lineDeliveryInterval.text()),
                int(self._ui.lineFirstDeliveryTime.text()),
                expiration_time,
            )
            for recv in self._receiver
        ]

    def _gen_one_to_one_contract_relationship(self, expiration_time) -> List[models.Contract]:

        return [
            models.Contract(
                sndr.id,
                rec.id,
                self._ui.comboBoxProduct.currentText(),
                int(self._ui.lineDeliveryInterval.text()),
                int(self._ui.lineFirstDeliveryTime.text()),
                expiration_time,
            )
            for rec, sndr in zip(self._receiver, self._sender)
        ]

    def make_new_contracts(self) -> List[models.Contract]:
        expiration_time_str = self._ui.lineExpirationTime.text()
        expiration_time = int(expiration_time_str) if expiration_time_str else None

        if len(self._sender) == 1 and len(self._receiver) > 1:
            # One to many Contract Relationship
            sender = self._sender[0]

            return self._gen_one_to_many_contract_relationship(sender, expiration_time)

        if len(self._sender) == len(self._receiver):
            # One to One Contract Relationship

            return self._gen_one_to_one_contract_relationship(expiration_time)
        # Not valid

        gen_quick_warning_modal(
            self,
            "Validation failure",
            "The selected agents are not corresponding a one to many or a one to one schema \n\n",
        )

        return None
