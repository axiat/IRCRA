from PyQt5.QtWidgets import QDialog
from trafficapp.uis.trafficui import Ui_Traffic


class WTrafficDialog(QDialog):
    def __init__(self):
        super(WTrafficDialog, self).__init__()
        self.ui = Ui_Traffic()
        self.ui.setupUi(self)

    # 其他交互与逻辑处理
    def handle_video(self):
        pass

    def modify_bright(self,val):
        print("")