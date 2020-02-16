#-*- coding:utf-8 -*-
import shutil
import os

xml_path="/media/ljy2019/760AE2350AE1F1D3/datas/detrac/xml"
new_path="/media/ljy2019/760AE2350AE1F1D3/datas/detrac/xml_train"
if os.path.exists(new_path)==False: #判断文件夹是否存在
     os.makedirs(new_path)
 
f=open(r"/media/ljy2019/760AE2350AE1F1D3/datas/detrac/ImageSets/Main/train.txt")
line=f.readline()
while line:
    line=line.split()[0]
    xml_dir=os.path.join(xml_path,line)+".xml"
    shutil.copy(xml_dir,new_path)
    line=f.readline()
f.close()
