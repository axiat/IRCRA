from PyQt5.QtWidgets import QDialog
from trafficframe.uis.trafficui import Ui_Traffic

class WTrafficeDialog(QDialog):
    def __init__(self):
        super(WTrafficeDialog,self).__init__()
        self.ui = Ui_Traffic()
        self.ui.setupUi(self)

    # 其他交互与罗技处理