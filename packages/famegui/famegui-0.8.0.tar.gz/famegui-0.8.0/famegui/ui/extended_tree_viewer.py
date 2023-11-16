import re
import typing

import PySide2
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem

from famegui.utils import get_product_name_from_contract


class ExtendedTreeWidget(QTreeWidget):
    """Tree widget that uses custom event signals/triggers to communicate with the main application"""

    all_agents_deletion_requested = QtCore.Signal(str, name="del_all_agents_of_type")
    single_agent_deletion_requested = QtCore.Signal(int, name="del_single_agent")
    single_contract_deletion_requested = QtCore.Signal(
        int, int, str, name="del_single_agent"
    )  # agent_sender_id,agent_receiver_id, product_name

    agent_deletion_requested = QtCore.Signal(int, name="agent_deletion_requested")

    def __init__(
            self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...
    ) -> None:
        super().__init__(parent)

    def _get_id_from_item_desc(self, text: str):
        # extract id from text
        pattern = r"#(\d+)"
        match = re.search(pattern, text)

        if match:
            result = match.group(1)
            return result
        else:
            return ""

    def process_contract_deletion(
            self, text_of_selected_item: str, current_item, agent_id_ref
    ):
        selected_agent_id = current_item.parent().data(0, QtCore.Qt.UserRole)
        connection_type = current_item.data(1, QtCore.Qt.UserRole)  # sender or receiver
        operator_name_two = get_product_name_from_contract(text_of_selected_item)

        if connection_type == "sender":
            self.single_contract_deletion_requested.emit(
                int(selected_agent_id),
                int(agent_id_ref),
                operator_name_two,
            )
            return
        self.single_contract_deletion_requested.emit(
            int(agent_id_ref),
            int(selected_agent_id),
            operator_name_two,
        )

    def keyPressEvent(self, event):
        """Process key press event to process the deletion of agents and contracts"""
        if event.key() == Qt.Key_Delete:
            selected_items = self.selectedItems()

            for item in selected_items:
                parent = item.parent()
                text_of_selected_item = self.currentItem().text(0)

                if not parent:  # -> check if item has no parent to trigger the deletion of all agents of a certain type
                    self.all_agents_deletion_requested.emit(text_of_selected_item)
                    return

                agent_id_ref = self._get_id_from_item_desc(text_of_selected_item)

                if agent_id_ref:
                    # item has a parent and is a contract or single agent
                    non_agent_root_item = self.currentItem()
                    print(non_agent_root_item)

                    if not self.currentItem().text(0).__contains__(
                            "("):  # use display id to check if item is a contract

                        self.agent_deletion_requested.emit(int(agent_id_ref))

                        return

                    self.process_contract_deletion(
                        text_of_selected_item, non_agent_root_item, agent_id_ref
                    )

                    return
