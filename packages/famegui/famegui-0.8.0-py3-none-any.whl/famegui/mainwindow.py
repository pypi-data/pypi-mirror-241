# This Python file uses the following encoding: utf-8
import getpass
import logging
import os
import logging
import getpass
import re
import typing
from functools import partial

import fameio
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QModelIndex, Qt, QPointF, QPoint
from PySide2.QtGui import QColor
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QGroupBox,
    QFormLayout,
    QMenu,
    QAction,
    QSizePolicy,
    QMessageBox,
    QLabel,
    QTreeWidgetItem,
    QGraphicsScene,
)
from fameio.source.scenario import Attribute

from famegui.config.runtime_consts import CONTRACT_RECEIVER_ID, UPDATED_CONTRACT_KEY, OLD_CONTRACT_KEY, \
    CONTRACT_SENDER_ID
from famegui.database.db_management import (
    get_recently_opened_projects,
    manage_path_for_db,
)

from famegui.appworkingdir import AppWorkingDir
from famegui import models
import famegui.generated.qt_resources_rc
from famegui.agent_controller import AgentController
from famegui.dialogs.ask_for_agent_deletion_dialog import DeletionDialog
from famegui.dialogs.dialog_new_multi_dialog import DialogNewMultiContract
from famegui.dialogs.dialog_newagent import DialogNewAgent
from famegui.dialogs.dialog_newcontract import DialogNewContract
from famegui.dialogs.dialog_scenario_properties import DialogScenarioProperties
from famegui.dialogs.edit_agent_dialog import EditAgentDialog
from famegui.dialogs.edit_contract_dialog import EditContractDialog
from famegui.generated.ui_mainwindow import Ui_MainWindow
from famegui.maincontroller import MainController
from famegui.models import Agent, Contract
from famegui.path_resolver import FameGuiPathResolver
from famegui.scenario_graph_view import ScenarioGraphView
from famegui.scenario_graph_view_items import ContractGraphItem
from famegui.ui.quick_modals import gen_quick_warning_modal
from famegui.ui.ui_utils import GUIConsoleHandler
from famegui.utils import get_product_name_from_contract, get_id_from_item_desc

""" needs to be imported to load the resources """
""" Some IDEs may mark this as unused, but it is needed to load the resources """
import famegui.generated.qt_resources_rc


class PropertyTreeItem(QtWidgets.QTreeWidgetItem):
    def __init__(
            self,
            parent: QtWidgets.QTreeWidget,
            attr_name: str,
            attr_value: Attribute,
    ):
        super().__init__(parent, [attr_name, str(attr_value.value)])
        self.setFlags(self.flags() | QtCore.Qt.ItemIsEditable)

    def setData(self, column, role, value):
        """Override QTreeWidgetItem.setData()"""
        if role == QtCore.Qt.EditRole:
            # review: Can we remove this code? It seems to be unused at the moment and not necessary.
            # logging.info("new value: {}".format(value))
            pass

        QtWidgets.QTreeWidgetItem.setData(self, column, role, value)


class MainWindow(QMainWindow):
    def __init__(self, working_dir: AppWorkingDir):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._working_dir = working_dir
        self._path_resolver = FameGuiPathResolver(self._working_dir)
        self._tree_items_for_agent_types = {}
        self._controller = MainController(self._working_dir)
        # init
        self._init_ui()
        self._connect_actions()
        self._connect_slots()
        self._on_project_closed()

    def _init_ui(self):
        logging.debug("initializing main window UI")
        self.setWindowIcon(QtGui.QIcon(":/icons/nodes-128px.png"))
        # create and attach the scene

        self._graph_view = ScenarioGraphView(self)
        self._graph_view.setSceneRect(self._controller.compute_scene_rect())
        self.ui.graphicsView.setScene(self._graph_view)
        # important: set the index method to NoIndex, otherwise the scene will not be updated correctly and crash
        self._graph_view.setItemIndexMethod(QGraphicsScene.NoIndex)

        # customize main window
        self.ui.labelUserName.setText(getpass.getuser())
        self.ui.graphicsView.setBackgroundBrush(QtGui.QColor(194, 194, 194))

        self.ui.graphicsView.unselect_contracts.connect(self.clear_contract_highlights)
        self.ui.consoleLogTextEdit.setStyleSheet("background: #2D2D2D; ")
        self.ui.consoleLogTextEdit.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.consoleLogTextEdit.verticalScrollBar()
        self.ui.consoleLogTextEdit.setMinimumSize(300, 100)
        self.ui.consoleLogTextEdit.setWidgetResizable(True)
        self.ui.graphicsView.setMinimumSize(400, 400)
        self.ui.graphicsView.setBaseSize(600, 600)

        self.setWindowTitle(QtWidgets.QApplication.instance().applicationDisplayName())
        # allowed zoom range
        self.ui.sliderZoomFactor.setRange(10, 10000)
        # status bar
        self._status_label_icon = QtWidgets.QLabel()
        self.statusBar().addWidget(self._status_label_icon)

        # project structure tree view
        self.ui.treeProjectStructure.all_agents_deletion_requested.connect(
            self._del_all_agents_of_type
        )

        #        self.ui.treeProjectStructure = ExtendedTreeWidget(self.ui.treeProjectStructure.layout())

        self.ui.treeProjectStructure.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )

        self.ui.treeProjectStructure.setColumnCount(1)
        self.ui.treeProjectStructure.setHeaderLabels(["Agents"])
        # attributes tree view
        self.ui.treeAttributes.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )

        self.ui.treeAttributes.setRootIsDecorated(False)
        self.ui.treeAttributes.setColumnCount(2)
        self.ui.treeAttributes.setHeaderLabels(["Attribute", "Value"])
        self.ui.treeAttributes.setColumnWidth(0, 140)
        self.ui.treeAttributes.setAlternatingRowColors(True)
        self.ui.treeAttributes.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )

        # console
        self.ui.consoleLogTextEdit.setMinimumHeight(70)
        self.ui.consoleLogTextEdit.setWidgetResizable(True)
        self.ui.consoleLogTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.consoleLogTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        logger = logging.getLogger()
        formLayout = QFormLayout()
        groupBox = QGroupBox()
        groupBox.setLayout(formLayout)
        self.ui.consoleLogTextEdit.setWidget(groupBox)

        logger.addHandler(GUIConsoleHandler(formLayout, self.ui.consoleLogTextEdit))

        # console
        self.ui.treeProjectStructure.clicked.connect(self.on_clicked_tree)

        # recently opened projects
        recently_opened_projects = get_recently_opened_projects()

        if len(recently_opened_projects) == 0:
            return

        another_menu = QMenu("Recently opened projects", self)

        for project in recently_opened_projects:
            action = QAction(project.path, self)
            action.triggered.connect(partial(self.open_project, project.path))
            another_menu.addAction(action)

        self.ui.menuok.addMenu(another_menu)

    def open_project(self, file_path):
        if not self._confirm_current_project_can_be_closed():
            return
        if file_path != "":
            manage_path_for_db(file_path)

            self.load_scenario_file(file_path)

    def _del_all_agents_of_type(self, agent_type_name: str):
        selected_agent_type_list = self._controller.get_all_agents_by_type_name(
            agent_type_name
        )
        del_dlg = DeletionDialog(
            selected_agent_type_list,
            scenario=self._controller.scenario,
            working_dir=self._working_dir,
            parent_widget=self.ui.widget,
            main_controller=self._controller,
        )

    def _connect_actions(self):
        logging.debug("connecting main window actions")
        # new
        self.ui.actionNewProject.triggered.connect(self.new_project)
        # open
        self.ui.actionOpenProject.triggered.connect(self.show_open_scenario_file_dlg)
        # save (enabled only when a change has been done)
        self.ui.actionSaveProject.triggered.connect(self.save_project)
        # save as
        self.ui.actionSaveProjectAs.triggered.connect(self.save_project_as)
        # close
        self.ui.actionCloseProject.triggered.connect(self.close_project)

        self.ui.actionCloseProject.setVisible(False)
        # generate protobuf
        self.ui.actionMakeRunConfig.triggered.connect(self.make_run_config)
        # exit
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionReArrangeLayout.triggered.connect(self.rearrange_layout)
        self.ui.actionSchemaValidation.triggered.connect(self.revalidate_scenario)

        # edit
        self.ui.actionGeneralProperties.triggered.connect(
            self._on_edit_scenario_properties
        )

        # tree
        self.ui.treeProjectStructure.agent_deletion_requested.connect(
            self._on_single_agent_deletion_requested
        )
        self.ui.treeProjectStructure.single_contract_deletion_requested.connect(
            self._on_single_contract_deletion_requested
        )

    def _on_single_agent_deletion_requested(self, agent_id: int):
        """opens up a deletion dialog for a single agent"""
        DeletionDialog(
            [self._controller.agent_from_id(agent_id)],
            scenario=self._controller.scenario,
            working_dir=self._working_dir,
            parent_widget=self.ui.widget,
            main_controller=self._controller,
        )

    def _get_contract_tree_items(
            self, sender_agent: Agent, receiver_agent: Agent, product_name: str
    ) -> typing.List[QTreeWidgetItem]:
        """returns a list of tree leaf items that represent the contract between the two agents"""

        contract_ids = {sender_agent.id, receiver_agent.id}
        contract_tree_items = []
        agent_type_names = {sender_agent.type_name, receiver_agent.type_name}
        for i in range(self.ui.treeProjectStructure.topLevelItemCount()):
            top_lvl_item = self.ui.treeProjectStructure.topLevelItem(i)
            agent_type = top_lvl_item.text(0)

            if agent_type not in agent_type_names:
                continue
            for agent_child_idx in range(top_lvl_item.childCount()):
                selected_node = top_lvl_item.child(agent_child_idx)
                selected_node_id = int(
                    top_lvl_item.child(agent_child_idx).data(0, Qt.UserRole)
                )

                if selected_node_id not in contract_ids:
                    continue
                for contract_child_idx in range(selected_node.childCount()):
                    selected_contract_leaf = selected_node.child(contract_child_idx)
                    contract_description = selected_contract_leaf.text(0)
                    if product_name not in contract_description:
                        continue
                    if (
                            str(sender_agent.id) not in contract_description
                            and str(receiver_agent.id) not in contract_description
                    ):
                        continue
                    contract_tree_items.append(selected_contract_leaf)

        return contract_tree_items

    def _remove_contract_tree_items(
            self, sender_agent: Agent, receiver_agent: Agent, product_name: str
    ):
        """removes the contract leaf items between the two agents from the tree"""
        contract_ids = {sender_agent.id, receiver_agent.id}
        contract_leafs_to_remove_idx = []
        contract_to_removes = []

        agent_type_names = {sender_agent.type_name, receiver_agent.type_name}
        for i in range(self.ui.treeProjectStructure.topLevelItemCount()):
            top_lvl_item = self.ui.treeProjectStructure.topLevelItem(i)
            agent_type = top_lvl_item.text(0)

            if agent_type not in agent_type_names:
                continue
            for agent_child_idx in range(top_lvl_item.childCount()):
                selected_node = top_lvl_item.child(agent_child_idx)
                selected_node_id = int(
                    top_lvl_item.child(agent_child_idx).data(0, Qt.UserRole)
                )

                if selected_node_id not in contract_ids:
                    continue
                contract_children = [
                    selected_node.child(contract_child_idx)
                    for contract_child_idx in range(selected_node.childCount())
                ]
                for idx, selected_contract_leaf in enumerate(contract_children[:]):
                    contract_description = selected_contract_leaf.text(0)
                    if product_name not in contract_description:
                        continue
                    if (
                            str(sender_agent.id) not in contract_description
                            and str(receiver_agent.id) not in contract_description
                    ):
                        continue

                    contract_leafs_to_remove_idx.append(idx)

                for contract_leaf_to_remove in contract_leafs_to_remove_idx:
                    contract_to_removes.append(
                        {
                            "sender_id": sender_agent.id,
                            "receiver_id": receiver_agent.id,
                            "product_name": get_product_name_from_contract(
                                contract_description
                            ),
                        }
                    )

                    selected_node.removeChild(
                        selected_node.child(contract_leaf_to_remove)
                    )

    def _remove_contract_tree_items_using_contract(self, contract: Contract):
        """removes the contract leaf items between the two agents from the tree using a contract object"""

        self._remove_contract_tree_items(
            self._controller.get_agent_ctrl(contract.sender_id).model,
            self._controller.get_agent_ctrl(contract.receiver_id).model,
            contract.product_name,
        )

    def _on_single_contract_deletion_requested(
            self, sender_agent_id: int, receiver_agent_id: int, product_name: str
    ):
        """opens up a deletion dialog for a single contract"""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(
            f"Do you want to delete the contract with the sender: {sender_agent_id}\n.And the receiver: {receiver_agent_id}\nwith the product name:  ({product_name}) ?"
        )
        msg_box.setWindowTitle("Confirmation")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        msg_box.setDefaultButton(QMessageBox.No)

        response = msg_box.exec()

        alert_badge = QLabel()
        alert_badge.setText("Alert!")
        alert_badge.setStyleSheet(
            "background-color: red;"
            "color: white;"
            "border-radius: 8px;"
            "padding: 4px 8px;"
        )

        if response == QMessageBox.Yes:
            self._controller.remove_contract(
                sender_agent_id, receiver_agent_id, product_name
            )
            self.ui.treeProjectStructure.blockSignals(True)
            self._graph_view.blockSignals(True)

            self._controller.set_unsaved_changes(True)

            self._remove_contract_tree_items(
                self._controller.get_agent_ctrl(sender_agent_id).model,
                self._controller.get_agent_ctrl(receiver_agent_id).model,
                product_name,
            )

            self._graph_view.remove_contract(sender_agent_id, receiver_agent_id)

            self.ui.treeProjectStructure.blockSignals(False)
            self._graph_view.blockSignals(False)

    def revalidate_scenario(self):
        if not self._controller.is_open:
            return
        self._controller.revalidate_scenario()

    # Contract UI Utils
    def rearrange_layout(self):
        """adjust the layout of the graph view in circular orbital mode"""
        if not self._controller.is_open:
            return
        self._controller.rearrange_layout()
        for item in self.ui.graphicsView.items():
            if issubclass(type(item), ContractGraphItem):
                item: ContractGraphItem
                item.adjust()

    def clear_contract_highlights(self):
        """Resets the highlight mode of all contract items in the graph view"""
        for item in self._graph_view.get_contract_items():
            if item.is_in_highlight_mode():
                item.set_highlight_mode(False)
                item.adjust()

    def _connect_slots(self):
        """Event handling for the main window"""
        logging.debug("initializing main window slots")
        self.ui.sliderZoomFactor.valueChanged.connect(self._on_zoom_value_changed)
        self._graph_view.selected_agent_changed.connect(
            self._controller.set_selected_agent_id
        )
        self._graph_view.contract_creation_requested.connect(
            self._on_contract_creation_requested
        )

        self._graph_view.agent_creation_requested.connect(
            self._on_agent_creation_requested
        )

        self.ui.graphicsView.agent_deletion_requested.connect(
            self._on_agent_deletion_requested
        )

        self._graph_view.agent_edition_requested.connect(
            self._on_agent_edition_requested
        )

        self.ui.treeProjectStructure.currentItemChanged.connect(
            self._on_tree_view_current_item_changed
        )

        self.ui.treeProjectStructure.itemDoubleClicked.connect(
            self._on_tree_view_current_item_double_clicked
        )

        self.ui.lineFilterPattern.textChanged.connect(self._filter_pattern_changed)
        self._graph_view.zoom_in_requested.connect(
            lambda: self.ui.sliderZoomFactor.setValue(
                self.ui.sliderZoomFactor.value() + 10
            )
        )
        self._graph_view.released_multi_selection_mode.connect(
            self.on_multi_agent_select
        )

        self._graph_view.released_multi_selection_mode_no_valid.connect(
            self.clear_graph_from_multi_selection
        )
        self._graph_view.zoom_out_requested.connect(
            lambda: self.ui.sliderZoomFactor.setValue(
                self.ui.sliderZoomFactor.value() - 10
            )
        )

        self._controller.project_properties.changed.connect(
            self._on_scenario_status_changed
        )
        self._controller.agent_added.connect(self._on_agent_added)
        self._controller.contract_added.connect(self._on_contract_added)
        self._controller.contracts_deleted.connect(self._on_contract_removed)
        self._controller.agents_deleted.connect(self._on_agents_deleted)
        self._controller.selected_agent_changed.connect(self._on_selected_agent_changed)

    def _on_agents_deleted(self, agent_ids: typing.List[int]):
        """initiates removal of agents from the graph view and the tree view"""
        self._graph_view.clearSelection(True)
        self.clear_contract_highlights()
        self.ui.treeAttributes.clear()

        self.ui.treeProjectStructure.blockSignals(True)

        for agent_id in agent_ids:
            agent_ctrl = self._controller.get_agent_ctrl(agent_id)
            self.remove_agent_tree_item(agent_ctrl)
        self._graph_view.remove_agents(agent_ids)
        self.ui.treeProjectStructure.blockSignals(False)

    def _on_agent_edition_requested(self, agent_id: int):
        """initiates the agent edition dialog"""
        EditAgentDialog(
            agents=[self._controller.agent_from_id(agent_id)],
            scenario=self._controller.scenario,
            working_dir=self._working_dir,
            main_ctrl=self._controller,
        )

    def _on_agent_deletion_requested(self, q_point: QPoint):
        """initiates the agent deletion dialog"""
        map_point: QPointF = self.ui.graphicsView.mapToScene(q_point)
        agent_id = self._graph_view.get_agent_id(map_point)
        if not agent_id:
            gen_quick_warning_modal(
                self.parentWidget(),
                "No Agent Selected",
                "Please select at least one agent\n"
                "or navigate your mouse to an agent",
            )
            return
        selected_agent = self._controller.agent_from_id(agent_id)
        DeletionDialog(
            [selected_agent],
            scenario=self._controller.scenario,
            working_dir=self._working_dir,
            parent_widget=self.ui.widget,
            main_controller=self._controller,
        )

    def _on_zoom_value_changed(self):
        zoom_factor = self.ui.sliderZoomFactor.value()
        assert zoom_factor > 0
        scale_factor = zoom_factor * 0.001
        self.ui.graphicsView.setTransform(
            QtGui.QTransform.fromScale(scale_factor, scale_factor)
        )
        self.ui.labelZoomFactor.setText("{} %".format(zoom_factor))

    def clear_graph_from_multi_selection(self):
        """Clears the graph view from multi selection mode by clearing the selection and the highlights"""
        self._graph_view.clearSelection(True)
        self.clear_contract_highlights()

    def _get_agent_list_from_ids(
            self, agent_id_list: typing.List[int]
    ) -> typing.List[Agent]:
        """Fetches the agent object list from the agent id list"""
        agent_list = []
        for agent_id in agent_id_list:
            agent_list.append(self._controller.agent_from_id(agent_id))
        return agent_list

    def on_multi_agent_select(self, sender_list: list, receiver_list: list):
        """Initiates the multi contract creation dialog"""
        self.clear_graph_from_multi_selection()
        sender_agent_list = self._get_agent_list_from_ids(sender_list)
        receiver_agent_list = self._get_agent_list_from_ids(receiver_list)

        dlg = DialogNewMultiContract(
            receiver_agent_list,
            sender_agent_list,
            self._controller.scenario.schema,
            self,
        )

        if dlg.exec_() != 0:
            for contract in dlg.make_new_contracts():
                self._controller.add_new_contract(contract)

    def _on_tree_view_current_item_double_clicked(self):
        """initiates a matching edition dialog"""
        assert self._controller.is_open
        tree_item = self.ui.treeProjectStructure.currentItem()

        if tree_item is not None:
            # note: the given id value can be None
            selected_agent_id = tree_item.data(0, QtCore.Qt.UserRole)

            if selected_agent_id:
                agent_ctrl_list = [self._controller.agent_from_id(selected_agent_id)]
                agent_model_list = [agent_ctrl.model for agent_ctrl in agent_ctrl_list]
                EditAgentDialog(
                    agents=agent_model_list,
                    scenario=self._controller.scenario,
                    working_dir=self._working_dir,
                    main_ctrl=self._controller,
                )

                return
            agent_type = tree_item.text(0)
            if agent_type:
                selected_agents = self._controller.get_all_agents_by_type_name(
                    agent_type
                )
                if len(selected_agents) != 0:
                    EditAgentDialog(
                        agents=selected_agents,
                        scenario=self._controller.scenario,
                        working_dir=self._working_dir,
                        main_ctrl=self._controller,
                    )
                    return

            # single contract selection
            parent_agent_item = tree_item.parent()
            selected_con_agent_id = tree_item.data(2, QtCore.Qt.UserRole)
            parent_agent_item_id = parent_agent_item.data(0, QtCore.Qt.UserRole)
            product_name = get_product_name_from_contract(
                tree_item.data(1, QtCore.Qt.UserRole)
            )

            if tree_item.data(1, QtCore.Qt.UserRole) == "receiver":
                edit_contract_dlg = EditContractDialog(
                    self._controller.get_contract(
                        selected_con_agent_id, parent_agent_item_id, product_name
                    ),
                    self._controller.scenario,
                    self._controller,
                    on_contract_edited_slot=self._on_contract_edited,
                )
                edit_contract_dlg.on_contract_edited.connect(self._on_contract_edited)

                return

            edit_contract_dlg = EditContractDialog(
                self._controller.get_contract(
                    parent_agent_item_id, selected_agent_id, product_name
                ),
                self._controller.scenario,
                self._controller,
                on_contract_edited_slot=self._on_contract_edited,
            )
            edit_contract_dlg.on_contract_edited.connect(self._on_contract_edited)

    def _on_contract_removed(self, agent_id: int):
        """Clears the graph view and the tree view from the given agent id after removing it from the scenario"""
        related_contracts = self._controller.get_all_related_contracts(agent_id)
        self.ui.treeProjectStructure.blockSignals(True)
        self._graph_view.blockSignals(True)

        for related_contract in related_contracts:
            self._graph_view.remove_contract(
                related_contract.sender_id, related_contract.receiver_id
            )
            self._remove_contract_tree_items_using_contract(related_contract)

        self.ui.treeProjectStructure.blockSignals(False)
        self._graph_view.blockSignals(False)
        self._controller.set_unsaved_changes(True)

    def _on_contract_edited(self, contracts: dict):
        """Updates the graph view and the tree view after editing a contract"""
        self._graph_view.clearSelection()
        old_contract_sender_ctrl = self._controller.get_agent_ctrl(contracts[OLD_CONTRACT_KEY][CONTRACT_SENDER_ID])
        old_contract_receiver_ctrl = self._controller.get_agent_ctrl(contracts[OLD_CONTRACT_KEY][CONTRACT_RECEIVER_ID])
        new_contract_sender_ctrl = self._controller.get_agent_ctrl(contracts[UPDATED_CONTRACT_KEY][CONTRACT_SENDER_ID])
        new_contract_receiver_ctrl = self._controller.get_agent_ctrl(
            contracts[UPDATED_CONTRACT_KEY][CONTRACT_RECEIVER_ID])

        self._graph_view.remove_contract(
            old_contract_sender_ctrl.id,
            old_contract_receiver_ctrl.id,
        )

        self._graph_view.add_contract(
            new_contract_sender_ctrl,
            new_contract_receiver_ctrl,
        )

        self._remove_contract_tree_items(
            old_contract_sender_ctrl.model,
            old_contract_receiver_ctrl.model,
            contracts[OLD_CONTRACT_KEY]["productname"]
        )

        self._create_tree_view_contract(
            new_contract_sender_ctrl,
            new_contract_receiver_ctrl,
            Contract.from_dict(contracts[UPDATED_CONTRACT_KEY])
        )

    def _on_tree_view_current_item_changed(self):
        assert self._controller.is_open
        selected_agent_id = None
        tree_item = self.ui.treeProjectStructure.currentItem()
        self.ui.treeProjectStructure.indexFromItem(tree_item, 0)

        if tree_item is not None:
            # note: the given id value can be None
            selected_agent_id = tree_item.data(0, QtCore.Qt.UserRole)
        self._controller.set_selected_agent_id(selected_agent_id)

    def _on_agent_creation_requested_accepted(
            self, dlg: DialogNewAgent, x: int, y: int
    ):
        new_agent = dlg.make_new_agent(self._controller.generate_new_agent_id())
        self._controller.add_new_agent(new_agent, x, y)
        self._graph_view.setSceneRect(self._controller.compute_scene_rect())

        dlg.save_data_in_scenario(data=self._controller.scenario, agent_id=new_agent.id)

    def _on_agent_creation_requested(self, x: int, y: int):
        assert self._controller.is_open

        dlg = DialogNewAgent(
            self._controller.schema, self._working_dir, self._controller.scenario
        )

        if dlg._ui.exec_() != 0:
            new_agent = dlg.make_new_agent(self._controller.generate_new_agent_id())

            self._controller.add_new_agent(new_agent, x, y)

            self._graph_view.setSceneRect(self._controller.compute_scene_rect())

    def _on_contract_creation_requested(self, sender_id: int, receiver_id: int):
        sender = self._controller.agent_from_id(sender_id)
        receiver = self._controller.agent_from_id(receiver_id)
        dlg = DialogNewContract(
            sender, receiver, self._controller.scenario.schema, self
        )
        if dlg.exec_() != 0:
            self._controller.add_new_contract(dlg.make_new_contract())

    def highlight_all_contracts_from_agent(self, agent_id):
        """Highlighting all contracts from a given agent in graph view"""
        for graphic_item in self._graph_view.get_contract_items():
            graphic_item: ContractGraphItem
            if graphic_item.sourceNode().agent_id.__eq__(
                    agent_id
            ) or graphic_item.destNode().agent_id.__eq__(agent_id):
                graphic_item.set_highlight_mode(True)
                graphic_item.adjust()

    def _on_selected_agent_changed(self, agent_ctrl: AgentController):

        self.clear_contract_highlights()

        if self._graph_view.is_in_multi_selection_mode():
            return

        if agent_ctrl is None:
            # clear selection
            self.ui.treeProjectStructure.clearSelection()
            self._graph_view.clearSelection()
            self.ui.treeAttributes.clear()
            return
        # block signals
        self.ui.treeProjectStructure.blockSignals(True)
        self._graph_view.blockSignals(True)

        # update graph view
        if self._graph_view.is_in_multi_selection_mode():
            return
        self._graph_view.clearSelection()
        agent_ctrl.scene_item.setSelected(True)

        # update tree view
        self.ui.treeProjectStructure.setCurrentItem(agent_ctrl.tree_item)

        # update agent view
        self.ui.treeAttributes.clear()
        item_type = QtWidgets.QTreeWidgetItem(
            self.ui.treeAttributes, ["Type", agent_ctrl.type_name]
        )

        item_type.setBackgroundColor(1, agent_ctrl.svg_color)
        QtWidgets.QTreeWidgetItem(self.ui.treeAttributes, ["ID", agent_ctrl.display_id])

        for attr_name, attr_value in agent_ctrl.attributes.items():
            attr_value: fameio.Attribute
            PropertyTreeItem(self.ui.treeAttributes, attr_name, attr_value).setToolTip(
                0,
                self._controller.get_help_text_for_attr(
                    agent_ctrl.type_name, attr_name
                ),
            )

        for graphic_item in self._graph_view.get_contract_items():
            graphic_item: ContractGraphItem
            if graphic_item.sourceNode().agent_id.__eq__(
                    agent_ctrl.id
            ) or graphic_item.destNode().agent_id.__eq__(agent_ctrl.id):
                graphic_item.set_highlight_mode(True)
                graphic_item.adjust()

        # unblock signals
        self.ui.treeProjectStructure.blockSignals(False)
        self._graph_view.blockSignals(False)

    def _filter_pattern_changed(self):
        pattern = self.ui.lineFilterPattern.text().lower()
        for a in self._controller.agent_list:
            hide = a.type_name.lower().find(pattern) == -1
            a.tree_item.setHidden(hide)

    def _tree_item_parent_for_agent(self, agent_ctrl) -> QtWidgets.QTreeWidgetItem:
        # return existing if it already exists
        if agent_ctrl.type_name in self._tree_items_for_agent_types:
            return self._tree_items_for_agent_types[agent_ctrl.type_name]
        item = QtWidgets.QTreeWidgetItem(
            self.ui.treeProjectStructure, [agent_ctrl.type_name]
        )

        item.setExpanded(True)
        item.setBackgroundColor(0, agent_ctrl.svg_color)
        self._tree_items_for_agent_types[agent_ctrl.type_name] = item

        return item

    def remove_agent_tree_item(self, agent_ctrl: AgentController):
        """removes second stage agents from the tree view + top lvl items if there are no more children left"""
        parent_item = self._tree_item_parent_for_agent(agent_ctrl)
        parent_item.removeChild(agent_ctrl.tree_item)
        child_count = parent_item.childCount()

        if child_count != 0:
            return
        for idx in range(0, self.ui.treeProjectStructure.topLevelItemCount()):
            if self.ui.treeProjectStructure.topLevelItem(idx) == parent_item:
                self.ui.treeProjectStructure.takeTopLevelItem(idx)
                del self._tree_items_for_agent_types[agent_ctrl.type_name]

        self.ui.treeProjectStructure.blockSignals(True)
        self._graph_view.blockSignals(True)
        self.ui.treeProjectStructure.blockSignals(False)
        self._graph_view.blockSignals(False)

    def _create_agent_tree_item(self, agent_ctrl: AgentController):
        parent_item = self._tree_item_parent_for_agent(agent_ctrl)
        # create tree item
        item = QtWidgets.QTreeWidgetItem(parent_item, [agent_ctrl.display_id])
        item.setBackgroundColor(0, QtGui.QColor(agent_ctrl.svg_color))
        item.setData(0, QtCore.Qt.UserRole, agent_ctrl.id)
        item.setToolTip(0, agent_ctrl.tooltip_text)
        # add item

        agent_ctrl.tree_item = item
        self.ui.treeProjectStructure.addTopLevelItem(item)

    def _on_agent_added(self, agent_ctrl: AgentController):
        logging.debug("agent_added: {}".format(agent_ctrl.display_id))
        self._graph_view.add_agent(agent_ctrl)
        self._create_agent_tree_item(agent_ctrl)

    def highlight_contract(
            self, sender_id, receiver_id, single_highlight_mode=False
    ):
        """Highlights the contract in the graph view between selected agents"""

        for graphic_item in self._graph_view.get_contract_items():
            graphic_item: ContractGraphItem
            if graphic_item.sourceNode().agent_id.__eq__(
                    sender_id
            ) and graphic_item.destNode().agent_id.__eq__(receiver_id):
                graphic_item.set_highlight_mode(True)
                if single_highlight_mode:
                    graphic_item.set_single_highlight_mode(True)
                graphic_item.adjust()
                return
            elif graphic_item.sourceNode().agent_id.__eq__(
                    receiver_id
            ) and graphic_item.destNode().agent_id.__eq__(sender_id):
                graphic_item.set_highlight_mode(True)
                if single_highlight_mode:
                    graphic_item.set_single_highlight_mode(True)
                graphic_item.adjust()
                return

    def on_clicked_tree(self, pos: QModelIndex):
        """Handles the click event on the agent tree view.
        Process all types of tree items"""

        pos.parent().data(QtCore.Qt.UserRole)
        parent_agent_id = pos.parent().data(
            QtCore.Qt.UserRole
        )  # get Id from selected agent level

        if parent_agent_id is None:
            return
        results = re.findall(
            r"\d+", str(pos.data(0))
        )  # extract Id of partner agent from the 1 to 1 contract
        if len(results) == 0:  # prevent mismatching
            return
        agent_id = results[0]

        if parent_agent_id is None:
            return

        self.highlight_contract(int(parent_agent_id), int(agent_id), True)

    def _create_tree_view_contract(
            self,
            sender: AgentController,
            receiver: AgentController,
            contract: models.Contract,
    ):
        sender_tree_item = QtWidgets.QTreeWidgetItem(
            sender.tree_item,
            ["{} ({})".format(receiver.display_id, contract.product_name)],
        )
        sender_tree_item.setIcon(0, QtGui.QIcon(":/icons/16px-login.png"))
        sender_tree_item.setData(1, QtCore.Qt.UserRole, "sender")
        sender_tree_item.setData(2, QtCore.Qt.UserRole, receiver.id)
        sender_tree_item.setBackground(0, QColor(0, 255, 0, 100))  # green color sender

        receiver_tree_item = QtWidgets.QTreeWidgetItem(
            receiver.tree_item,
            [" ({}) {}".format(contract.product_name, sender.display_id)],
        )

        receiver_tree_item.setBackground(
            0, QColor(255, 0, 0, 100)
        )  # red color receiver
        receiver_tree_item.setData(1, QtCore.Qt.UserRole, "receiver")
        receiver_tree_item.setData(2, QtCore.Qt.UserRole, sender.id)
        receiver_tree_item.setIcon(0, QtGui.QIcon(":/icons/16px-logout.png"))

    def _on_contract_added(
            self,
            sender: AgentController,
            receiver: AgentController,
            contract: models.Contract,
    ):
        """Handles the event when a new contract is added to the scenario by creating UI elements"""
        # update scene graph
        self._graph_view.add_contract(sender, receiver)
        # update tree view
        self._create_tree_view_contract(sender, receiver, contract)

    def _confirm_current_project_can_be_closed(self) -> bool:
        if self._controller.has_unsaved_changes:
            choice = QtWidgets.QMessageBox.warning(
                self,
                self.tr("Modifications will be lost"),
                self.tr(
                    "Modifications done to the current scenario have not been saved!\n\nWhat do you want to do?"
                ),
                QtWidgets.QMessageBox.StandardButtons(
                    QtWidgets.QMessageBox.Save
                    | QtWidgets.QMessageBox.Discard
                    | QtWidgets.QMessageBox.Cancel
                ),
                QtWidgets.QMessageBox.Cancel,
            )
            if choice == QtWidgets.QMessageBox.Save:
                return self.save_project()
            elif choice == QtWidgets.QMessageBox.Discard:
                return True
            else:
                return False
        return True

    def _on_project_closed(self):
        self._graph_view.clear()
        # reset zoom
        self.ui.sliderZoomFactor.setValue(50)
        # reset attributes
        self._tree_items_for_agent_types = {}
        # reset scenario
        self._controller.reset()
        # reset ui
        self.ui.treeProjectStructure.clear()
        self.ui.treeAttributes.clear()
        self.ui.lineFilterPattern.clear()
        self.ui.labelProjectName.clear()

    def display_error_msg(self, msg: str) -> None:
        logging.error(msg)
        if not msg.endswith("."):
            msg += "."
        QtWidgets.QMessageBox.critical(self, self.tr("Error"), msg)

    def new_project(self):
        if not self._confirm_current_project_can_be_closed():
            return
        self._on_project_closed()

        dlg = DialogScenarioProperties(
            models.GeneralProperties.make_default(), self._working_dir, self
        )
        dlg.setWindowTitle(self.tr("New scenario"))
        # ask user to choose which schema to use for that new scenario
        dlg.enable_schema_selection()

        if dlg.exec_() != 0:
            schema_path = dlg.get_selected_schema_full_path()
            schema = models.Schema.load_yaml_file(schema_path)
            scenario = models.Scenario(schema, dlg.make_properties())
            self._controller.reset(scenario)

    def save_project(self) -> bool:
        if not self._controller.is_open:
            return False
        return self._do_save_project_as(self._controller.project_properties.file_path)

    def save_project_as(self) -> bool:
        if not self._controller.is_open:
            return False
        return self._do_save_project_as("")

    def _do_save_project_as(self, file_path: str) -> bool:
        assert self._controller.is_open

        if file_path == "":
            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                self,
                self.tr("Save scenario file"),
                self._working_dir.scenarios_dir,
                "Scenario file (*.yaml *.yml)",
            )
            if file_path == "":
                return False

        self._controller.save_to_file(file_path)
        self._graph_view.setSceneRect(self._controller.compute_scene_rect())
        return True

    def close_project(self) -> None:
        if self._confirm_current_project_can_be_closed():
            self._on_project_closed()

    def show_open_scenario_file_dlg(self):
        if not self._confirm_current_project_can_be_closed():
            return

        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            self.tr("Open scenario file"),
            self._working_dir.scenarios_dir,
            self.tr("Scenario (*.yaml *.yml)"),
        )
        if file_path != "":
            self.load_scenario_file(file_path)

    def _on_scenario_status_changed(self):
        logging.debug(
            "scenario status changed: agents={}, contracts={}".format(
                self._controller.agent_count, self._controller.contract_count
            )
        )

        is_open = self._controller.is_open
        self.ui.treeProjectStructure.setEnabled(is_open)
        self.ui.treeAttributes.setEnabled(is_open)
        self.ui.lineFilterPattern.setEnabled(is_open)
        self.ui.graphicsView.setEnabled(is_open)
        self.ui.sliderZoomFactor.setEnabled(is_open)

        props = self._controller.project_properties
        if is_open:
            if props.file_path != "":
                self.ui.labelProjectName.setText(props.file_path)
            else:
                self.ui.labelProjectName.setText(self.tr("Unsaved scenario"))
        else:
            self.ui.labelProjectName.setText("")

        self.ui.actionSaveProject.setEnabled(props.has_unsaved_changes)
        self.ui.actionGeneralProperties.setEnabled(is_open)
        self.ui.actionMakeRunConfig.setEnabled(self._controller.can_export_protobuf)

        # update status bar
        if self._controller.agent_count > 0:
            if props.is_validation_successful:
                self._status_label_icon.setPixmap(":/icons/success-16px.png")
                self._status_label_icon.setToolTip(
                    self.tr("Schema validation succeeded")
                )
            else:
                self._status_label_icon.setPixmap(":/icons/warning-16px.png")
                all_errors = "\n".join(props.validation_errors)
                self._status_label_icon.setToolTip(
                    self.tr("Schema validation failed:\n{}".format(all_errors))
                )
        else:
            self._status_label_icon.clear()

    def load_scenario_file(self, file_path):
        self._on_project_closed()
        file_path = os.path.abspath(file_path)
        try:
            logging.info("opening scenario file {}".format(file_path))
            # TODO prevent freezing UI at this place with Multithreading -> Freezing place number 1
            scenario_model = models.ScenarioLoader.load_yaml_file(
                file_path, self._path_resolver
            )

            self._controller.init_scenario_model(scenario_model, file_path)
        except Exception as e:
            self._on_project_closed()
            self.display_error_msg("Failed to open scenario file: {}".format(e))
            return

        props = self._controller.project_properties
        if not props.is_validation_successful:
            QtWidgets.QMessageBox.warning(
                self,
                self.tr("Validation failure"),
                self.tr("The loaded scenario does not fulfill the schema:\n\n")
                + "\n".join(props.validation_errors),
            )
        self.ui.actionCloseProject.setVisible(True)

    def _on_edit_scenario_properties(self):
        dlg = DialogScenarioProperties(
            self._controller.scenario.general_properties, self._working_dir, self
        )
        dlg.setWindowTitle(self.tr("Scenario properties"))
        if dlg.exec_() != 0:
            self._controller.update_scenario_properties(dlg.make_properties())

    def make_run_config(self):
        assert self._controller.can_export_protobuf
        scenario_name = os.path.basename(
            self._controller.project_properties.file_path
        ).replace(".yaml", "")
        output_path = "{}/{}.pb".format(self._working_dir.protobuf_dir, scenario_name)
        output_path = self._working_dir.make_relative_path(output_path)

        dlg = DialogScenarioProperties(
            self._controller.scenario.general_properties, self._working_dir, self
        )
        dlg.setWindowTitle(self.tr("Make run config"))
        dlg.enable_outputfile_selection(output_path)
        if dlg.exec_() != 0:
            self._controller.update_scenario_properties(dlg.make_properties())
            self.save_project()
            output_path = self._working_dir.make_full_path(dlg.get_output_file_path())

            # display progress dialog
            progress_dlg = QtWidgets.QProgressDialog(self)
            progress_dlg.setLabelText(self.tr("Generating protobuf file..."))
            progress_dlg.setRange(0, 0)
            progress_dlg.setCancelButton(None)
            progress_dlg.show()
            QApplication.processEvents()

            try:
                models.write_protobuf_output(
                    self._controller.scenario, output_path, self._path_resolver
                )
                progress_dlg.close()
                QtWidgets.QMessageBox.information(
                    self,
                    self.tr("Success"),
                    self.tr(
                        "The following file was successfully generated:\n\n{}"
                    ).format(output_path),
                )
            except Exception as e:
                progress_dlg.close()
                logging.error("failed to generate protobuf output: {}".format(e))
                QtWidgets.QMessageBox.critical(
                    self,
                    self.tr("Error"),
                    self.tr("Failed to generate the protobuf output.\n\n{}").format(e),
                )
            finally:
                progress_dlg.close()

    # prevent data loss when closing the main window
    def closeEvent(self, event):
        if not self._confirm_current_project_can_be_closed():
            event.ignore()
        else:
            event.accept()
