#-*- coding:utf-8 -*-
#opencv和PIL图片读入后的相互转换
import cv2
from PIL import Image
import numpy as np
 
img = cv2.imread("001.jpg") # opencv打开的是BRG
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#########
img2 = Image.fromarray(img1)
img3 = np.asarray(img2)
#矩阵内容 img1==img3,长宽相反

