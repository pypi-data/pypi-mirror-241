import os.path
from typing import List

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QFile, Qt, Signal
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QDialogButtonBox

from famegui.agent_controller import AgentController
from famegui.maincontroller import MainController
from famegui.models import Scenario


class AgentTreeItem(QtWidgets.QTreeWidgetItem):
    """Tree item for agent that shows agent metadata with a checkbox"""

    def __init__(
        self,
        parent: QtWidgets.QTreeWidget,
        agent_id: int,
        agent_type: str,
        amount_of_contracts: int,
        amount_of_connected_agents: int,
    ):
        self._agent_id = agent_id
        self._agent_type = agent_type
        QtWidgets.QTreeWidgetItem.__init__(self, parent)

        self.setFlags(self.flags() | Qt.ItemIsUserCheckable)
        self.setCheckState(0, Qt.Checked)

        self._display_error = lambda has_error: None

        self.setText(0, str(agent_id))
        self.setText(1, str(agent_type))
        self.setText(2, str(amount_of_contracts))
        self.setText(3, str(amount_of_connected_agents))


class DeletionDialog(QtCore.QObject):
    """Dialog for Agent deletion"""

    def iterate_items(self, parent_item, func):
        pass

    def _get_checked_agents(self, parent_item) -> List[int]:
        """Returns list of by user selected agents"""
        return [
            child_item.text(0)
            for child_item in list(
                filter(lambda x: x.checkState(0) == Qt.Checked, self._tree_items)
            )
        ]

    def __init__(
        self,
        agents_arr: [AgentController],
        scenario: Scenario,
        working_dir,
        parent_widget,
        main_controller,
    ):
        super().__init__()
        self._tree_items = []
        self.scenario: Scenario = scenario
        self._main_controller: MainController = main_controller
        self._agents: [AgentController] = agents_arr

        ui_file = QFile(
            os.path.join(os.path.dirname(__file__), "delete_agent_dialog.ui")
        )
        ui_file.open(QFile.ReadOnly)
        self._loader = QUiLoader()

        self._ui = self._loader.load(ui_file)
        self.init_ui()
        self._ui.exec_()

    def confirm_button_clicked(self):
        """Performs user chosen actions"""
        selected_agent_ids = self._get_checked_agents(
            self._ui.treeWidget.invisibleRootItem()
        )

        if self._ui.checkBoxDeleteAgent.isChecked():
            for agent in selected_agent_ids:
                self._main_controller.remove_agent(agent)

        else:
            """deletes all contracts which are connected to selected agents"""
            # all contract which are connected to selected agents will be deleted
            for agent_id in selected_agent_ids:
                self._main_controller.delete_all_related_contracts(agent_id)

        if self._ui.checkBoxDeleteAllConnectedAgents.isChecked():
            agent_id_set = set(selected_agent_ids)
            for agent_id in selected_agent_ids:
                for (
                    related_agent_id
                ) in self._main_controller.scenario.get_all_related_agents_ids(
                    agent_id
                ):
                    agent_id_set.add(related_agent_id)

            if not self._ui.checkBoxDeleteAgent.isChecked():
                for agent_id in selected_agent_ids:
                    agent_id_set.remove(agent_id)

            for agent_id in agent_id_set:
                self._main_controller.remove_agent(agent_id)

        self._ui.close()

    def cancel_button_clicked(self):
        """Closes the dialog"""
        self._ui.close()

    def init_ui(self):
        """Initializes the UI"""
        self._ui.treeWidget.setRootIsDecorated(False)
        self._ui.treeWidget.setColumnCount(3)
        self._ui.treeWidget.setHeaderLabels(
            [
                "Agent ID",
                "Agent type",
                "Amount of \nconnected Agents",
                "Amount of \ncontracts",
            ]
        )

        self._ui.treeWidget.setColumnWidth(0, 200)
        self._ui.treeWidget.setAlternatingRowColors(True)
        self._reset_attributes()
        self._ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(
            self.confirm_button_clicked
        )
        self._ui.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(
            self.cancel_button_clicked
        )

    def _reset_attributes(self):
        """Resets all attributes to the default state"""
        self._ui.treeWidget.clear()
        self._tree_items.clear()

        for agent in self._agents:
            amount_of_related_contracts = self.scenario.get_amount_of_related_contracts(
                agent.id
            )
            amount_of_connected_agents = self.scenario.get_amount_connected_agents(
                agent.id
            )

            agent: AgentController
            item = AgentTreeItem(
                self._ui.treeWidget,
                agent.id,
                agent.type_name,
                amount_of_connected_agents,
                amount_of_related_contracts,
            )
            self._tree_items.append(item)
