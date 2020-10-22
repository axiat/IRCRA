from PyQt5.QtCore import QThread
import cv2
import numpy as np


class WtrafficDev(QThread):
    def __init__(self, dev_id):
        super(WtrafficDev, self).__init__()
        self.dev_id = dev_id
        self.dev = cv2.VideoCapture(self.dev_id, cv2.CAP_DSHOW)
        self.dev.open(self.dev_id, cv2.CAP_DSHOW)

    def run(self):
        while True:
            # 视频捕捉与处理
            _, img = self.dev.read()
            #处理
            #...
            #发送信号
            # 暂停, 符合人眼视觉习惯
            QThread.usleep(1000000)
