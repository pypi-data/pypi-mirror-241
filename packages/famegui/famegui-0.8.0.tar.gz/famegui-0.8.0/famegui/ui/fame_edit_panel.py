from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget


def get_list_widget_holder():
    """
    Create and return a QWidget containing a QListWidget, an input field, and buttons to add/remove items.
    """

    holder = QWidget()
    layout = QVBoxLayout()
    lineEdit = QLineEdit(holder)

    layout.addWidget(lineEdit)

    addButton = QPushButton("Add", holder)
    layout.addWidget(addButton)

    listWidget = QListWidget(holder)
    layout.addWidget(listWidget)

    removeButton = QPushButton("Remove Selected", holder)
    layout.addWidget(removeButton)

    holder.setLayout(layout)

    return holder
