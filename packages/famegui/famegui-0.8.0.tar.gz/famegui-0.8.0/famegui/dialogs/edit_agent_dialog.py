import os

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QFile, Qt
from PySide2.QtGui import QFont
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QDialog, QTreeWidget
from PySide2.QtWidgets import QTreeWidgetItem
from fameio.source.scenario import Attribute
from fameio.source.schema import AttributeSpecs

from famegui.models import Agent, Scenario
from famegui.ui.attribute_row_item import AttributeTreeItem

from PySide2.QtCore import QFile, Slot

from famegui.ui.quick_modals import gen_quick_warning_modal


class EditAgentDialog(QDialog):
    """Dialog for editing agent attributes"""

    trigger_input_validation = QtCore.Signal()
    validation_error_signal = QtCore.Signal(bool, str)

    def __init__(self, scenario, working_dir, agents: [Agent], main_ctrl):
        super().__init__()
        ui_file = QFile(os.path.join(os.path.dirname(__file__), "edit_agent_dialog.ui"))

        ui_file.open(QFile.ReadOnly)
        self._loader = QUiLoader()
        self.validation_list = []

        self._ui = self._loader.load(ui_file)
        self.attr_top_tree_items = []
        self.validation_data = []

        self._agents = agents
        self._scenario = scenario
        self._working_dir = working_dir
        self._main_ctrl = main_ctrl
        self._schema = scenario.schema

        self.init_ui()
        self._ui.setWindowFlags(
            self.windowFlags() | Qt.WindowMaximizeButtonHint | Qt.Window
        )

        self._ui.exec_()

    def init_ui(self):
        """Initialize UI elements"""
        self._ui.treeWidget.setRootIsDecorated(False)
        self._ui.treeWidget.setColumnCount(2)
        self._ui.treeWidget.setHeaderLabels([self.tr("Attribute"), self.tr("Value")])
        self._ui.treeWidget.setColumnWidth(0, 200)
        self._ui.treeWidget.setAlternatingRowColors(True)
        self._ui.treeWidgetShowSelectedAgents.setRootIsDecorated(False)

        self._ui.treeWidgetShowSelectedAgents: QTreeWidget
        self._ui.treeWidgetShowSelectedAgents.setStyleSheet(
            "QTreeWidget::item { padding: 5px; }"
        )
        self._ui.treeWidgetShowSelectedAgents.setFixedHeight(200)
        self._ui.treeWidgetShowSelectedAgents.setColumnCount(3)
        self._ui.treeWidgetShowSelectedAgents.setHeaderLabels(
            [self.tr("selected"), self.tr("#id"), self.tr("agent type")]
        )
        self._ui.treeWidgetShowSelectedAgents.setColumnWidth(0, 200)
        self._ui.treeWidgetShowSelectedAgents.setAlternatingRowColors(True)

        self.validation_error_signal.connect(self.on_err_validation)

        self._reset_attributes()
        self._ui.agent_type_name.setText(self._agents[0].type_name)
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)
        self._ui.agent_type_name.setFont(font)
        self._ui.agent_type_name.setStyleSheet("margin-bottom: 10px;")
        self._ui.buttonBox.accepted.connect(
            self._on_accept
        )  # Connect OK button to accept() method
        self._ui.buttonBox.rejected.connect(
            self._on_cancel
        )  # Connect Cancel button to reject() method

        if len(self._agents) == 1:
            preloaded_agent = self._agents[0]
            preloaded_agent: Agent

            self.init_agent_data(preloaded_agent)

    def _group_invalid_data(self):
        """Group invalid data into a string to be displayed in a modal"""
        start_str = "The Following attributes are not valid:\n"

        for item in self.validation_data:
            for item_key, item_value in item.items():
                if item_key != "msg":
                    continue
                if not item["is_valid"]:
                    start_str += "- {}\n".format(item["msg"])

        return start_str

    def on_err_validation(self, is_valid, attr_name):
        """Receive validation error signal from  a panel item and append to validation data to be checked later"""

        self.validation_data = [
            item for item in self.validation_data if item["msg"] != attr_name
        ]

        self.validation_data.append({"is_valid": is_valid, "msg": attr_name})


    def init_agent_data(self, agent: Agent):
        """Initialize agent default data by building the rows of  tree widget"""
        self._ui.treeWidget.clear()

        for attr_name, attr_spec in self._scenario.schema.agent_types[
            agent.type_name
        ].attributes.items():
            default_attr = None
            attr_spec: AttributeSpecs

            if attr_spec.has_nested_attributes:
                default_attr = agent.attributes.items()

                for item_key, item_value in agent.attributes.items():
                    if item_key == attr_name:
                        default_attr = item_value
                        break

                if not isinstance(default_attr, Attribute):
                    default_attr = None

            else:
                if attr_name in agent.attributes:
                    default_attr = agent.attributes[attr_name]

            if self.validation_error_signal is None:
                raise Exception("self.validation_error_signal is None")
                

            item = AttributeTreeItem(
                self._ui.treeWidget,
                attr_name,
                attr_spec,
                self._schema,
                self._working_dir,
                validation_signal=self.trigger_input_validation,
                validation_error_signal=self.validation_error_signal,
                default_value=default_attr,
            )

            self.attr_top_tree_items.append(item)

    def _on_cancel(self):
        """Close dialog"""
        self._ui.close()

    @staticmethod
    def _match_type_and_id(agent_type, checked_agents_ids_set: set, agent: Agent):
        """Check if agent is of given type and id is in checked_agents_ids_set"""
        return agent.type_name == agent_type and agent.id in checked_agents_ids_set

    def _save_changes(self):
        '''Save changes to scenario'''

        top_lvl_tree_agents = [
            self._ui.treeWidgetShowSelectedAgents.topLevelItem(i)
            for i in range(self._ui.treeWidgetShowSelectedAgents.topLevelItemCount())
        ]
        checked_agents = [item for item in top_lvl_tree_agents if item.checkState(0) == Qt.Checked]
        checked_agents_ids = set([int(item.text(1)) for item in checked_agents])

        self._scenario: Scenario
        matching_agents = [
            agent
            for agent in self._scenario.agents
            if self._match_type_and_id(agent.type_name, checked_agents_ids, agent)
        ]

        for agent in matching_agents:
            agent.attributes.clear()
            for item in self.attr_top_tree_items:
                item: AttributeTreeItem

                if item.attr_value is not None:
                    value = item.attr_value
                    if isinstance(value, dict):
                        value: dict
                        if not value:
                            continue

                    agent.attributes[item.attr_name] = item.attr_value

            self._scenario.update_agent(agent)

        self._main_ctrl.set_unsaved_changes(True)
        self._ui.close()

    def _on_accept(self):
        '''Apply entered changes and close dialog if all data is valid'''
        self.validation_data.clear()
        self.trigger_input_validation.emit()

        # Notify the user if there are any invalid attributes with an Alert
        for validated_item in self.validation_data:
            for item_key, item_value in validated_item.items():
                if isinstance(item_value, bool):
                    if not item_value:
                        gen_quick_warning_modal(self, "Validation error", self._group_invalid_data())

                        return

        self._save_changes()

    def _reset_attributes(self):
        """Reset UI to default state"""
        self._ui.treeWidget.clear()
        self.attr_top_tree_items.clear()
        current_agent_type = self._agents[0].type_name

        for item in self._agents:
            item: Agent
            tree_item = QTreeWidgetItem(self._ui.treeWidgetShowSelectedAgents)
            tree_item.setCheckState(0, Qt.Checked)
            tree_item.setText(1, str(item.id))
            tree_item.setText(2, item.type_name)

        for attr_name, attr_spec in self._scenario.schema.agent_types[
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
            self.attr_top_tree_items.append(item)

        self.adjust_tree_size()

    def update(self) -> None:
        """Update tree view and adjust size"""
        self.adjust_tree_size()
        super().update()

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
        total_height += (
            self._ui.treeWidget.contentsMargins().top()
            + self._ui.treeWidget.contentsMargins().bottom()
        )

        # Set the height of the QTreeWidget
        self._ui.treeWidget.setFixedHeight(total_height)
        self.fired_once = True
