# -*- coding:UTF-8 -*-
import xml.etree.ElementTree as ET
import os
import glob
import shutil
import cv2

xml_files = "/media/root/硬盘2/huizhi/tes"
rename_path="/media/root/硬盘2/huizhi/ori/"

os.makedirs(rename_path,exist_ok=True)
xmls = glob.glob(os.path.join(xml_files,"*.xml"))
for xml in xmls:
    tree = ET.parse(xml)
    root = tree.getroot()
    name=root.findall("filename")[0].text
    newname=name.split('.')[0]
    newxml=rename_path+newname+".xml"
    # for obj in root.findall("filename"):
    #     name = obj.find("name").text
    shutil.copy(xml,newxml)
    print(newname)
