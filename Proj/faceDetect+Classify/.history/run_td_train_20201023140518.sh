python train.py \
--epochs 300  \
--batch-size 4 \
--data facesv2/faces.data \
--cfg cfg/yolov4-tiny.cfg \
--weights weights/yolov4-tiny.pt \
--name facesv2 \
--img 640 640 640
