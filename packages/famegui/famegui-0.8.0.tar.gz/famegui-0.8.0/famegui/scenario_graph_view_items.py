import typing

import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QBrush, QColor
from PySide2.QtWidgets import QGraphicsItem

import weakref
import math
import logging


class ContractGraphItem(QtWidgets.QGraphicsItem):
    """Graphical representation of a contract between two agents.
    Note: do not register listeners here, instead use -> scenario_graph_view.py"""

    Type = QGraphicsItem.UserType + 1
    _highlight = False
    _single_highlight = False

    def __init__(
        self, sourceNode, destNode
    ):  # sourceNode: AgentGraphItem (sender) , destNode: AgentGraphItem (receiver)
        QGraphicsItem.__init__(self)
        self.setAcceptedMouseButtons(QtCore.Qt.NoButton)
        self._arrow_size = 10.0
        self._draw_line = QtCore.QLineF()
        self.source = weakref.ref(sourceNode)
        self.dest = weakref.ref(destNode)
        self.source().addEdge(self)
        self.dest().addEdge(self)
        self.adjust()

    def type(self):
        """override QGraphicsItem.type()"""
        return ContractGraphItem.Type

    """-> AgentGraphItem:"""

    def sourceNode(self):
        return self.source()

    def setSourceNode(self, node):
        if node is None:
            self.source = None
            return
        self.source = weakref.ref(node)
        self.adjust()

    """-> AgentGraphItem:"""

    def destNode(self):
        return self.dest()

    def setDestNode(self, node):
        if node is None:
            self.dest = None
            return
        self.dest = weakref.ref(node)
        self.adjust()

    def set_highlight_mode(self, highlight_enabled):
        if not highlight_enabled:
            self._single_highlight = False
        self._highlight = highlight_enabled

    def set_single_highlight_mode(self, highlight_enabled):
        self._single_highlight = highlight_enabled

    def adjust(self):
        # reset drawing
        self._draw_line = QtCore.QLineF()
        if not self.source() or not self.dest():
            return
        radius = 50
        src_center = self.mapFromItem(self.source(), radius, radius)
        dest_center = self.mapFromItem(self.dest(), radius, radius)

        # compute the distance between the two items
        [src_x, src_y] = src_center.toTuple()
        [dest_x, dest_y] = dest_center.toTuple()
        distance = math.sqrt((src_x - dest_x) ** 2 + (src_y - dest_y) ** 2)
        if distance <= radius * 2:
            logging.warning("items are too close to draw a line")
            return
        distance_x = dest_x - src_x
        distance_y = dest_y - src_y

        offset_ratio = radius * 1.0 / distance
        offset_x = distance_x * offset_ratio
        offset_y = distance_y * offset_ratio

        centerOffset = QtCore.QPointF(offset_x, offset_y)

        self.prepareGeometryChange()
        line_start = src_center + centerOffset
        line_end = dest_center - centerOffset
        self._draw_line = QtCore.QLineF(line_start, line_end)

    def is_in_highlight_mode(self):
        return self._highlight

    def boundingRect(self):
        if not self.source() or not self.dest():
            return QtCore.QRectF()

        penWidth = 1
        extra = (penWidth + self._arrow_size) / 2.0
        size = QtCore.QSizeF(
            self._draw_line.x2() - self._draw_line.x1(),
            self._draw_line.y2() - self._draw_line.y1(),
        )
        return (
            QtCore.QRectF(self._draw_line.p1(), size)
            .normalized()
            .adjusted(-extra, -extra, extra, extra)
        )

    def paint(self, painter, option, widget):
        if not self.source() or not self.dest():
            return

        # Draw the line itself
        if self._draw_line.length() == 0.0:
            return

        color = QtCore.Qt.black
        pen_stroke = 2

        if self._highlight:
            color = QtGui.QColor("#ff1100")  # Red

        if self._single_highlight:
            pen_stroke = 5

        painter.setPen(
            QtGui.QPen(
                color,
                pen_stroke,
                QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap,
                QtCore.Qt.RoundJoin,
            )
        )
        painter.drawLine(self._draw_line)

        # Draw the arrows if there's enough room.
        angle = math.acos(self._draw_line.dx() / self._draw_line.length())
        if self._draw_line.dy() >= 0:
            angle = (2.0 * math.pi) - angle

        line_end = self._draw_line.p2()
        destArrowP1 = line_end + QtCore.QPointF(
            math.sin(angle - math.pi / 3) * self._arrow_size,
            math.cos(angle - math.pi / 3) * self._arrow_size,
        )
        destArrowP2 = line_end + QtCore.QPointF(
            math.sin(angle - math.pi + math.pi / 3) * self._arrow_size,
            math.cos(angle - math.pi + math.pi / 3) * self._arrow_size,
        )

        painter.setBrush(color)
        painter.drawPolygon(
            QtGui.QPolygonF([self._draw_line.p2(), destArrowP1, destArrowP2])
        )


class AgentGraphItem(QtWidgets.QGraphicsItem):
    """A Agent node in the graph."""

    Type = QGraphicsItem.UserType + 2

    def zValue(self) -> float:
        z_value = 100
        return z_value

    # use a lambda rather than a Qt signal because we don't inherit from QObject
    position_changed = lambda self, x, y: None

    def setSelected(self, selected: bool, sender: bool = True) -> None:
        self._in_receiver_mode = sender
        super().setSelected(selected)

    def __init__(self, agent_id, label, color):
        QGraphicsItem.__init__(self)
        # public
        self.edgeList = []
        # private / read only
        self._label = "#{}".format(agent_id)
        self._color = color
        self._radius = 50
        self._agent_id = agent_id
        self._links = []
        self._highlight_border = False
        self._in_receiver_mode = True
        # customize graphics item
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)

    def type(self):
        """override QGraphicsItem.type()"""
        return AgentGraphItem.Type

    def addEdge(self, edge):
        self.edgeList.append(weakref.ref(edge))
        edge.adjust()

    def set_border_highlight(self, highlight: bool):
        self._highlight_border = highlight

    @property
    def agent_id(self) -> int:
        return self._agent_id

    def add_link(self, link):
        self._links.append(link)

    def boundingRect(self):
        return QtCore.QRectF(0, 0, self._radius * 2, self._radius * 2)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for edge in self.edgeList:
                if not edge():
                    continue
                edge().adjust()
            self.position_changed(self.x(), self.y())
        return QGraphicsItem.itemChange(self, change, value)

    def paint(self, painter, option, widget=None):
        """Qt paint method"""
        # main rectangle with its border
        if option.state & QtWidgets.QStyle.State_Selected:
            background_color = QtGui.QColor(self._color).darker()
            border_color = QtGui.QColor("#ff009a")
            border_width = 3
        else:
            background_color = QtGui.QColor(self._color)
            border_color = QtGui.QColor(0, 0, 0)
            border_width = 2
        if not self._in_receiver_mode:
            background_color = QtGui.QColor(self._color).darker()
            border_color = QtGui.QColor("#40ff00")
            border_width = 3

        item_rect = self.boundingRect()

        painter.setBrush(QtGui.QBrush(background_color))
        painter.setPen(QtGui.QPen(border_color, border_width))
        painter.drawEllipse(item_rect)

        # label
        font = QtGui.QFont("Arial", 14)
        font.setStyleStrategy(QtGui.QFont.ForceOutline)
        painter.setFont(font)
        painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 1))
        painter.drawText(item_rect, QtCore.Qt.AlignCenter, self._label)
