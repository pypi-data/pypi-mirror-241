import os

from PySide2.QtGui import QIntValidator, QFont
from typing import Tuple, List

from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QDateTime
from PySide2.QtWidgets import (
    QHBoxLayout,
    QDateTimeEdit,
    QComboBox,
    QLineEdit,
    QWidget,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QStyle,
    QTextEdit,
)

from famegui.appworkingdir import AppWorkingDir
from famegui.config.style_config import DEFAULT_INPUT_STYLE, FAME_CALENDAR_INPUT_STYLE, FAME_LINE_EDIT_STYLE_DEFAULT, \
    FAME_LINE_EDIT_STYLE_ERR_STATE, ERROR_TEXT_STYLE_LINE_EDIT
from famegui.time_utils import convert_fame_time_to_gui_datetime, convert_gui_datetime_to_fame_time, WIDGET_DATE_FORMAT
from famegui.ui.fame_ui_elements import QFameBoldLabel


class FileChooserWidgetPanel(QtWidgets.QWidget):
    """ "Class based panel to choose a file from the file system or to enter a float value"""

    current_value_changed = QtCore.Signal(str)

    def __init__(
            self,
            working_dir: AppWorkingDir,
            field_name: str = None,
            default_value: str = None,
            parent: QtWidgets.QWidget = None,
    ) -> None:
        super().__init__(parent)

        self._working_dir = working_dir
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setMargin(0)
        self.layout.setSpacing(0)

        self.validation_state = True

        self.default_value = default_value

        self.field_name = field_name

        self._line_edit = QTextEdit(self)

        self._line_edit: QTextEdit
        self._line_edit.setStyleSheet(FAME_CALENDAR_INPUT_STYLE)

        self._line_edit.setWordWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)

        self._line_edit.setFixedHeight(50)
        self._line_edit.setFont(QFont("Arial", 12))

        self._line_edit.setPlaceholderText(
            self.tr(
                "Please enter file path, drop in a file or type in a single float value"
            )
        )

        uniq_widget_id = str(id(self._line_edit))

        self._line_edit.setObjectName(uniq_widget_id)

        self._line_edit.setStyleSheet(
            FAME_LINE_EDIT_STYLE_DEFAULT
        )
        self._line_edit.setContentsMargins(0, 0, 0, 0)

        self._line_edit.textChanged.connect(self._on_text_edit_changed)

        self._line_edit.setStyleSheet(DEFAULT_INPUT_STYLE)

        if self.field_name:
            label = QtWidgets.QLabel(self)
            label.setFont(QFont("Arial", 8))
            label.setText(self.field_name)
            self.layout.addWidget(label)

        if self.default_value:
            self._line_edit.setText(str(self.default_value))

        self.layout.addWidget(self._line_edit)
        # button (to open dialog box)
        button = QtWidgets.QPushButton("...", self)
        button.setToolTip(self.tr("Select file..."))
        button.setFixedWidth(button.fontMetrics().width(button.text()) + 60)
        self.layout.addWidget(button)
        # connect
        button.clicked.connect(self._on_button_clicked)

        self._drop_icon_label = QtWidgets.QLabel(self)

        self.layout.addWidget(self._drop_icon_label)
        self._drop_icon_label.hide()

        self.setAcceptDrops(True)

    def set_validation_state(self, is_valid):
        """Set the validation state of the input panel after a validation check has been performed"""
        self.validation_state = is_valid

        if is_valid:
            self._line_edit.setStyleSheet(DEFAULT_INPUT_STYLE)
            return
        self._line_edit.setStyleSheet(
            FAME_LINE_EDIT_STYLE_ERR_STATE

        )

    def get_path(self) -> str:
        """Return the path of the selected file from a file chooser widget"""

        return self._line_edit.toPlainText()

    def get_input_related_widgets(self):
        return self.layout, self._line_edit

    def _set_drop_zone_style(self, is_dragging: bool) -> None:
        # Change the styling based on whether a drag event is occurring
        if is_dragging:
            style_sheet = "FileChooserWidget { border: 2px dashed #888888; }"
            self._drop_icon_label.show()
        else:
            style_sheet = ""
            self._drop_icon_label.hide()
        self.setStyleSheet(style_sheet)

    def dragLeaveEvent(self, event) -> None:
        self._set_drop_zone_style(False)

    def dropEvent(self, event) -> None:
        file_path = event.mimeData().urls()[0].toLocalFile()  # Extract the file path from the dropped item

        if os.path.isfile(file_path):
            file_path = self._working_dir.make_relative_path(file_path)
            self._line_edit.setText(file_path)
        self._set_drop_zone_style(False)

    def dragEnterEvent(self, event) -> None:
        # Check if the dragged item is a file
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event) -> None:
        # Accept drag movement
        event.accept()

    def _on_button_clicked(self) -> None:
        open_location = self._working_dir.timeseries_dir
        if self._line_edit.toPlainText() != "":
            full_edit_path = self._working_dir.make_full_path(
                self._line_edit.toPlainText()
            )
            if os.path.isfile(full_edit_path):
                open_location = full_edit_path

        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            self.tr("Open time series file"),
            open_location,
            self.tr("Time series (*.csv);;All files (*.*)"),
        )
        if file_path != "":
            file_path = self._working_dir.make_relative_path(file_path)
            self._line_edit.setText(file_path)

    def _on_text_edit_changed(self) -> None:
        self.current_value_changed.emit(self._line_edit.toPlainText())

    def display_error(self, has_error: bool) -> None:
        style_sheet = ERROR_TEXT_STYLE_LINE_EDIT if has_error else ""
        self._line_edit.setStyleSheet(style_sheet)


class FameCalendarInputPanelWidget(QWidget):
    """Class based panels require to call the get_input_related_widgets() method
    -> get the layout and the input widget
    The input is to access the input widget
    Return a tuple of the layout and the calender input widget
    Can be stacked easily into nested and complex layouts
    Class based panels have usually a richer functionality and some intern event based logic
    """

    WIDGET_DATE_FORMAT = "dd/MM/yyyy hh:mm:ss"

    def __init__(
            self, parent: QtWidgets.QWidget, label: str, current_fame_time: int = None
    ) -> None:
        super().__init__(parent)
        self._label = label
        self._current_fame_time = current_fame_time

        self._inner_layout = QHBoxLayout(self)
        self._inner_layout.setContentsMargins(0, 0, 0, 0)
        self._inner_layout.setSpacing(0)

        self._line_edit = QLineEdit()
        self._line_edit.setValidator(QIntValidator())

        line_edit_layout = QVBoxLayout()
        line_edit_layout.setContentsMargins(10, 10, 10, 10)
        line_edit_layout.addStretch(1)  # push labels and input fields to bottom

        line_edit_heading = QLabel("Fame Time:")  # heading label for QLineEdit
        font = QFont()
        font.setBold(True)
        line_edit_heading.setFont(font)

        line_edit_layout.addWidget(line_edit_heading)
        line_edit_layout.addWidget(self._line_edit)

        self._date_time_edit = QDateTimeEdit()
        self._date_time_edit.setCalendarPopup(True)
        self._date_time_edit.setDisplayFormat(self.WIDGET_DATE_FORMAT)
        self._date_time_edit.setDateTime(QDateTime.currentDateTime())

        date_time_edit_heading = QLabel("Date Time:")  # heading label for QDateTimeEdit
        date_time_edit_heading.setFont(font)

        date_time_edit_layout = QVBoxLayout()
        date_time_edit_layout.addStretch(1)  # push labels and input fields to bottom
        date_time_edit_layout.addWidget(date_time_edit_heading)
        date_time_edit_layout.addWidget(self._date_time_edit)
        date_time_edit_layout.setContentsMargins(10, 10, 10, 10)

        if current_fame_time:
            self._line_edit.setText(str(current_fame_time))

        self._date_time_edit.setMinimumWidth(parent.width() * 0.3)

        self._inner_layout.addWidget(QFameBoldLabel(label))
        self._inner_layout.addLayout(line_edit_layout)
        self._date_time_edit.dateTimeChanged.connect(self._update_fame_times)
        self._line_edit.textChanged.connect(self._update_fame_time_text_areas)
        self._inner_layout.addLayout(date_time_edit_layout)

    def get_input_related_widgets(self) -> Tuple[QHBoxLayout, QLineEdit]:
        """Returns a tuple of the layout and the calendar QDateTimeEdit widget"""
        return self._inner_layout, self._line_edit

    def _update_fame_times(self):
        """Inner event based logic"""
        self._line_edit.setText(
            str(convert_gui_datetime_to_fame_time(self._date_time_edit.text()))
        )

    def _update_fame_time_text_areas(self):
        """Inner event based logic"""
        fame_first_delivery_time: str = self._line_edit.text()
        if fame_first_delivery_time == "" or fame_first_delivery_time == "-":
            return
        gui_start_time = convert_fame_time_to_gui_datetime(
            int(fame_first_delivery_time)
        )
        self._date_time_edit.setDateTime(gui_start_time)

        fame_expiration_time: str = self._line_edit.text()
        if fame_expiration_time == "":
            return
        gui_expiration_time_time = convert_fame_time_to_gui_datetime(
            int(fame_expiration_time)
        )
        self._date_time_edit.setDateTime(gui_expiration_time_time)


"""Function based panels"""


def get_datetime_choose_panel(
        label: str, parent=None
) -> Tuple[QHBoxLayout, QDateTimeEdit]:
    """Returns a tuple of the layout and the calender QDateTimeEdit widget
    The widget is in the layout
    Widget ref is needed to access the input more easily
    Also opens up the opportunity
    to attach event based logic to the widget,
    like the datetime change event"""

    inner_layout = QHBoxLayout()
    if parent:
        inner_layout = QHBoxLayout(parent)

    date_time_edit: QDateTimeEdit = QDateTimeEdit()
    date_time_edit.setDateTime(QDateTime.currentDateTime())
    date_time_edit.setDisplayFormat(WIDGET_DATE_FORMAT)

    inner_layout.addWidget(QFameBoldLabel(label))
    inner_layout.addWidget(date_time_edit)
    return inner_layout, date_time_edit


def get_string_chooser_panel(
        options: List[str], label: str, parent=None
) -> Tuple[QHBoxLayout, QComboBox]:
    """Classic combo box panel Returns a chooser box from a list of options"""
    inner_layout = QHBoxLayout()
    if parent:
        inner_layout = QHBoxLayout(parent)

    combo_box = QtWidgets.QComboBox()
    combo_box.addItems(options)
    inner_layout.addWidget(QFameBoldLabel(label))
    inner_layout.addWidget(combo_box)
    return inner_layout, combo_box


def get_integer_input_panel(
        label: str, input_help_text=None, parent=None
) -> Tuple[QHBoxLayout, QtWidgets.QLineEdit]:
    """Integer input panel Returns an input field only allowing integers"""

    inner_layout = QHBoxLayout()

    if parent:
        inner_layout = QHBoxLayout(parent)

    if not input_help_text:
        input_help_text = "Enter an integer"

    int_edit = QtWidgets.QLineEdit()
    int_edit.setPlaceholderText(input_help_text)
    int_validator = QIntValidator()  # Integer validator
    int_edit.setValidator(int_validator)
    inner_layout.addWidget(QFameBoldLabel(label))
    inner_layout.addWidget(int_edit)

    return inner_layout, int_edit


def get_double_input_panel(
        label: str, input_help_text=None, parent=None
) -> Tuple[QHBoxLayout, QtWidgets.QLineEdit]:
    """Double input panel Returns an input field only allowing integers"""

    if not input_help_text:
        input_help_text = "Enter an Double"

    return get_integer_input_panel(label, input_help_text)


def get_string_input_panel(
        label: str, parent=None
) -> Tuple[QHBoxLayout, QtWidgets.QLineEdit]:
    """String input panel. Returns an input field for string input."""

    inner_layout = QHBoxLayout()
    if parent:
        inner_layout = QHBoxLayout(parent)

    string_edit = QtWidgets.QLineEdit()
    inner_layout.addWidget(QFameBoldLabel(label))
    inner_layout.addWidget(string_edit)

    return inner_layout, string_edit
