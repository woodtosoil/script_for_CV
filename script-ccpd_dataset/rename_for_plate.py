# _*_ coding=utf-8 _*_
import cv2
import shutil
import os
import glob

datapath="/media/root/硬盘2/ccpd_dataset/newimg"
newpath="/media/root/硬盘2/ccpd_dataset/plate-val"
provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "警", "学", "O"]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', 'O']
ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
       'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']

imglist=glob.glob(os.path.join(datapath,'*.jpg'))
for img in imglist:
    image=img.split('/')[-1]
    name=image.split('.')[0]
    x0=int(name.split('_')[0])
    x1=int(name.split('_')[1])
    x2=int(name.split('_')[2])
    x3=int(name.split('_')[3])
    x4=int(name.split('_')[4])
    x5=int(name.split('_')[5])
    x6=int(name.split('_')[6])
    # print(provinces[x0])
    newname=str(provinces[x0]+alphabets[x1]+ads[x2]+ads[x3]+ads[x4]+ads[x5]+ads[x6])
    print(newname)
    os.rename(os.path.join(datapath,image),os.path.join(newpath,newname)+".jpg")
