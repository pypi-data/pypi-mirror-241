import logging
from datetime import datetime

from PySide2.QtCore import QTimer
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QFormLayout, QScrollArea, QLabel, QSizePolicy

from famegui.config.style_config import FAME_CONSOLE_STYLE
from famegui.time_utils import WIDGET_DATE_FORMAT_CONSOLE


class GUIConsoleHandler(logging.StreamHandler):
    """A custom logging handler that writes to a QScrollArea to display the log messages in the GUI"""

    def __init__(self, form_layout: QFormLayout, scroll_area: QScrollArea):
        logging.StreamHandler.__init__(self)
        super().__init__()
        self._form_layout = form_layout
        self._scroll_area = scroll_area
        self._labels = []

    def emit(self, record):
        """On new log message, add a new row to the form layout and scroll to the bottom"""
        msg = self.format(record)
        current_time = datetime.now().strftime(WIDGET_DATE_FORMAT_CONSOLE)

        label_widget = QLabel(f"{current_time}: {record.levelname}: {msg}")
        label_widget.setWordWrap(True)
        label_widget.setStyleSheet(FAME_CONSOLE_STYLE)
        label_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        font = QFont()
        font.setPointSize(10)
        label_widget.setFont(font)

        if len(self._labels) >= 150:
            # remove the oldest row if max amount reached
            old_label = self._labels.pop(0)
            self._form_layout.removeRow(old_label)

        self._form_layout.addRow(label_widget)
        self._labels.append(label_widget)  # keep a reference to the label

        self._scroll_area.update()
        self._form_layout.update()
        self._form_layout.activate()

        QTimer.singleShot(100, self.scroll_to_bottom)

    def scroll_to_bottom(self):
        """Scroll to the bottom of the scroll area"""
        scroll_bar = self._scroll_area.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())
