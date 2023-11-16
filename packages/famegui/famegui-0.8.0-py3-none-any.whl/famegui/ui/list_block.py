from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QScrollArea, QFrame, QLabel, QHBoxLayout, QLineEdit
from famegui import models
from fameio.source.schema import AttributeSpecs

from famegui.config.style_config import REMOVE_BTN_STYLE, COLLAPSE_BTN_STYLE
from famegui.ui.fame_list_item import ListItem
from famegui.ui.fame_ui_elements import QFameBoldLabel


class CustomListWidget(QFrame):
    """Wrapper to enable the creation and management of a list of all types Input Panels."""
    row_creation_requested = QtCore.Signal(AttributeSpecs, QWidget)

    def __init__(
            self,
            widget_instance,
            attr_spec: AttributeSpecs,
            schema: models.Schema,
            attr_name: str,
            parent=None,
    ):
        super(CustomListWidget, self).__init__(parent)

        self.widget_instance = widget_instance
        self.attr_spec = attr_spec
        self.attr_name = attr_name
        self.schema: models.Schema = schema
        self.main_layout = QVBoxLayout(self)

        self.init_ui()

    def init_ui(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        # Add button to add new widgets
        self.add_button = QPushButton("Add", self)
        self.add_button.setFixedHeight(20)
        self.add_button.clicked.connect(self.add_widget_instance)

        # Add the button to the scroll layout
        self.scroll_layout.addWidget(QFameBoldLabel("LIST::"))
        self.scroll_layout.addWidget(self.add_button)

        # Add the scroll area to the main layout
        self.main_layout.addWidget(self.scroll_area)

        self.add_widget_instance()
        self.scroll_layout.addWidget(self.widget_instance)

        uniq_obj_name = f"customListWidgetNx-{id(self.scroll_content)}"

        self.scroll_content.setObjectName(uniq_obj_name)

        color_str = "rgba(134, 227, 206, 0.5)"

        stylesheet = f"#{uniq_obj_name} {{ border: 2px dashed grey; background-color: {color_str};  }}"

        self.scroll_content.setStyleSheet(stylesheet)
        self.setStyleSheet(stylesheet)

        self.setFixedHeight(int(self.height() * 1.2))

    def set_style(self, widget, style):
        """Sets the style of the given widget.

        Args:
          widget: The widget to set the style of.
          style: A dictionary of CSS properties and values.
        """

        for property, value in style.items():
            widget.setStyleSheet(f"{property}: {value};")

    def set_widget(self, widget_instance):
        card_wrapper_widget = ListItem(self.attr_name)
        card_wrapper_layout = card_wrapper_widget.layout()
        card_header_layout = QHBoxLayout()
        card_header_layout.addWidget(
            QFameBoldLabel(f"Block Nr.{self.scroll_layout.count() - 1}")
        )

        remove_btn = QPushButton("Remove", self)
        remove_btn.setStyleSheet(
            REMOVE_BTN_STYLE
        )
        collapse_btn = QPushButton("Collapse", self)

        collapse_btn.setStyleSheet(
            COLLAPSE_BTN_STYLE
        )

        remove_btn.setFixedHeight(30)
        remove_btn.clicked.connect(
            lambda: self.remove_widget_instance(card_wrapper_widget)
        )

        card_header_layout.addWidget(remove_btn)
        card_header = QWidget()
        card_header.setLayout(card_header_layout)
        collapse_btn.setFixedHeight(30)
        collapse_btn.clicked.connect(
            lambda: widget_instance.hide()
            if widget_instance.isVisible()
            else widget_instance.show()
        )

        card_wrapper_layout.addWidget(card_header)

        card_wrapper_widget.set_panel_widget(widget_instance)
        card_header_layout.addWidget(collapse_btn)

        uniq_widget = f"myUniqueWidget{id(card_wrapper_widget)}"
        card_wrapper_widget.setObjectName(uniq_widget)

        self.scroll_layout.addWidget(card_wrapper_widget)

        color_str = "rgba(190, 196, 254, 0.8)"

        card_header.setStyleSheet(
            f"background-color: {color_str}; border-radius: 8px; border: 2px dashed grey;"
        )

    def add_widget_instance(self):
        """Duplicate the initial list item and add it to the scroll layout."""

        if self.scroll_layout.count() == 0:
            card_wrapper_widget = ListItem(self.attr_name)

            new_widget = type(self.widget_instance)()
            new_widget: QWidget

            new_widget.setStyleSheet("background: rgb(255, 255, 49);")

            new_widget.setLayout(self.widget_instance.layout())

            card_wrapper_widget.set_panel_widget(new_widget)

            self.scroll_layout.addWidget(card_wrapper_widget)
            return
        self.row_creation_requested.emit(self.attr_spec, self)

    def remove_widget_instance(self, widget_instance):
        """Remove the given widget from list scroll layout."""
        widget_instance.deleteLater()
        self.scroll_layout.removeWidget(widget_instance)

    def _merge_data(self, data):
        """Merge input date recursively from nested input blocks to a single list of dicts."""

        merged_list = []

        for item in data:
            for key, value in item.items():
                if isinstance(value, list):
                    merged_dict = {}
                    for sub_item in value:
                        merged_dict.update(sub_item)
                    merged_list.append(merged_dict)
                elif isinstance(value, dict):
                    merged_list.extend(self._merge_data([value]))

        return merged_list

    def get_data(self):
        """Group and gather all the data from the input widget."""
        data = {}
        data_list = []

        widget_list = []
        for i in range(self.scroll_layout.count()):
            widget = self.scroll_layout.itemAt(i).widget()
            widget_list.append(widget)

            if widget:
                if widget.__class__.__name__ == "BlockItemWrapper":
                    data_list.append({str(self.attr_name): widget.get_data()})

                if isinstance(widget, QLineEdit):
                    data_list.append({str(self.attr_name): widget.get_data()})

                if widget.__class__.__name__ == "BlockTypeWrapper":
                    data_list.append({str(self.attr_name): widget.get_data()})
                    continue

                if widget.__class__.__name__ == "InputPanelWrapper":
                    data_list.append({str(self.attr_name): widget.get_data()})

                if isinstance(widget, ListItem):
                    widget: ListItem
                    data_list.append({str(self.attr_name): widget.get_data()})

                else:
                    pass

        data[self.attr_name] = data_list

        merged_data = self._merge_data(data_list)

        return merged_data
