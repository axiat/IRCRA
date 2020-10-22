from PyQt5.QtWidgets import QDialog

class WTrafficVideoDialog(QDialog):
    def __init__(self, parent=None):
        super(WTrafficVideoDialog,self).__init__(parent)
        #窗体要加self 否则会释放掉
