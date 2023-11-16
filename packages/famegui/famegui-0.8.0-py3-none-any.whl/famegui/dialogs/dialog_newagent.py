import os

import fameio.source.scenario as fameio
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QSize, Qt, QEvent, QObject
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QPushButton

from famegui import models
from famegui.appworkingdir import AppWorkingDir
from famegui.ui.attribute_row_item import AttributeTreeItem

import fameio.source.schema as schema

from famegui.ui.quick_modals import gen_quick_warning_modal


class DialogNewAgent(QtWidgets.QDialog):
    accepted = QtCore.Signal()
    trigger_input_validation = QtCore.Signal()
    validation_error_signal = QtCore.Signal(bool, str)

    def __init__(
        self,
        schema: models.Schema,
        working_dir: AppWorkingDir,
        scenario: models.Scenario,
        parent=None,
    ):
        super().__init__()

        loader = QUiLoader()
        file = QtCore.QFile(
            os.path.join(os.path.dirname(__file__), "dialog_newagent.ui")
        )

        file.open(QtCore.QFile.ReadOnly)

        self._ui = loader.load(file, self)
        self._ui.setParent(None)
        self.scenario: models.Scenario = scenario

        file.close()

        self._schema = schema
        self._working_dir = working_dir
        self._tree_items = []

        self.validation_data = []

        self.setup_ui()
        self.connect_slots()

        # connect slots

    def setup_ui(self):
        self.fired_once = False
        self.saved_data = None

        # init
        self.setWindowTitle(self.tr("New agent"))
        self._ui.comboBoxType.addItems(self._schema.agent_types.keys())

        self._ui.setWindowFlags(
            Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint
        )

        # tree view
        self._ui.treeWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self._ui.treeWidget.setRootIsDecorated(False)
        self._ui.treeWidget.setColumnCount(2)
        self._ui.treeWidget.setHeaderLabels([self.tr("Attribute"), self.tr("Value")])
        self._ui.treeWidget.setColumnWidth(0, 200)
        self._ui.treeWidget.setAlternatingRowColors(True)
        self._reset_attributes()

        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        flags = self.windowFlags()
        flags |= Qt.CustomizeWindowHint
        flags |= Qt.WindowTitleHint
        flags |= Qt.WindowSystemMenuHint
        flags |= Qt.WindowCloseButtonHint
        flags |= Qt.WindowStaysOnTopHint
        flags |= Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

    def connect_slots(self):
        """Used to handle user input and to prevent default behavior of the dialog"""
        self._ui.buttonBox.accepted.disconnect()

        self._ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.on_ok_clicked)

        self._ui.comboBoxType.currentTextChanged.connect(self._reset_attributes)
        self.validation_error_signal.connect(self.on_err_validation)

    def on_err_validation(self, is_valid, attr_name):
        """Receive validation error signal from  a panel item and append to validation data to be checked later"""
        self.validation_data.append({"is_valid": is_valid, "msg": attr_name})

    def recursive_dict_iter(self):
        """Iterate over nested attributes in a dict"""
        for key, value in self.items():
            if isinstance(value, dict):
                yield from self.recursive_dict_iter(value)
            else:
                yield key, value

    def merge_data(self, data):
        """Merge nested attributes in a dict"""
        merged_list = []

        for item in data:
            for key, value in item.items():
                if isinstance(value, list):
                    merged_dict = {}
                    for sub_item in value:
                        merged_dict.update(sub_item)
                    merged_list.append(merged_dict)
                elif isinstance(value, dict):
                    merged_list.extend(self.merge_data([value]))

        return merged_list

    def _group_invalid_data(self):
        """Group invalid data in a string to display in a alert"""
        start_str = "The Following attributes are not valid:\n"

        for item in self.validation_data:
            for item_key, item_value in item.items():
                if item_key != "msg":
                    continue
                if not item["is_valid"]:
                    start_str += "- {}\n".format(item["msg"])

        return start_str

    def on_ok_clicked(self):
        """Processing User input and save data in scenario"""

        self.validation_data.clear()

        self.trigger_input_validation.emit()

        for validated_item in self.validation_data:
            for item_key, item_value in validated_item.items():
                if isinstance(item_value, bool):
                    if not item_value:
                        gen_quick_warning_modal(
                            self, "Validation error", self._group_invalid_data()
                        )

                        return

        self.accepted.emit()

        self._ui.accept()

    def adjust_tree_size(self):
        """Initially  Adjust treeWidget height to fit items"""

        total_height = 0
        iterator = QtWidgets.QTreeWidgetItemIterator(self._ui.treeWidget)
        while iterator.value():
            item = iterator.value()
            row = self._ui.treeWidget.indexOfTopLevelItem(item)
            total_height += self._ui.treeWidget.sizeHintForRow(row)
            iterator += 1

        # Adjust for header height and any additional margins or spacing
        total_height += self._ui.treeWidget.header().height()
        total_height += (
            self._ui.treeWidget.contentsMargins().top()
            + self._ui.treeWidget.contentsMargins().bottom()
        )

        # Set the height of the QTreeWidget
        self._ui.treeWidget.setFixedHeight(total_height)
        self.fired_once = True

    def _reset_attributes(self):
        """Reset UI to default state and rebuild tree view"""
        self._ui.treeWidget.clear()
        self._tree_items.clear()

        current_agent_type = self._ui.comboBoxType.currentText()

        for attr_name, attr_spec in self._schema.agent_types[
            current_agent_type
        ].attributes.items():
            item = AttributeTreeItem(
                self._ui.treeWidget,
                attr_name,
                attr_spec,
                self._schema,
                self._working_dir,
                validation_signal=self.trigger_input_validation,
                validation_error_signal=self.validation_error_signal,

            )
            self._tree_items.append(item)

        self._ui.treeWidget: QtWidgets.QTreeWidget

        self._ui.treeWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )

        self.adjust_tree_size()

    def update(self) -> None:
        """Update tree view and adjust size"""

        self.adjust_tree_size()
        super().update()

    def make_new_agent(self, agent_id) -> models.Agent:
        """Create a new agent with the given ID if it has a value. Note also used for editing agents"""
        agent_type = self._ui.comboBoxType.currentText()
        agent = models.Agent(agent_id, agent_type)

        for item in self._tree_items:
            if item.attr_value is not None:
                attr = fameio.Attribute(item.attr_name, item.attr_value)

                agent.add_attribute(item.attr_name, attr)
        return agent
