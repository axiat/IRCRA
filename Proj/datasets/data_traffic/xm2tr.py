import os
import os.path
import xml.etree.ElementTree as ET
import glob


def xml_to_txt(xmlpath,txtpath):

    os.chdir(xmlpath)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')
    file_save = '/'+'train' + '.txt'
    file_txt = os.path.join(txtpath, file_save)
    f_w = open(file_txt, 'w')

    for i,file in enumerate(annotations):

        in_file = open(file)
        tree=ET.parse(in_file)
        root = tree.getroot()

        L= ''
        filename = root.find('filename').text

        for obj in root.iter('object'):
                name = obj.find('name').text

                class_num = class_names.index(name)

                xmlbox = obj.find('bndbox')

                x1 = xmlbox.find('xmin').text
                x2 = xmlbox.find('xmax').text
                y1 = xmlbox.find('ymin').text
                y2 = xmlbox.find('ymax').text
                L+=x1+','+y1+','+x2+','+y2+','+str(class_num)+' '
        f_w.write(filename+' '+L+'\n')

if __name__ == "__main__":
    class_names = ['person','hat']
    xmlpath = '/home/qin/SeniorA/PracticeA/IRCRA/Proj/datasets/data_traffic/data/labels/xml'
    txtpath = '/home/qin/SeniorA/PracticeA/IRCRA/Proj/datasets/data_traffic/data/labels/train'
    xml_to_txt(xmlpath,txtpath)

