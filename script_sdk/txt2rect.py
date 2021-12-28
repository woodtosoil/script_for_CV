import os
import shutil
import cv2
import re

def view(txt_path,image_path,save_path):
    with open(txt_path,'r',encoding="utf-8") as f:
        lists = f.readlines()
    num = len(lists)
    for line in lists:
        img_name = line.split("-")[0].split("/")[-1]
        try:
            loc = line.split("-")[1]
            carinfo = line.split("-")[2]
        except:
            continue
        if carinfo[0] == 'V':
            continue
        img_path = os.path.join(image_path,img_name)
        save_img = os.path.join(save_path,img_name)
        save_txt = os.path.join(save_path,img_name.replace("jpg","txt"))
        image = cv2.imread(img_path)
        h, w, _ = image.shape
        loc = re.sub("[()]","", loc)
        loc = loc.replace("[","")
        loc = loc.replace("]","")
        # print(loc)
        loc = loc.split(",")
        x0 = int(loc[0])
        y0 = int(loc[1])
        x1 = int(loc[2])
        y1 = int(loc[3])
        cv2.rectangle(image, (x0,y0), (x1,y1), (0, 255, 0), 2)
        cv2.putText(image, carinfo, (x0,y0-3), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        file=open(save_txt,mode='w')
        fileline = " ".join(i for i in loc)
        file.write("0 ")
        file.write(fileline)
        file.write(" ")
        file.write(carinfo[13:])

        cv2.imwrite(save_img,image)
        file.close()





if __name__ == '__main__':
    txt_path = "D:\\datasets\\Face++\\20211015084732.txt"
    image_path = "D:\\datasets\\Face++\\plate_data"
    save_path = "D:\\datasets\\Face++\\result2"
    view(txt_path,image_path,save_path)