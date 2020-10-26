Hi!

This is the documentation of my recent program IRCRA, which stands for Intelligent Road Condition Report Application. The application implements the automatic detection of traffic violation/traffic volume and restore captured pictures in a mysql database. The program is directed by Prof. Qiang, Yang.

    While running my project, please note that the root directory is IRCRA/Proj instead of IRCRA(while importing python module)

This doc also serves as a lovely diary:)

[2020-10-21 Morning] (In A302, School of computer science, WHU)

Uploaded Design(Draft, UML)

![微信图片_20201021094422.jpg](https://i.loli.net/2020/10/21/BJjF6GClcbknydI.jpg)

[2020-10-21 Afternoon] Established program structure

[2020-10-22 Morning] Built User Interface

[2020-10-22 Afternoon] Finished UI, Collected Data

[2020-10-23 Morning] Preprocessed Data (see datasets/xqnfaces, using colabeler, bash files& python) jpg->xml->txt

[2020-10-23 Afternoon] Training model(detect/classify, using YOLOv4)
![IMG_20201023_151633.jpg](https://i.loli.net/2020/10/23/f8cFIDQijrzSHko.jpg)

training: enter IRCRA/Proj/faceDetect+Classify, run ./run_td_train_facesv2.sh (on Linux)
testing: enter IRCRA/Proj/faceDetect+Classify/yolov4_1025/yolov4, run ./run_detect.sh
