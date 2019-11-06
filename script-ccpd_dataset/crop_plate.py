# _*_ coding=utf-8 _*_
import cv2
import shutil
import os
import glob


def spl(newpath,datapath):
    image=cv2.imread(datapath)
    name=datapath.split('/')[-1].split('.')[0]
    local=name.split('-')[2]
    plate=name.split('-')[-3]
    newimage=os.path.join(newpath,plate)+".jpg"
    x0=int(local.split('_')[0].split('&')[0])
    y0=int(local.split('_')[0].split('&')[1])
    x1=int(local.split('_')[1].split('&')[0])
    y1=int(local.split('_')[1].split('&')[1])
    # print(x0,y0,x1,y1)
    cropImg = image[y0:y1,x0:x1]
    cv2.imwrite(newimage,cropImg)
    # return x0,y0,x1,y1

if __name__ == '__main__':
    datapath="/media/root/硬盘2/ccpd_dataset/ccpd_weather"
    newpath="/media/root/硬盘2/ccpd_dataset/newimg"
    imglist=glob.glob(os.path.join(datapath,'*.jpg'))
    for img in imglist: 
        print(img)
        spl(newpath,img)



