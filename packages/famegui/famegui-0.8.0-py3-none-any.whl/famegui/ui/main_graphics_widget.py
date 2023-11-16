import PySide2
from PySide2 import QtCore
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import QGraphicsView


class MainGraphicsWidget(QGraphicsView):
    unselect_contracts = QtCore.Signal(name="unselect_contracts")
    agent_deletion_requested = QtCore.Signal(object)

    def __init__(self, parent=None):
        super(MainGraphicsWidget, self).__init__(parent)
        self.startPos = None

    def _get_local_widget_position(self) -> QPoint:
        """transforms the global mouse position to the local widget position"""
        mouse_position = QCursor.pos()
        local_position = self.mapFromGlobal(mouse_position)
        return local_position

    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None:
        """triggers agent deletion when delete key is pressed"""
        key = event.key()
        if key == Qt.Key_Delete:
            self.agent_deletion_requested.emit(self._get_local_widget_position())
        super().keyPressEvent(event)

    def mousePressEvent(self, event):
        """event handler for remounting the scene origin point int the canvas"""
        self.unselect_contracts.emit()
        if event.modifiers() & Qt.ShiftModifier and event.button() == Qt.LeftButton:
            self.startPos = event.pos()
        else:
            super(MainGraphicsWidget, self).mousePressEvent(event)

    def wheelEvent(self, event: PySide2.QtGui.QWheelEvent) -> None:
        """prevent from unwanted movement/ side effects when scrolling with"""
        if event.modifiers() & Qt.ShiftModifier:  # bitwise comparison necessary, due to the fact that multiple
            # modifiers can be pressed at the same time
            return
        super().wheelEvent(event)

    def mouseMoveEvent(self, event):
        """compute the difference between the current cursor position and the
        previous saved origin point"""
        if self.startPos is not None:
            delta = self.startPos - event.pos()
            transform = self.transform()
            deltaX = delta.x() / transform.m11()
            deltaY = delta.y() / transform.m22()
            self.setSceneRect(self.sceneRect().translated(deltaX, deltaY))
            self.startPos = event.pos()
        else:
            super(MainGraphicsWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """resets the alternative origin point"""
        self.startPos = None
        super(MainGraphicsWidget, self).mouseReleaseEvent(event)
