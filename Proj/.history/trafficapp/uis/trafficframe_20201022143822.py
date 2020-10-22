from PyQt5.QtWidgets import QDialog
from trafficapp.uis.trafficui import Ui_Traffic
from trafficapp.uis.trafficdev import WTrafficDev
from PyQt5.QtGui import QPixmap,QImage


class WTrafficDialog(QDialog):
    def __init__(self):
        super(WTrafficDialog, self).__init__()
        self.ui = Ui_Traffic()
        self.ui.setupUi(self)
        self.ui.lbl_video_1.clicked.connect(self.switch_video1_main)
        self.ui.lbl_video_2.clicked.connect(self.switch_video2_main)
        self.ui.lbl_video_3.clicked.connect(self.switch_video3_main)
        self.ui.lbl_video_4.clicked.connect(self.switch_video4_main)
        self.ui.lbl_video_5.clicked.connect(self.switch_video5_main)
        self.ui.lbl_video_6.clicked.connect(self.switch_video6_main)
        self.ui.lbl_video_7.clicked.connect(self.switch_video7_main)
        # 创建线程
        self.th_1 = WTrafficDev(1, 0)
        self.th_2 = WTrafficDev(2, "交通视频.mp4")
        # 绑定线程槽函数
        self.th_1.sign_video.connect(self.show_video)
        self.th_2.sign_video.connect(self.show_video)
        # 启动线程
        self.th_1.start()
        self.th_2.start()

    # 其他交互与逻辑处理
    def show_video(self, data, w, h, c, th_id):
        if th_id == 1:
            self.show_video_in_label(self.ui.lbl_video_1,QPixmap)
        if th_id == 2:
            self.show_video_in_label(self.ui.lbl_video_2,QPixmap)

    def show_video_in_label(self, component, img):
        component.setPixmap(img)
        component.setScaleContents(True)

    def switch_video1_main(self):
        print("切换1接口的视频")

    def switch_video2_main(self):
        print("切换2接口的视频")

    def switch_video3_main(self):
        print("切换3接口的视频")

    def switch_video4_main(self):
        print("切换4接口的视频")

    def switch_video5_main(self):
        print("切换5接口的视频")

    def switch_video6_main(self):
        print("切换6接口的视频")

    def switch_video7_main(self):
        print("切换7接口的视频")

    def handle_video(self, btn_id):
        print("打开的按钮id: ", btn_id)
        if btn_id == 100:
            pass
        if btn_id == 101:
            pass
        if btn_id == 102:
            pass
        if btn_id == 103:
            pass

    def modify_bright(self, val):
        print("调整亮度值: ", val)
