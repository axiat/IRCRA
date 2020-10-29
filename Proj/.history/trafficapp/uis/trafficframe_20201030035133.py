from PyQt5.QtWidgets import QDialog
from trafficapp.uis.trafficui import Ui_Traffic
from trafficapp.uis.trafficdev import WTrafficDev
from PyQt5.QtGui import QImage, QPixmap
from trafficapp.uis.trafficvideoframe import WTrafficVideoDialog
from PyQt5.QtCore import QUrl
from trafficapp.biz.map import GetMapUrl
from PyQt5.QtCore import pyqtSignal


class WTrafficDialog(QDialog):
    # int传递图像的处理方式0:原图,1:灰色,2:高斯模糊,3:线条处理
    signal_handle = pyqtSignal(int)

    def __init__(self):
        super(WTrafficDialog, self).__init__()
        self.main_id = 1
        self.is_sub_dialog = False
        self.ui = Ui_Traffic()
        self.ui.setupUi(self)
        self.ui.lbl_video_1.clicked.connect(self.switch_video1_main)
        self.ui.lbl_video_2.clicked.connect(self.switch_video2_main)
        self.ui.lbl_video_3.clicked.connect(self.switch_video3_main)
        self.ui.lbl_video_4.clicked.connect(self.switch_video4_main)
        self.ui.lbl_video_5.clicked.connect(self.switch_video5_main)
        self.ui.lbl_video_6.clicked.connect(self.switch_video6_main)
        self.ui.lbl_video_7.clicked.connect(self.switch_video7_main)
        self.ui.lbl_video_main.clicked.connect(self.show_main_video)

    def init_dev(self):
        # 加载地图(可优化)
        map_url = GetMapUrl()
        self.ui.wdt_map.load(QUrl(map_url))
        # 创建线程
        self.th_1 = WTrafficDev(1, 0)
        self.th_2 = WTrafficDev(2, "交通视频.mp4")
        self.th_3 = WTrafficDev(3, "街口1.mp4")
        self.th_4 = WTrafficDev(4, "街口2.mp4")
        self.th_5 = WTrafficDev(5, "街口3.mp4")
        self.th_6 = WTrafficDev(6, "街口4.mp4")
        self.th_7 = WTrafficDev(7, "交通视频.mp4")
        # 绑定图像处理信号到视频抓取模块
        self.signal_handle.connect(self.th_1.recv_handle)
        self.signal_handle.connect(self.th_2.recv_handle)
        self.signal_handle.connect(self.th_3.recv_handle)
        self.signal_handle.connect(self.th_4.recv_handle)
        self.signal_handle.connect(self.th_5.recv_handle)
        self.signal_handle.connect(self.th_6.recv_handle)
        self.signal_handle.connect(self.th_7.recv_handle)
        # 绑定视频槽函数
        self.th_1.sign_video.connect(self.show_video)
        self.th_2.sign_video.connect(self.show_video)
        self.th_3.sign_video.connect(self.show_video)
        self.th_4.sign_video.connect(self.show_video)
        self.th_5.sign_video.connect(self.show_video)
        self.th_6.sign_video.connect(self.show_video)
        self.th_7.sign_video.connect(self.show_video)

        # 启动线程
        self.th_1.start()
        self.th_2.start()
        self.th_3.start()
        self.th_4.start()
        self.th_5.start()
        self.th_6.start()
        self.th_7.start()

    # 其他交互与逻辑处理

    def show_video(self, data, h, w, c, th_id):
        qimg = QImage(data, w, h, w*c, QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimg)

        if th_id == 1:
            self.show_video_in_label(self.ui.lbl_video_1, qpixmap)
            if self.main_id == 1:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(
                        self.main_video_dlg.ui.lbl_video, qpixmap)

        if th_id == 2:
            self.show_video_in_label(self.ui.lbl_video_2, qpixmap)
            if self.main_id == 2:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(
                        self.main_video_dlg.ui.lbl_video, qpixmap)

        if th_id == 3:
            self.show_video_in_label(self.ui.lbl_video_3, qpixmap)
            if self.main_id == 3:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(
                        self.main_video_dlg.ui.lbl_video, qpixmap)

        if th_id == 4:
            self.show_video_in_label(self.ui.lbl_video_4, qpixmap)
            if self.main_id == 4:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(
                        self.main_video_dlg.ui.lbl_video, qpixmap)

        if th_id == 5:
            self.show_video_in_label(self.ui.lbl_video_5, qpixmap)
            if self.main_id == 5:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(
                        self.main_video_dlg.ui.lbl_video, qpixmap)

        if th_id == 6:
            self.show_video_in_label(self.ui.lbl_video_6, qpixmap)
            if self.main_id == 6:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(
                        self.main_video_dlg.ui.lbl_video, qpixmap)

        if th_id == 7:
            self.show_video_in_label(self.ui.lbl_video_7, qpixmap)
            if self.main_id == 7:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(
                        self.main_video_dlg.ui.lbl_video, qpixmap)

    def show_video_in_label(self, component, img):
        component.setPixmap(img)
        component.setScaledContents(True)

    def switch_video1_main(self):
        # 记录点击的标签
        self.main_id = 1
        # 显示视频，做个逻辑判定，并显示在主区

    def switch_video2_main(self):
        self.main_id = 2

    def switch_video3_main(self):
        self.main_id = 3

    def switch_video4_main(self):
        self.main_id = 4

    def switch_video5_main(self):
        self.main_id = 5

    def switch_video6_main(self):
        self.main_id = 6

    def switch_video7_main(self):
        self.main_id = 7

    def handle_video(self, btn_id):
        """
            实际得图像得处理，从设计结构上讲，都交给视频抓取模块再抓取后处理
             1. 发送一个信号给视频抓取模块（信号指定一个处理方式的参数）
                |- 定义信息
                |- 绑定信号
             2. 视频抓取类定义一个变量存储处理方式，并根据处理方式处理图像
                |- 绑定接受信号
                |- 根据信号的图像处理方式处理图像
                |- （再使用信号发送给窗体显示）
        """
        print("打开的按钮id：", btn_id)
        if btn_id == 100:
            pass
        if btn_id == 101:
            pass
        if btn_id == 102:
            pass
        if btn_id == 103:
            pass

    def modify_bright(self, val):
        print("调整亮度值：", val)

    # 主显示区弹窗显示监控视频
    def show_main_video(self):
        # 1. 创建一个窗体
        self.main_video_dlg = WTrafficVideoDialog(self)  # 非模式对话框
        # 设置一个标记
        self.is_sub_dialog = True

        # 2. 进入窗体的消息训练
        # self.main_video_dlg.setModal(False)
        # self.main_video_dlg.show()
        self.main_video_dlg.exec()
        # 3. 释放窗体
        self.is_sub_dialog = False
        self.main_video_dlg.destroy()
        self.main_video_dlg = None

    def closeEvent(self, e):
        self.th_1.terminate()
        self.th_2.terminate()
        self.th_3.terminate()
        self.th_4.terminate()
        self.th_5.terminate()
        self.th_6.terminate()
        self.th_7.terminate()
