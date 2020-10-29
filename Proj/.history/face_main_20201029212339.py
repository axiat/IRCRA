from yolo.detector import YOLOv4Detector
if __name__ == "__main__":
    detector = YOLOv4Detector(weights="best.pt")
    # img = detector.load_image("/home/qin/SeniorA/PracticeA/IRCRA/saved/1027/04traffic/04traffic/imgs/2020-10-27-130538.jpg")
    # img = detector.load_image("dd.jpg")
    reval, img = cv2.VideoCapture(0).read()
    result = detector.detect(img)[0][0] # [0][0]  # 总长6：目标位置与大小（0:3），目标概率(4)，目标类别[5]
    print(result)
    rect = result[0:4].detach().numpy()
    prob = result[4].detach().item()
    clss = int(result[5].detach().item())
    cls_name = detector.get_name(clss)
    print("侦测结果: ", rect, "，概率：", prob, ",类别:", clss, "类别名：", cls_name)