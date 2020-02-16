# -*- coding:UTF-8 -*-
import os, random, shutil 
random.seed(1)

def moveFile(imgDir): 
    pathDir = os.listdir(imgDir) #取图片的原始路径 
    imgnumber=len(pathDir) 
    rate=0.05 #自定义抽取图片的比例，比方说100张抽10张，那就是0.1 
    picknumber=int(imgnumber*rate) #按照rate比例从文件夹中取一定数量图片 
    sample = random.sample(pathDir, picknumber) #随机选取picknumber数量的样本图片 

    for img_name in sample:
        xml_name = img_name.replace("xml","jpg") 
        print (img_name) 
        shutil.copy(imgDir+img_name, newimgDir+img_name)
        #shutil.copy(xmlDir+xml_name, newxmlDir+xml_name)
    return 

if __name__ == '__main__': 
    #xmlDir = "/media/root/硬盘2/huizhi/JPEGImagess/JPEGImages/" #源文件夹路径 
    imgDir="/media/root/硬盘2/复审20190713/xml/"
    #newxmlDir = '/media/root/硬盘2/huizhi/test/images/' #移动到新的文件夹路径 
    newimgDir = '/media/root/硬盘2/复审20190713/new_xml/' #移动到新的文件夹路径 
   
    moveFile(imgDir)
