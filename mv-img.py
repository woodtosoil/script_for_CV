#-*- coding:utf-8 -*-
import shutil
import glob
import os

xml_dir = "/media/a313/FEE2C4F9E2C4B765/huizhi-data/ori_Annotations/val/"
images_dir = "/media/a313/FEE2C4F9E2C4B765/huizhi-data/images/"
new_path="/media/a313/FEE2C4F9E2C4B765/huizhi-data/testimages/"
xml_list = glob.glob(os.path.join(xml_dir,"*.xml"))
for xml in xml_list:
    image_path = os.path.join(images_dir,xml.split("/")[-1].replace("xml","jpg"))
    shutil.copy(image_path,new_path)


