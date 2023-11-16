import copy

from PySide2.QtWidgets import QDialog, QDialogButtonBox, QFileDialog
from PySide2 import QtGui
from famegui.time_utils import (
    convert_gui_datetime_to_fame_time,
    convert_fame_time_to_gui_datetime,
)
from fameio.source.time import ConversionException


from famegui import models
from famegui.appworkingdir import AppWorkingDir
from famegui.generated.ui_dialog_scenario_properties import Ui_DialogScenarioProperties


class DialogScenarioProperties(QDialog):
    fame_to_datetime_conversion_triggered: bool = False

    def __init__(
        self, props: models.GeneralProperties, workdir: AppWorkingDir, parent=None
    ):
        QDialog.__init__(self, parent)
        self._ui = Ui_DialogScenarioProperties()
        self._ui.setupUi(self)
        self._workdir = workdir
        self.hide_outputfile_selection()
        self.hide_schema_selection()

        # make sure to always have the required fields initialized
        self._props = copy.deepcopy(props)
        #        self._props.init_missing_values()

        # default button
        self._ui.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)

        # simulation params
        self._ui.lineEditStartTime.setDateTime(
            convert_fame_time_to_gui_datetime(self._props.simulation_start_time)
        )

        self._ui.lineEditStartTime.setDisplayFormat("dd/MM/yyyy hh:mm:ss")
        self._ui.lineEditStopTime.setDisplayFormat("dd/MM/yyyy hh:mm:ss")

        self._ui.lineEditStartTime.setCalendarPopup(True)
        self._ui.lineEditStopTime.setCalendarPopup(True)

        self._ui.lineEditStopTime.setDateTime(
            convert_fame_time_to_gui_datetime(self._props.simulation_stop_time)
        )
        self._ui.lineEditRandomSeed.setValidator(QtGui.QIntValidator())  # int64
        self._ui.lineEditRandomSeed.setText(str(self._props.simulation_random_seed))

        # output params
        self._ui.spinBoxInterval.setRange(0, 2_147_483_647)  # int32
        self._ui.spinBoxInterval.setValue(self._props.output_interval)
        self._ui.spinBoxProcess.setRange(0, 2_147_483_647)  # int32
        self._ui.spinBoxProcess.setValue(self._props.output_process)

        # protobuf output file
        self._ui.buttonOutputPath.clicked.connect(self._on_select_output_path)

        # button status update
        self._connect_slots()
        self._update_ok_button_status()

    def _connect_slots(self):
        self._ui.lineEditStartTime.dateTimeChanged.connect(
            self._update_ok_button_status
        )
        self._ui.lineEditStopTime.dateTimeChanged.connect(self._update_ok_button_status)
        self._ui.fame_start_time.textChanged.connect(self._update_date_time_text_areas)
        self._ui.fame_stop_time.textChanged.connect(self._update_date_time_text_areas)

        self._ui.lineEditRandomSeed.textChanged.connect(self._update_ok_button_status)
        self._ui.lineEditOutputPath.textChanged.connect(self._update_ok_button_status)

    def hide_outputfile_selection(self):
        self._ui.groupBoxOutputFile.setEnabled(False)
        self._ui.groupBoxOutputFile.setVisible(False)
        self.adjustSize()

    def enable_outputfile_selection(self, default_path: str):
        self._ui.groupBoxOutputFile.setEnabled(True)
        self._ui.groupBoxOutputFile.setVisible(True)
        self._ui.lineEditOutputPath.setText(default_path)
        self.adjustSize()

    def hide_schema_selection(self):
        self._ui.groupBoxSchema.setEnabled(False)
        self._ui.groupBoxSchema.setVisible(False)
        self.adjustSize()

    def enable_schema_selection(self):
        self._ui.groupBoxSchema.setEnabled(True)
        self._ui.groupBoxSchema.setVisible(True)
        self._ui.comboBoxSchema.clear()
        self._ui.comboBoxSchema.addItems(self._workdir.list_existing_schema_files())
        self.adjustSize()

    def _on_select_output_path(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.tr("Protobuf output file"),
            self._workdir.protobuf_dir,
            self.tr("Protobuf (*.pb)"),
        )
        if file_path != "":
            self._ui.lineEditOutputPath.setText(file_path)

    def make_properties(self) -> models.GeneralProperties:
        # simulation
        datetime_string_start_time = self._ui.lineEditStartTime.text()
        datetime_string_stop_time = self._ui.lineEditStopTime.text()

        self._props.set_simulation_start_time(
            convert_gui_datetime_to_fame_time(datetime_string_start_time)
        )

        self._props.set_simulation_stop_time(
            convert_gui_datetime_to_fame_time(datetime_string_stop_time)
        )
        self._props.set_simulation_random_seed(int(self._ui.lineEditRandomSeed.text()))
        # output
        self._props.set_output_interval(self._ui.spinBoxInterval.value())
        self._props.set_output_process(self._ui.spinBoxProcess.value())
        return self._props

    def get_output_file_path(self):
        assert self._ui.lineEditOutputPath.text() != ""
        return self._ui.lineEditOutputPath.text()

    def get_selected_schema_full_path(self) -> str:
        assert self._ui.comboBoxSchema.count() > 0
        selected_path = self._ui.comboBoxSchema.currentText()
        return self._workdir.make_full_path(selected_path)

    def _check_all_fields_are_valid(self):
        if (
            self._ui.lineEditStartTime.text() == ""
            or self._ui.lineEditStopTime.text() == ""
            or self._ui.lineEditRandomSeed.text() == ""
        ):
            return False
        if (
            self._ui.lineEditOutputPath.isVisible()
            and self._ui.lineEditOutputPath.text() == ""
        ):
            return False
        return True

    def _update_date_time_text_areas(self):
        self.fame_to_datetime_conversion_triggered = True
        fame_stop_time: str = self._ui.fame_stop_time.text()
        if fame_stop_time == "":
            return

        gui_stop_time = convert_fame_time_to_gui_datetime(int(fame_stop_time))
        self._ui.lineEditStopTime.setDateTime(gui_stop_time)
        fame_start_time: str = self._ui.fame_start_time.text()
        if fame_start_time == "":
            return
        gui_start_time = convert_fame_time_to_gui_datetime(int(fame_start_time))
        self._ui.lineEditStartTime.setDateTime(gui_start_time)

    def _update_fame_time_text_areas(self):
        if self.fame_to_datetime_conversion_triggered:
            self.fame_to_datetime_conversion_triggered = False
            return
        self._ui.fame_stop_time.setStyleSheet("QLabel {color: black}")
        self._ui.fame_start_time.setStyleSheet("QLabel {color: black}")

        try:
            fame_start_time = convert_gui_datetime_to_fame_time(
                self._ui.lineEditStartTime.text()
            )
            self._ui.fame_start_time.setText(str(fame_start_time))

        except ConversionException as c_ex:

            self._ui.fame_start_time.setText(str(c_ex))
            self._ui.fame_start_time.setStyleSheet("QLabel {color: red}")


        try:
            fame_stop_time = convert_gui_datetime_to_fame_time(
                self._ui.lineEditStopTime.text()
            )
            self._ui.fame_stop_time.setText(str(fame_stop_time))

        except ConversionException as c_ex:
            self._ui.fame_stop_time.setText(str(c_ex))
            self._ui.fame_stop_time.setStyleSheet("QLabel {color: red}")

    def _update_ok_button_status(self):
        self._update_fame_time_text_areas()
        self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            self._check_all_fields_are_valid()
        )
