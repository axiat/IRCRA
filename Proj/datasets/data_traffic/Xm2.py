import os
import re
import sys
import glob
import xml.etree.ElementTree as ET


def xml_to_txt(indir, outdir):

    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')
    pat = re.compile('(?<=\>).*?(?=\<)')

    for i, file in enumerate(annotations):
        file_save = file.split('.')[0]+'.txt'
        file_txt = os.path.join(outdir, file_save)
        f_w = open(file_txt, 'w', encoding="utf-8")

        tree = ET.parse(file)
        root = tree.getroot()

        for obj in root.iter('PostItem'):
            current = list()
            for ele in obj.iter():
                if "content" in ele.tag:
                    content = obj.find('content').text
                    if content:
                        content = re.sub(
                            r'</?\w+[^>]*>', '', content).replace("&nbsp;", " ").strip()
                        print(content)
                        f_w.write(content)
                        f_w.write("\n")
                if "caption" in ele.tag:
                    caption = obj.find('caption').text
                    if caption:
                        caption = re.sub(
                            r'</?\w+[^>]*>', '', caption).replace("&nbsp;", " ").strip()
                        f_w.write(caption)
                        f_w.write("\n")
                        print(caption)


indir = '/home/qin/SeniorA/PracticeA/IRCRA/Proj/datasets/data_traffic/data/labels/xml'
outdir = '/home/qin/SeniorA/PracticeA/IRCRA/Proj/datasets/data_traffic/data/labels/train'

if __name__ == "__main__":
    xml_to_txt(indir, outdir)
