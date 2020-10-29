import cv2
import numpy as np
import time
from PyQt5.QtGui import QImage
# def QImageToCvMat(self,incomingImage):
#     '''  Converts a QImage into an opencv MAT format  '''

#     incomingImage = incomingImage.convertToFormat(QtGui.QImage.Format_RGB888)

#     width = incomingImage.width()
#     height = incomingImage.height()

#     ptr = incomingImage.constBits()
#     arr = np.array(ptr).reshape(height, width, 4)  #  Copies the data
#     return arr


def QImageToCvMat(incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''

    incomingImage = incomingImage.convertToFormat(QImage.Format_RGB888)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(height * width * 4)
    arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
    return arr


def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def timeImg(img):
    # img1=np.asarray(img)
    # img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.putText(img, getTime(), (5, 30),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    # img = np.expand_dims(img1, axis=2).repeat(3, axis=2)5
    imgzi = cv2.putText(img, getTime(), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    return imgzi


def toGray(img):
    # 灰度处理
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 把灰度的2为图像转换为3为灰度图像（彩色）
    # img = img1[:, :, np.newaxis].repeat(dim=2)
    # cv2.putText(img1, getTime(), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    img = np.expand_dims(img1, axis=2).repeat(3, axis=2)
    # print("图像的维度", img.shape)
    return img


def toClear(img):
    return img


def toBright(img, brightness=127):
    return img


def toLine(img):
    return img
