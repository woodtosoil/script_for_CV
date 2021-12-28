import json
import os
import numpy as np
import codecs
from glob import glob
import cv2
import shutil
from sklearn.model_selection import train_test_split

saved_path = "D:/datasets/djw/BDD100K/bdd100k_labels/bdd100k/"
img_path = 'D:/datasets/djw/BDD100K/bdd100k_images/bdd100k/images/100k/val/'
json_path = 'D:/datasets/djw/BDD100K/bdd100k_labels/bdd100k/labels/100k/val/'

#2.创建要求文件夹
if not os.path.exists(saved_path + "Annotations"):
    os.makedirs(saved_path + "Annotations")
# if not os.path.exists(saved_path + "JPEGImages/"):
#     os.makedirs(saved_path + "JPEGImages/")
if not os.path.exists(saved_path + "ImageSets/Main/"):
    os.makedirs(saved_path + "ImageSets/Main/")

for jsons in os.listdir(json_path):
    

    with open(json_path+jsons, 'r') as load_f:
        data = json.load(load_f)  # data是一个列表
        for item in data:  # item是一个字典
            path_name = item['name']
            with codecs.open(saved_path + "Annotations/" + path_name[:-4] + ".xml", "w", "utf-8") as xml:
                path = img_path + str(path_name)
                print(path)
                height, width, channels = cv2.imread(path).shape
                # print(height, width, channels)
                xml.write('<annotation>\n')
                xml.write('\t<folder>' + 'UAV_data' + '</folder>\n')
                xml.write('\t<filename>' + path_name + '</filename>\n')
                xml.write('\t<source>\n')
                xml.write('\t\t<database>The UAV autolanding</database>\n')
                xml.write('\t\t<annotation>UAV AutoLanding</annotation>\n')
                xml.write('\t</source>\n')
                # xml.write('\t<owner>\n')
                # xml.write('\t\t<flickrid>NULL</flickrid>\n')
                # xml.write('\t\t<name>ChaojieZhu</name>\n')
                # xml.write('\t</owner>\n')
                xml.write('\t<size>\n')
                xml.write('\t\t<width>' + str(width) + '</width>\n')
                xml.write('\t\t<height>' + str(height) + '</height>\n')
                xml.write('\t\t<depth>' + str(channels) + '</depth>\n')
                xml.write('\t</size>\n')
                xml.write('\t\t<segmented>0</segmented>\n')

                comments = item['labels']  # 是一个列表
                for _item in comments:  # _item是一个一个的字典
                    # print(_item)
                    for _, x2 in enumerate(_item):
                        # print(x2, _item[x2])
                        if x2 == 'category' and _item[x2] != 'drivable area' and _item[x2] != 'lane':
                            xml.write('\t<object>\n')
                            xml.write('\t\t<name>' + _item[x2] + '</name>\n')
                            xml.write('\t\t<pose>Unspecified</pose>\n')
                            xml.write('\t\t<truncated>1</truncated>\n')
                            xml.write('\t\t<difficult>0</difficult>\n')

                        if x2 == 'box2d':
                            dic = _item[x2]
                            for _, j in enumerate(dic):
                                if j == 'x1':
                                    xmin = int(dic[j])
                                if j == 'y1':
                                    ymin = int(dic[j])
                                if j == 'x2':
                                    xmax = int(dic[j])
                                if j == 'y2':
                                    ymax = int(dic[j])
                            if xmax <= xmin:
                                pass
                            elif ymax <= ymin:
                                pass
                            else:
                                xml.write('\t\t<bndbox>\n')
                                xml.write('\t\t\t<xmin>' + str(xmin) + '</xmin>\n')
                                xml.write('\t\t\t<ymin>' + str(ymin) + '</ymin>\n')
                                xml.write('\t\t\t<xmax>' + str(xmax) + '</xmax>\n')
                                xml.write('\t\t\t<ymax>' + str(ymax) + '</ymax>\n')
                                xml.write('\t\t</bndbox>\n')
                                xml.write('\t</object>\n')
                xml.write('</annotation>')
