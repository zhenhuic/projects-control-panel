from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, QPoint


class ClickableLabel(QLabel):
    clicked = pyqtSignal(bool)
    released = pyqtSignal(bool)
    moved = pyqtSignal(tuple)

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setMouseTracking(True)

    def mousePressEvent(self, mouse_event):
        self.clicked.emit(True)

    def mouseReleaseEvent(self, mouse_event):
        self.released.emit(True)

    def mouseMoveEvent(self, mouse_event):
        self.moved.emit((mouse_event.x(), mouse_event.y()))

