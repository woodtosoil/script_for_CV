# -*- coding:UTF-8 -*-
import xml.etree.ElementTree as ET
import os
import glob
import shutil
import cv2


vehicle_index = {"BigTruck":"0","MiddleBus":"1","Bicycle":"2","Motorcycle":"3","BigBus":"4","MPV":"5",
                 "Electrombile":"6","LongTruck":"7","Person":"8","Sedan":"9","MiniTruck":"10","Pickup":"11",
                 "LightTruck":"12","MiniBus":"13","Tricycle":"14","SUV":"15"}

############## rename the images and annotations ##############
images_folder1 = "/media/root/硬盘2/huizhi/JPEGImagess/JPEGImages"

rename_image_dir = "/media/root/硬盘2/huizhi/val_img"
xml_files = "/media/root/硬盘2/huizhi/val"

os.makedirs(rename_image_dir,exist_ok=True)
xmls = glob.glob(os.path.join(xml_files,"*.xml"))
for index,xml in enumerate(xmls):
    if os.path.exists(os.path.join(images_folder1,xml.split("/")[-1]).replace("xml","jpg").replace("xml","JGP")):
        image = cv2.imread(os.path.join(images_folder1,xml.split("/")[-1]).replace("xml","jpg").replace("xml","JGP"))
    else:
        print("There have no image {}".format(xml.split("/")[-1]))
        continue
    #tree = ET.parse(xml)
    #root = tree.getroot()
    #for obj in root.findall("object"):
        #name = obj.find("name").text
        #if name == "Ignore":
            #bndbox = obj.find("bndbox")
            #x1 = int(bndbox.find('xmin').text)
            #y1 = int(bndbox.find('ymin').text)
            #x2 = int(bndbox.find('xmax').text)
            #y2 = int(bndbox.find('ymax').text)
            #image[y1:y2, x1:x2, :] = 0
    new_image_path = os.path.join(rename_image_dir,str(index+1).zfill(5)+".jpg")
    new_xml_path = os.path.join(rename_image_dir.replace("val_img","val_xml"),str(index+1).zfill(5)+".xml")
    cv2.imwrite(new_image_path,image)
    shutil.copy(xml,new_xml_path)



























