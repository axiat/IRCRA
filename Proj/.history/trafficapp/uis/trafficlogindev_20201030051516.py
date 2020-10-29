from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import numpy as np
from yolo.detector import YOLOv4Detector
from trafficapp.dao.users import UserDAO
from collections import Counter


class WTrafficLoginDev(QThread):
    sign_video = pyqtSignal(bytes, int, int, int, bool)

    def __init__(self, dev_id):
        super(WTrafficLoginDev, self).__init__()
        self.dev_id = dev_id
        self.dev = cv2.VideoCapture(self.dev_id)
        self.detector = YOLOv4Detector()
        self.dao = UserDAO()
        self.users = []
        self.counter = 0
        self.is_valid = False

    def run(self):
        while True:
            # 视频捕捉
            reval, img = self.dev.read()
            if not reval:
                self.dev.open(self.dev_id)
                continue
            # 识别
            # img = self.detector.detect_mark(img)
            img, username = self.detector.detect_mark(img.copy())
            # 技术100次，根据其中出现的最多数，来作为登录名
            if username is not None:
                self.users.append(username)
                self.counter += 1
            if self.counter >= 1:  # 大约一秒钟
                # 取出最多的用户名，并判定登录，登录成功，然后发送信号给登录窗体处理
                self.is_valid = True
                collected_users = Counter(self.users)
                login_user = collected_users.most_common(1)[0]
                login_user_name = login_user[0]
                login_user_times = login_user[1]
                print("作为", login_user_name, "登录")
                print("识别次数: ", login_user_times)
                self.counter = 0  # 重新计数
                self.users = []  # 业务规则，自行完成

            # 处理颜色通道
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # 发送信号
            data = img.tobytes()
            h, w, c = img.shape
            self.sign_video.emit(data, h, w, c, self.is_valid)
            # 暂停，复合人眼的视觉习惯
            QThread.usleep(100000)

    def close(self):
        self.terminate()
        while self.isRunning():
            pass
        self.dev.release()
        self.counter = 0
        self.is_valid = False
        self.dao = None  # 释放数据库
