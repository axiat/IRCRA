from PyQt5.QtWidgets import QApplication
from trafficapp.uis.trafficframe import WTrafficDialog


class WTrafficApp(QApplication):
    def __init__(self, Liststr=None):
        super(WTrafficApp, self).__init__(Liststr=Liststr)
        self.dlg = WTrafficDialog()
        self.dlg.show()
    # 可以增加应用程序的处理
