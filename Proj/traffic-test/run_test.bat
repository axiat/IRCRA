python test.py  ^
--data traffics/traffics.data ^
--cfg cfg/yolov4-tiny.cfg ^
--weights weights/last.pt ^
--img 640 ^
--iou-thr 0.6 ^
--conf-thres 0.5 ^
--batch-size 1