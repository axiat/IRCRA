from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import numpy as np

class WTrafficDev(QThread):
    sign_video = pyqtSignal(bytes, int, int, int, int)
    def __init__(self, th_id, dev_id):
        super(WTrafficDev, self).__init__()
        self.dev_id = dev_id
        self.th_id = th_id
        self.dev = cv2.VideoCapture(self.dev_id)
        self.dev.open(self.dev_id)
    
    def run(self):
        while True:
            # 视频捕捉
            reval, img = self.dev.read()
            if not reval:
                break
            # 处理
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # 发送信号
            data = img.tobytes()
            h, w, c = img.shape
            self.sign_video.emit(data, h, w, c, self.th_id)
            # 暂停，复合人眼的视觉习惯
            QThread.usleep(100000)
            

