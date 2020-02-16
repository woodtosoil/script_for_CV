#-*- coding:utf-8 -*-
import cv2
import glob
import os
import xml.etree.ElementTree as ET
import random


view_dir = "/media/root/硬盘2/detrac/DETRAC-Train-Annotations-XML/"
images_dir = "/media/root/硬盘2/detrac/Insight-MVT_Annotation_Train/"
newpath="/media/root/硬盘2/detrac/newimg"
random_select = list()
# total_object = 0
xml_list = glob.glob(os.path.join(view_dir,"*.xml"))
# number = len(xml_list)
# select_number = int(number*0.05)
# for i in range(0,select_number):
#     random_select.append(random.randint(0,number))

# for i in random_select:
for xml in xml_list:
    xmlname=xml.split("/")[-1].split(".")[0]
    # xml = xml_list[i]
    image_path = os.path.join(images_dir,xmlname)
    imglist=os.listdir(image_path)
    print(xml)
    tree = ET.parse(xml)
    root = tree.getroot()
    # sequence=root.find("sequence")
    ignore=root.find("ignored_region")
    # print(ignore.findall("box"))

    for img in imglist:
        imgpath=os.path.join(image_path,img)
        image = cv2.imread(imgpath)
        # h,w,_ = image.shape
        for bndbox in ignore.findall("box"):
            # name = obj.find("ignored_region").text
            # total_object += 1
            # print(name)
            # print(bndbox)
            # bndbox = obj.find("box")
            x1 = int(float(bndbox.attrib['left']))
            y1 = int(float(bndbox.attrib['top']))
            x2 = int(float(bndbox.attrib['width']))+x1
            y2 = int(float(bndbox.attrib['height']))+y1


            image[y1:y2,x1:x2,:]=0
        # c1, c2 = (x1, y1), (x2, y2)
        # cv2.rectangle(image, c1, c2, (0, 255, 0), thickness=3)
        # cv2.putText(image, name, (c1[0], c1[1] - 2), cv2.FONT_HERSHEY_PLAIN, 3, [0, 255, 0], thickness=3)
    # cv2.namedWindow(image_path.split("/")[-1],0)
    # cv2.resizeWindow(image_path.split("/")[-1],w,h)
    # cv2.imshow(image_path.split("/")[-1],image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imwrite(os.path.join("/home/rah/datas/JPEGImagess/script/huizhichongxinbiaozhu",image_path.split("/")[-1]),image)
            savePath=os.path.join(newpath,xmlname)
            print(savePath)
            if os.path.exists(savePath)==False: #判断文件夹是否存在
                os.makedirs(savePath)
            cv2.imwrite(os.path.join(savePath,img),image)
# print("total object is :".format(total_object))

