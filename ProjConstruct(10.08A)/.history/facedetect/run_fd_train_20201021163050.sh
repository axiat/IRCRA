python train.py \
--epochs 30  \
--batch-size 4 \
--data ../datasets/data_faced/faced.data \
--cfg cfg/yolov4-tiny.cfg \
--weights weights/best_yolov4-tiny-1.pt \
--name yolov4-tiny \
--img 640 640 640
