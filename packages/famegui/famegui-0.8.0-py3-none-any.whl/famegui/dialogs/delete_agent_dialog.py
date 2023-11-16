# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_agent_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DeleteAgentDialog(object):
    def setupUi(self, DeleteAgentDialog):
        if not DeleteAgentDialog.objectName():
            DeleteAgentDialog.setObjectName("DeleteAgentDialog")
        DeleteAgentDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(DeleteAgentDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QTreeWidget(DeleteAgentDialog)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, "1")
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName("treeWidget")

        self.verticalLayout.addWidget(self.treeWidget)

        self.checkBoxDeleteAgent = QCheckBox(DeleteAgentDialog)
        self.checkBoxDeleteAgent.setObjectName("checkBoxDeleteAgent")
        self.checkBoxDeleteAgent.setText("Delete all related Contracts")

        self.verticalLayout.addWidget(self.checkBoxDeleteAgent)

        self.checkBoxDeleteAllContracts = QCheckBox(DeleteAgentDialog)
        self.checkBoxDeleteAllContracts.setObjectName("checkBoxDeleteAllContracts")
        self.checkBoxDeleteAllContracts.setText("Delete all related Contracts")

        self.verticalLayout.addWidget(self.checkBoxDeleteAllContracts)

        self.checkBoxDeleteAllConnectedAgents = QCheckBox(DeleteAgentDialog)
        self.checkBoxDeleteAllConnectedAgents.setObjectName("checkBoxDeleteAllConnectedAgents")
        self.checkBoxDeleteAllConnectedAgents.setText("Delete all related Agents")

        self.verticalLayout.addWidget(self.checkBoxDeleteAllConnectedAgents)

        self.retranslateUi(DeleteAgentDialog)

        QMetaObject.connectSlotsByName(DeleteAgentDialog)

    # setupUi

    def retranslateUi(self, DeleteAgentDialog):
        DeleteAgentDialog.setWindowTitle(QCoreApplication.translate("DeleteAgentDialog", "Delete Agent Dialog", None))

    # retranslateUi
