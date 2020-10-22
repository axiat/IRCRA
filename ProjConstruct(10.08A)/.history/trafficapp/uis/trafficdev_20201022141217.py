from PyQt5.QtCore import QThread
import cv2
import numpy as np


class WtrafficDev(QThread):
    def __init__(self):
        super(WtrafficDev, self).__init__()
        self.dev_id = 
        self.dev = cv2.VideoCapture()
        self.dev.open()

    def run(self):
        while True:
            # 视频捕捉与处理
            pass
