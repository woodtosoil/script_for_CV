#-*- coding:utf-8 -*-
import cv2
import glob
import os
import xml.etree.ElementTree as ET
import random


view_dir = "/media/root/硬盘2/huizhi/test/annotations/"
images_dir = "/media/root/硬盘2/huizhi/test/images/"
random_select = list()
total_object = 0
xml_list = glob.glob(os.path.join(view_dir,"*.xml"))
# number = len(xml_list)
# select_number = int(number*0.05)
# for i in range(0,select_number):
#     random_select.append(random.randint(0,number))

# for i in random_select:
for xml in xml_list:
    # xml = xml_list[i]
    image_path = os.path.join(images_dir,xml.split("/")[-1].replace("xml","jpg"))
    image = cv2.imread(image_path)
    h,w,_ = image.shape
    tree = ET.parse(xml)
    root = tree.getroot()
    for obj in root.findall("object"):
        name = obj.find("name").text
        total_object += 1
        print(name)
        bndbox = obj.find("bndbox")
        x1 = int(bndbox.find('xmin').text)
        y1 = int(bndbox.find('ymin').text)
        x2 = int(bndbox.find('xmax').text)
        y2 = int(bndbox.find('ymax').text)
        c1, c2 = (x1, y1), (x2, y2)
        cv2.rectangle(image, c1, c2, (0, 255, 0), thickness=3)
        cv2.putText(image, name, (c1[0], c1[1] - 2), cv2.FONT_HERSHEY_PLAIN, 3, [0, 255, 0], thickness=3)
    cv2.namedWindow(image_path.split("/")[-1],0)
    cv2.resizeWindow(image_path.split("/")[-1],w,h)
    cv2.imshow(image_path.split("/")[-1],image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite(os.path.join("/home/rah/datas/JPEGImagess/script/huizhichongxinbiaozhu",image_path.split("/")[-1]),image)

print("total object is :".format(total_object))

