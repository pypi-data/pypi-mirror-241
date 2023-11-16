from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QFont


class QFameBoldLabel(QLabel):
    """A QLabel with bold font"""

    def __init__(self, text: str, font_size=10, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setText(text)
        font = self.font()
        font.setPointSize(font_size)
        font.setBold(True)
        self.setFont(font)


class DescriptionLabel(QLabel):
    """A QLabel with italic font for descriptions"""

    def __init__(self, text: str, font_size=10, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setText(text)
        font = self.font()
        font.setPointSize(font_size)
        font.setItalic(True)
        self.setFont(font)
