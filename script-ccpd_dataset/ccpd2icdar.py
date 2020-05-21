# _*_ coding=utf-8 _*_
import cv2
import shutil
import os
import glob

provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "警", "学", "O"]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', 'O']
ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
       'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']


#031875-90_87-168&406_506&531-488&513_186&516_182&433_484&429-0_0_11_27_8_25_30-38-34
#右下角->左下角->左上角->右上角
def spl(newpath,datapath):
    image=cv2.imread(datapath)
    name=datapath.split('\\')[-1].split('.')[0]
    local2=name.split('-')[2]
    local4=name.split('-')[3]
    plate=name.split('-')[-3]
    # x0=int(local.split('_')[0].split('&')[0])
    # y0=int(local.split('_')[0].split('&')[1])
    # x1=int(local.split('_')[1].split('&')[0])
    # y1=int(local.split('_')[1].split('&')[1])
    #print(name)
    rbx=(local4.split('_')[0].split('&')[0])
    rby=(local4.split('_')[0].split('&')[1])
    lbx=(local4.split('_')[1].split('&')[0])
    lby=(local4.split('_')[1].split('&')[1])
    ltx=(local4.split('_')[2].split('&')[0])
    lty=(local4.split('_')[2].split('&')[1])
    rtx=(local4.split('_')[3].split('&')[0])
    rty=(local4.split('_')[3].split('&')[1])
#rename
    x0=int(plate.split('_')[0])
    x1=int(plate.split('_')[1])
    x2=int(plate.split('_')[2])
    x3=int(plate.split('_')[3])
    x4=int(plate.split('_')[4])
    x5=int(plate.split('_')[5])
    x6=int(plate.split('_')[6])
    newname=str(provinces[x0]+alphabets[x1]+ads[x2]+ads[x3]+ads[x4]+ads[x5]+ads[x6])
    return [ltx,lty,rtx,rty,rbx,rby,lbx,lby,newname]

if __name__ == '__main__':
    imgpath="E:\\code\\script\\script-ccpd_dataset\\test"
    imglist=glob.glob(os.path.join(imgpath,'*.jpg'))
    newpath="E:\\code\\script\\script-ccpd_dataset\\test2"
    i=0
    for img in imglist: 
        #print(img)
        
        info=spl(newpath,img)
        i=i+1
        shutil.copy(img,newpath+'\\'+str(i).zfill(5)+".jpg")
        f = open(newpath+'\\'+str(i).zfill(5)+".txt",'w')
        f.write(info[0])
        for j in range(len(info)-1):

            f.writelines(','+info[j+1])
        f.close()

    
    