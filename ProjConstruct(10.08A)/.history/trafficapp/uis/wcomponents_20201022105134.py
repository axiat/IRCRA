from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal

class WLabel(QLabel):
    def __init__(self, str, parent=None, flags=Qt.WindowFlags()):
        super().__init__(str, parent=parent, flags=flags)

    def mouseReleaseEvent(self, ):
       self.clicked.emit() 