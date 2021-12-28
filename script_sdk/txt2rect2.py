import os
import shutil
import cv2
import re

def view(txt_path,image_path,save_path):
    lists = os.listdir(txt_path)
    for txt in lists:
        with open(txt_path+txt,'r') as f:
            lines = f.readlines()
        

        img_path = os.path.join(image_path,txt.replace(".txt",".jpg"))
        save_img = os.path.join(save_path,txt.replace(".txt",".jpg"))
        # save_txt = os.path.join(save_path,txt.replace("jpg","txt"))
        image = cv2.imread(img_path)
        # print(image)
        # h, w, _ = image.shape
        # for line in lines[2:]:
        for line in lines:
        # print(loc)
            loc = line.split(" ")
            print(loc)
            x0 = int(loc[0])
            y0 = int(loc[1])
            # x1 = int(loc[2])+x0
            # y1 = int(loc[3])+y0
            x1 = int(loc[2])
            y1 = int(loc[3])
            score = loc[4]
            # print(loc)
            cv2.rectangle(image, (x0,y0), (x1,y1), (0, 255, 0), 2)
            cv2.putText(image, score, (x0,y0-3), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        # file=open(save_txt,mode='w')
        # fileline = " ".join(i for i in loc)
        # file.write("0 ")
        # file.write(fileline)
        # file.write(" ")
        # file.write(carinfo[13:])
        # print(save_img)
        # print(image.size())

        cv2.imwrite(save_img,image)
        f.close()





if __name__ == '__main__':
    txt_path = "D:\\test\\txt\\"
    image_path = "D:\\test\\img\\"
    save_path = "D:\\test\\res\\"
    view(txt_path,image_path,save_path)