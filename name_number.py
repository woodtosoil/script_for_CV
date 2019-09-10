import cv2
import os
import glob
import xml.etree.ElementTree as ET
import random
import shutil

image_dir = "/home/djw/huizhi_second/JPEGImages/*.jpg"
xml_dir = "/home/djw/huizhi_second/Annotations/*.xml"

#new_tricycle = "/home/djw/Fine-grained-erro/err"


images_list = glob.glob(image_dir)
xmls_list = glob.glob(xml_dir)
i=0

for index , image_file in enumerate(images_list):
    image_name = image_file.split("/")[-1]
    xml_file = image_file.replace("JPEGImages", "Annotations").replace("jpg", "xml")
    xml_name = xml_file.split("/")[-1]
    #if xml_file not in xmls_list:
        #print("The image {} don't have xml file".format(image_name))
        #continue
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for object in root.findall("object"):
        #if os.path.exists(os.path.join(new_tricycle, "images", image_name)):
            #continue
        name = object.find("name").text
        if name == "Tricycle":
            i=i+1
            #new_tricycle_images = os.path.join(new_tricycle,"images")
            #new_tricycle_xmls = os.path.join(new_tricycle,"annotations")
            #os.makedirs(new_tricycle_images,exist_ok=True)
            #os.makedirs(new_tricycle_xmls,exist_ok=True)

            #shutil.move(image_file,os.path.join(new_tricycle_images,image_name))
            #shutil.move(xml_file,os.path.join(new_tricycle_xmls,xml_name))
    print(i)
    print("{}/{}".format(index,len(images_list)))



