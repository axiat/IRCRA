from PyQt5.QtWidgets import QDialog
from trafficapp.uis.trafficui import Ui_Traffic
from trafficapp.uis.trafficdev import WTrafficDev
from PyQt5.QtGui import QImage, QPixmap
from trafficapp.uis.trafficvideoframe import WTrafficVideoDialog


class WTrafficDialog(QDialog):
    def __init__(self):
        super(WTrafficDialog, self).__init__()
        self.main_id = 1
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
        # 创建线程
        self.th_1 = WTrafficDev(1, 0)
        self.th_2 = WTrafficDev(2, "交通视频.mp4")
        self.th_3 = WTrafficDev(3, "交通视频.mp4")
        self.th_4 = WTrafficDev(4, "交通视频.mp4")
        self.th_5 = WTrafficDev(5, "交通视频.mp4")
        self.th_6 = WTrafficDev(6, "交通视频.mp4")
        self.th_7 = WTrafficDev(7, "交通视频.mp4")
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

        if th_id == 2:
            self.show_video_in_label(self.ui.lbl_video_2, qpixmap)
            if self.main_id == 2:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)

        if th_id == 3:
            self.show_video_in_label(self.ui.lbl_video_3, qpixmap)
            if self.main_id == 3:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)

        if th_id == 4:
            self.show_video_in_label(self.ui.lbl_video_4, qpixmap)
            if self.main_id == 4:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)

        if th_id == 5:
            self.show_video_in_label(self.ui.lbl_video_5, qpixmap)
            if self.main_id == 5:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)

        if th_id == 6:
            self.show_video_in_label(self.ui.lbl_video_6, qpixmap)
            if self.main_id == 6:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)

        if th_id == 7:
            self.show_video_in_label(self.ui.lbl_video_7, qpixmap)
            if self.main_id == 7:
                self.show_video_in_label(self.ui.lbl_video_main, qpixmap)

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
        # 1. 创建一个主窗f
        print("创建窗体")
        self.main_video_dlg = QDialog(self) #非模式对话框
        # self.main_video_dlg.setModel(False)
        # self.main_video_dlg.setWindowTitle("大视频")
        # 2. 进入窗体的消息训练
        self.main_video_dlg.exec()
        # 3. 释放窗体
        print("窗体关闭")
        self.main_video_dlg.destroy()
        self.main_video_dlg = None

    def closeEvent(self,e):
        self.th_1.terminate()
        self.th_2.terminate()
        self.th_3.terminate()
        self.th_4.terminate()
        self.th_5.terminate()
        self.th_6.terminate()
        self.th_7.terminate()
        # self.th_1.destroy()
        # self.th_2.destroy()
        # self.th_3.destroy()
        # self.th_4.destroy()
        # self.th_5.destroy()
        # self.th_6.destroy()
        # self.th_7.destroy()