from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal

class WLabel(QLabel):
    def __init__(self, str, parent=None):
        super().__init__(str, parent=parent)

    def mouseReleaseEvent(self, e):
       self.clicked.emit() 