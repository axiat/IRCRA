from yolo.models import *  # set ONNX_EXPORT in models.py
from yolo.utils.datasets import *
from yolo.utils.utils import *
import torch
import os 


current_path = os.path.dirname(__file__)

class YOLOv4Detector:
    def __init__(self, 
                img_size=640, 
                cfg_file="yolov4-tiny.cfg", 
                weights="best.pt", 
                names="faces.names"):
        self.img_size = img_size
        self.cfg_file = os.path.join(current_path, F"data/{cfg_file}")
        self.weights = os.path.join(current_path, F"data/{weights}")
        self.names = os.path.join(current_path, F"data/{names}")
        # ------------ 模型准备
        # 构建模型
        self.model = Darknet(self.cfg_file, self.img_size)
        # 加载预训练模型
        self.model.load_state_dict(torch.load(self.weights)['model'])
        # 因为模型中使用了BatchNorm，Dropout等操作，预测的时候需要调用eval屏蔽
        self.model.eval()
        # ------------ 识别类型名
        # 加载类别
        self.names = load_classes(self.names)

    def detect(self, img0):
        """
            img0:原始图像，指的是图像的原始大小
        """
        img = self.format_img(img0)
        # 计算侦测结果
        pred = self.model(img, augment=False)[0]
        # 进行最大化抑制
        pred = non_max_suppression(pred, 0.3, 0.2, merge=False, classes=None, agnostic=False)
        
        # 解析识别结果
        for det in pred:
            if det is not None and len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()
        return pred  # 总长6：目标位置与大小（0:3），目标概率(4)，目标类别[5]

    def get_name(self, idx):
        return self.names[idx]

    def format_img(self, img0):
        img = letterbox(img0, new_shape=self.img_size)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img)
        img = img.float()
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        return img
    
    def detect_file(self, img_file):
        """ 
            img_file:图像文件
        """
        pass
    
    def detect_mark(self, img0):
        """
            返回标注目标的图像
        """
        pass

    def detect_mark_file(self, img_file):
        """
            输入的是图像文件
            返回标注目标的图像
        """
        pass

    def load_image(self, img_file):
        img0 = cv2.imread(img_file)  # BGR
        return img0



