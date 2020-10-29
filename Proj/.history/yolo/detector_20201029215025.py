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
        self.CUDA = torch.cuda.is_available()
        if self.CUDA:
            self.model.cuda()
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
        if self.CUDA:
            img = img.cuda()
        # 计算侦测结果
        pred = self.model(img, augment=False)[0]
        pred = pred.cpu()
        # 进行最大化抑制
        pred = non_max_suppression(pred, 0.4, 0.2, merge=False, classes=None, agnostic=False)

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

    def detect_mark(self, img0):
        pred = self.detect(img0)[0]
        if pred is not None:
            result = pred[0]
            print(result)
            # 侦测到目标，然后解析其中数据
            x1, y1, x2, y2 = result[0:4].detach().numpy()
            prob = result[4].detach().item()
            clss = int( result[5].detach().item())
            cls_name = self.get_name(clss)
            print([x1, y1, x2, y2], prob, clss, cls_name)
            # 备注：这里可以做一个概率阈值过滤（登录成功，可以考虑使用计数规则）
            # 标注
            img0 = cv2.rectangle(img0, (x1,y1),(x2,y2), color=(0, 0, 255), thickness=2)
            return img0, cls_name
        else:
            # 没有侦测到目标，直接返回原图像
            return img0, None

    def load_image(self, img_file):
        img0 = cv2.imread(img_file)  # BGR
        return img0



