from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import numpy as np


class WtrafficDev(QThread):
    sign_video = pyqtSignal(bytes, int, int, int, int)

    def __init__(self, th_id, dev_id):
        super(WtrafficDev, self).__init__()
        self.dev_id = dev_id
        self.th_id = th_id
        self.dev = cv2.VideoCapture(self.dev_id, cv2.CAP_DSHOW)
        self.dev.open(self.dev_id, cv2.CAP_DSHOW)

    def run(self):
        while True:
            # 视频捕捉与处理
            _, img = self.dev.read()
            # 处理
            # ...
            # 发送信号
            data = img.tobytes()
            h, w, c = img.shape
            self.sign_video.emit(data, h, w, c, self.th_id)  # 还应该传送线程id
            # 暂停, 符合人眼视觉习惯
            QThread.usleep(100000)
