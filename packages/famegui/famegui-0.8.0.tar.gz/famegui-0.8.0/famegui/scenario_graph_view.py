from typing import List

import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPointF
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QGraphicsSceneMouseEvent

from famegui.agent_controller import AgentController
from famegui.scenario_graph_view_items import AgentGraphItem, ContractGraphItem


class ScenarioGraphView(QtWidgets.QGraphicsScene):
    """View displaying the scenario as a graph"""

    # (x, y)
    agent_creation_requested = QtCore.Signal(int, int)
    # (agent_id)
    agent_edition_requested = QtCore.Signal(int)
    # (agent_id)

    # (sender_id, receiver_id)
    contract_creation_requested = QtCore.Signal(int, int)
    # agent_id (can be None)
    selected_agent_changed = QtCore.Signal(int)
    # zoom factor control
    zoom_in_requested = QtCore.Signal()
    move_view_left_requested = QtCore.Signal()
    move_view_right_requested = QtCore.Signal()

    # multi selection
    released_multi_selection_mode = QtCore.Signal(list, list)
    released_multi_selection_mode_no_valid = QtCore.Signal()

    zoom_out_requested = QtCore.Signal()

    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.selectionChanged.connect(self._on_scene_selection_changed)
        self._selected_source_agents = []
        self._selected_target_agents = []
        self._is_in_multi_selection_mode = False
        self.last_state_alt_pressed = False

    def is_in_multi_selection_mode(self) -> bool:
        '''Return True if the multi agent selection mode is enabled'''
        return self._is_in_multi_selection_mode

    def set_multi_selection_mode(self, in_selection_mode: bool):
        '''Enable or disable multi selection mode using a flag'''
        self._is_in_multi_selection_mode = in_selection_mode

    def clearSelection(self, clear_highlights=False) -> None:
        if clear_highlights:
            for agent in self.get_agent_items():
                agent.set_border_highlight(False)
                agent.setSelected(False)

        super().clearSelection()

    @property
    def selected_agent_id(self):
        items = self.selectedItems()
        if len(items) == 1:
            item = items[0]
            assert item.type() == AgentGraphItem.Type
            return item.agent_id
        return None

    def remove_contract(self, agent_sender_id: int, agent_receiver_id: int):
        '''Remove a contract between two agents in the graph '''
        to_delete = []

        for contract in self.get_contract_items():
            contract: ContractGraphItem

            if contract.sourceNode().agent_id == agent_sender_id and contract.destNode().agent_id == agent_receiver_id:
                to_delete.append(contract)
                break

        for contract_to_delete in to_delete:
            self.removeItem(contract_to_delete)

    def get_contract_items(self) -> List[ContractGraphItem]:
        ''' get all contract items in the graph '''
        return_list = []
        for item in self.items():
            if issubclass(type(item), ContractGraphItem):
                return_list.append(item)
        return return_list

    def get_agent_items(self) -> List[AgentGraphItem]:
        ''' get all agent items in the graph '''

        return_list = []
        for item in self.items():
            if issubclass(type(item), AgentGraphItem):
                return_list.append(item)
        return return_list

    def remove_agents(self, agent_ids: List[int]):
        '''Remove a list of agents from the graph'''

        for agent_id in agent_ids:
            self.remove_agent(agent_id)

    def remove_related_contracts(self, agent_id: int):
        '''Remove all contracts related to an agent from the graph'''
        to_delete = []
        for contract in self.get_contract_items():
            contract: ContractGraphItem
            if contract.sourceNode().agent_id == agent_id or contract.destNode().agent_id == agent_id:
                to_delete.append(contract)

        for idx, contract in enumerate(to_delete):
            contract.prepareGeometryChange()
            for child_item in contract.childItems():
                super().removeItem(child_item)

            self.removeItem(contract)

    def remove_agent(self, agent_id: int):
        '''Permanently remove an agent from the graph'''
        agents_to_delete = []
        for agent in self.get_agent_items():
            if agent.agent_id == agent_id:
                agents_to_delete.append(agent)

        self.remove_related_contracts(agent_id)

        for agent in agents_to_delete:
            self.removeItem(agent)

    def add_agent(self, agent_ctrl: AgentController):
        item = AgentGraphItem(agent_ctrl.id, agent_ctrl.type_name, agent_ctrl.svg_color)
        item.setToolTip(agent_ctrl.tooltip_text)
        item.setPos(agent_ctrl.x, agent_ctrl.y)
        item.setZValue(100.0)
        self.addItem(item)
        agent_ctrl.set_scene_item(item)

    def add_contract(self, sender: AgentController, receiver: AgentController):
        self.addItem(ContractGraphItem(sender.scene_item, receiver.scene_item))

    def event(self, event: PySide2.QtCore.QEvent) -> bool:
        '''Handles user events of the scene'''

        if issubclass(type(event), QGraphicsSceneMouseEvent):
            event: QGraphicsSceneMouseEvent
            if event.modifiers() == QtCore.Qt.ShiftModifier:
                self.set_multi_selection_mode(True)
                click_pos = event.scenePos()

                if event.button() == QtCore.Qt.LeftButton:
                    for item in self.items(click_pos):
                        if item.type() == AgentGraphItem.Type:
                            item: AgentGraphItem
                            item.setSelected(True)
                            if not self._selected_source_agents.__contains__(item):
                                self._selected_source_agents.append(item)

                if event.button() == QtCore.Qt.RightButton:
                    for item in self.items(click_pos):
                        if item.type() == AgentGraphItem.Type:
                            item: AgentGraphItem
                            item.setSelected(True, False)
                            if not self._selected_target_agents.__contains__(item):
                                self._selected_target_agents.append(item)

        return super().event(event)

    def mouseDoubleClickEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton:
            return
        click_pos = event.scenePos()
        # is the double click on an agent item?
        for item in self.items(click_pos):
            if item.type() == AgentGraphItem.Type:
                self.agent_edition_requested.emit(item.agent_id)
                return

        self.agent_creation_requested.emit(click_pos.x(), click_pos.y())

    def keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None:
        '''Handles user key events of the scene'''
        '''Usually used to exit multi selection mode'''
        if event.key() == Qt.Key_Shift:
            self.set_multi_selection_mode(False)
            # EXIT MULTI SELECTION MODE
            if len(self._selected_source_agents) != 0 and len(self._selected_target_agents) != 0:
                self.released_multi_selection_mode.emit(
                    [x.agent_id for x in self._selected_target_agents],
                    [x.agent_id
                     for x in self._selected_source_agents])
                self._selected_target_agents.clear()
                self._selected_source_agents.clear()
                for item in self.get_contract_items():
                    item.setSelected(False)
                super().keyReleaseEvent(event)
                return
            self._selected_target_agents.clear()
            self._selected_source_agents.clear()
            self.released_multi_selection_mode_no_valid.emit()
        super().keyReleaseEvent(event)

    def get_agent_id(self, q_point: QPointF):
        '''Helper to return the agent id of the agent at the given position'''
        for item in self.items(q_point):
            if item.type() == AgentGraphItem.Type:
                return item.agent_id

    def _get_agent_id(self, event):
        '''Returns the agent id of the agent at the given position'''
        click_pos = event.scenePos()
        for item in self.items(click_pos):
            if item.type() == AgentGraphItem.Type:
                return item.agent_id

    def mousePressEvent(self, event):
        '''Handles user mouse events of the scene'''
        # Multi SELECT MODE
        if event.button() == QtCore.Qt.RightButton and event.modifiers() != QtCore.Qt.ShiftModifier:
            click_pos = event.scenePos()
            for item in self.items(click_pos):
                if item.type() == AgentGraphItem.Type:
                    self._on_agent_right_clicked(item.agent_id)
                    return
        QtWidgets.QGraphicsScene.mousePressEvent(self, event)

    def wheelEvent(self, event):
        '''enable zoom in/out if ctrl key is pressed'''
        if event.modifiers() == QtCore.Qt.ShiftModifier:
            if event.delta() > 0:
                self.move_view_left_requested.emit()
            else:
                self.move_view_right_requested.emit()
            event.accept()

        if QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier:
            if event.delta() > 0:
                self.zoom_in_requested.emit()
            else:
                self.zoom_out_requested.emit()
            event.accept()

    def _on_agent_right_clicked(self, agent_id):
        source_id = self.selected_agent_id
        if source_id is not None and source_id != agent_id:
            self.contract_creation_requested.emit(source_id, agent_id)

    def _on_scene_selection_changed(self):
        self.selected_agent_changed.emit(self.selected_agent_id)
