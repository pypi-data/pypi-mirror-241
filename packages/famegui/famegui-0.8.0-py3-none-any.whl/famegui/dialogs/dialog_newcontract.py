from typing import List

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QLineEdit

from famegui import models
from famegui.agent_controller import AgentController
from famegui.config.static_ui_components import build_new_contract_dlg
from famegui.generated.ui_dialog_newcontract import Ui_DialogNewContract
from famegui.time_utils import (
    convert_fame_time_to_gui_datetime,
    convert_gui_datetime_to_fame_time,
)
from famegui.ui.quick_modals import gen_quick_warning_modal


class DialogNewContract(QDialog):
    """Dialog for creating a single contract"""

    fame_to_datetime_conversion_triggered: bool = False
    WIDGET_DATE_FORMAT = "dd/MM/yyyy hh:mm:ss"

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

    def __init__(
        self,
        sender: AgentController,
        receiver: AgentController,
        schema: models.Schema,
        parent=None,
    ):
        QDialog.__init__(self, parent)
        self._ui = Ui_DialogNewContract()
        self._ui.setupUi(self)
        self._sender = sender
        self._receiver = receiver

        self.setWindowTitle(self.tr("New contract"))
        self._ui.labelDescr.setText(
            self.tr(
                self.tr(
                    self.tr(build_new_contract_dlg(self._sender, self._receiver))
                )

            ))

        # force the user to select a product except if only one is available
        if self._ui.comboBoxProduct.count() != 1:
            self._ui.comboBoxProduct.setCurrentIndex(-1)

        self._ui.comboBoxProduct.currentIndexChanged.connect(self._update_ok_button_status)
        self._update_ok_button_status()

        self._prep_input_line_edits()

        # fill possible products to select based on the sender schema agent type
        sender_type = schema.agent_type_from_name(sender.type_name)
        assert sender_type is not None
        self._ui.comboBoxProduct.addItems(list(set(sender_type.products)))

        # force the user to select a product except if only one is available
        if self._ui.comboBoxProduct.count() != 1:
            self._ui.comboBoxProduct.setCurrentIndex(-1)

        # connect
        self._ui.comboBoxProduct.currentIndexChanged.connect(
            self._update_ok_button_status
        )
        self._update_ok_button_status()

        self._ui.lineFirstDeliveryTime.textChanged.connect(
            self._update_fame_time_text_areas
        )
        self._ui.lineExpirationTime.textChanged.connect(
            self._update_fame_time_text_areas
        )  #

    def _prep_date_time_fields(self):
        """configure date time fields to use the correct format and to trigger the update of the fame time fields"""
        self._ui.lineFirstDeliveryNonFameTime.setCalendarPopup(True)
        self._ui.lineFirstDeliveryNonFameTime.setDisplayFormat(self.WIDGET_DATE_FORMAT)
        self._ui.lineFirstDeliveryNonFameTime.dateTimeChanged.connect(
            self._update_fame_times
        )

        self._ui.lineExpirationTimeNonFameTime.setCalendarPopup(True)
        self._ui.lineExpirationTimeNonFameTime.setDisplayFormat(self.WIDGET_DATE_FORMAT)
        self._ui.lineExpirationTimeNonFameTime.dateTimeChanged.connect(
            self._update_fame_times
        )

    def _prep_input_line_edits(self):
        """accept uint64 numbers as specified in protobuf schema"""
        self._configure_line_edit_for_unsigned_int(self._ui.lineDeliveryInterval)
        self._configure_line_edit_for_signed_int(self._ui.lineFirstDeliveryTime)
        self._configure_line_edit_for_optional_signed_int(self._ui.lineExpirationTime)

    def make_new_contract(self) -> models.Contract:
        expiration_time_str = self._ui.lineExpirationTime.text()
        expiration_time = int(expiration_time_str) if expiration_time_str else None

        return models.Contract(
            self._sender.id,
            self._receiver.id,
            self._ui.comboBoxProduct.currentText(),
            int(self._ui.lineDeliveryInterval.text()),
            int(self._ui.lineFirstDeliveryTime.text()),
            expiration_time,
        )

    def _update_fame_time_text_areas(self):
        self.fame_to_datetime_conversion_triggered = True

        fame_first_delivery_time: str = self._ui.lineFirstDeliveryTime.text()
        if fame_first_delivery_time == "":
            return
        gui_start_time = convert_fame_time_to_gui_datetime(
            int(fame_first_delivery_time)
        )
        self._ui.lineFirstDeliveryNonFameTime.setDateTime(gui_start_time)

        fame_expiration_time: str = self._ui.lineExpirationTime.text()
        if fame_expiration_time == "":
            return

        gui_expiration_time_time = convert_fame_time_to_gui_datetime(
            int(fame_expiration_time)
        )
        self._ui.lineExpirationTimeNonFameTime.setDateTime(gui_expiration_time_time)

    def _update_fame_times(self):
        if self.fame_to_datetime_conversion_triggered:
            self.fame_to_datetime_conversion_triggered = False
            return
        self._ui.lineExpirationTime.setText(
            str(
                convert_gui_datetime_to_fame_time(
                    self._ui.lineExpirationTimeNonFameTime.text()
                )
            )
        )
        self._ui.lineFirstDeliveryTime.setText(
            str(
                convert_gui_datetime_to_fame_time(
                    self._ui.lineFirstDeliveryNonFameTime.text()
                )
            )
        )

    def _update_ok_button_status(self):
        all_fields_ok = (
            self._ui.comboBoxProduct.currentText() != ""
            and self._ui.lineDeliveryInterval.text() != ""
            and self._ui.lineFirstDeliveryTime.text() != ""
        )
        self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(all_fields_ok)


