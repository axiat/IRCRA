from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import numpy as np
from trafficapp.aicv.imgshandle import *
from yolotr.detector import TrafficDetector


class WTrafficDev(QThread):
    sign_video = pyqtSignal(bytes, int, int, int, int, bytes)

    def __init__(self, th_id, dev_id):
        super(WTrafficDev, self).__init__()
        self.dev_id = dev_id
        self.th_id = th_id
        self.dev = cv2.VideoCapture(self.dev_id)
        self.dev.open(self.dev_id)
        self.handle_type = 0
        self.brightness = 127

        self.detector = TrafficDetector()

    def recv_handle(self, h_type):
        self.handle_type = h_type
        # print("接收信号:",self.handle_type)

    def recv_brightness(self, brightness):
        self.brightness = brightness
        # print("接收信号:",self.handle_type)

    def run(self):
        while True:
            # 视频捕捉
            reval, img = self.dev.read()
            if not reval:
                self.dev.open(self.dev_id)
                break
            # 处理
            # AI侦测并标注处理
            img, result = self.detector.detect_mark(img)
            # 亮度处理
            toBright(img,self.brightness)
            # 图像基础处理
            if self.handle_type == 0:
                # 不做任何处理,原始视频图像
                pass
            elif self.handle_type == 1:
                # print("处理灰度图像")
                img = toGray(img)
            elif self.handle_type == 2:
                # print("模糊处理")
                img = toBlur(img)
            elif self.handle_type == 3:
                # print("线条处理")
                img = toLine(img)

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # 发送信号
            data = img.tobytes()
            imgT = timeImg(img)
            dataT = imgT.tobytes()
            h, w, c = img.shape
            self.sign_video.emit(data, h, w, c, self.th_id, dataT)
            # 暂停，复合人眼的视觉习惯
            QThread.usleep(100000)
