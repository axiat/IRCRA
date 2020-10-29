# @Time : 2020/10/21 8:14

# @Author : xx

# @File : trafficjson2txt.py

# @Software: PyCharm

# @description=''

import os
import json
import numpy as np
tagdict = {'CrossWalk': '0', ' Person': '1',
           ' Car': '2', ' RedLight': '3', ' GreenLight': '4'}
root = os.path.dirname(__file__)
dataroot = root + '/data/labels/json'
if not os.path.exists(dataroot):
    os.makedirs(dataroot)
sub_dir = os.listdir(
    '/home/qin/SeniorA/PracticeA/IRCRA/Proj/datasets/data_traffic/data/labels/json')
save_dir = os.path.join(root, 'out', 'traffic_label')


def generatetxt():
    with open('shape.txt', 'w') as sf:

        for each in sub_dir:

            jsonsdir = os.listdir(dataroot)
            for js_file in jsonsdir:
                js_file_path = os.path.join(dataroot, js_file)
                # print(js_file_path)
                with open(js_file_path, encoding='utf-8') as f:
                    # 创建txt文件
                    save_name = os.path.join(
                        save_dir, js_file.split('.')[0] + '.txt')
                    with open(save_name, 'w') as ftxt:

                        txtcontent = f.read()
                        txtcontent = json.loads(txtcontent)

                        if not txtcontent['outputs']:
                            continue
                        w = txtcontent['size']['width']
                        h = txtcontent['size']['height']
                        sf.write(str(w)+' '+str(h)+'\n')
                        # print(w, h)
                        bboxes = txtcontent['outputs']['object']
                        # print(txtcontent)
                        for b in bboxes:
                            tag = tagdict[b['name']]
                            try:
                                xmin, ymin, xmax, ymax = b['bndbox']['xmin'], b['bndbox']['ymin'], b['bndbox']['xmax'], \
                                    b['bndbox']['ymax']
                            except:
                                print(b)
                            # 防止出格
                            xmin = xmin if 0 <= xmin else 0
                            xmax = xmax if xmax <= w else w
                            ymin = ymin if 0 <= ymin else 0
                            ymax = ymax if ymax <= h else h
                            # print(xmin,xmax,ymin,ymax)
                            # 中心x,y
                            x_ = '%.6f' % ((xmin+xmax) / 2 / w)
                            y_ = '%.6f' % ((ymin+ymax) / 2 / h)
                            delta_x = '%.6f' % ((xmax - xmin) / w)
                            delta_y = '%.6f' % ((ymax - ymin) / h)
                            # print(js_file)
                            # print(xmin, ymin, xmax, ymax)
                            # print(x_, y_, delta_x, delta_y, tag)
                            ftxt.write(
                                tag + ' ' + str(x_) + ' ' + str(y_) + ' ' + str(delta_x) + ' ' + str(delta_y) + ' ' + '\n')


def generate_trainlist():
    srcroot = 'data_traffic/data/images/train'
    files = os.listdir(
        r'/home/qin/SeniorA/PracticeA/IRCRA/Proj/datasets/data_traffic/data/images/train_157-176')
    with open('train.txt', 'w') as f:
        for each in files:
            f.write(srcroot+'/'+each+'\n')


if __name__ == '__main__':
    generatetxt()
    # generate_trainlist()
