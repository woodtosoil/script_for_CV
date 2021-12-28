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
            loc = line.strip().split(" ")
            print(loc)
            x0 = int(loc[0])
            y0 = int(loc[1])
            # x1 = int(loc[2])+x0
            # y1 = int(loc[3])+y0
            x1 = int(loc[2])
            y1 = int(loc[3])
            score = loc[4]
            landm_1x = int(loc[5])
            landm_1y = int(loc[6])
            landm_2x = int(loc[7])
            landm_2y = int(loc[8])
            landm_3x = int(loc[9])
            landm_3y = int(loc[10])
            landm_4x = int(loc[11])
            landm_4y = int(loc[12])
            landm_5x = int(loc[13])
            landm_5y = int(loc[14])
            # print(loc)
            cv2.rectangle(image, (x0,y0), (x1,y1), (0, 255, 0), 2)
            cv2.putText(image, score, (x0,y0-3), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cv2.circle(image, (landm_1x,landm_1y), 1, (0, 0, 255), 4)
            cv2.circle(image, (landm_2x, landm_2y), 1, (0, 255, 255), 4)
            cv2.circle(image, (landm_3x, landm_3y), 1, (255, 0, 255), 4)
            cv2.circle(image, (landm_4x,landm_4y), 1, (0, 255, 0), 4)
            cv2.circle(image, (landm_5x, landm_5y), 1, (255, 0, 0), 4)
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
    txt_path = "D:\\test\\face_txt\\"
    image_path = "D:\\test\\face_img\\"
    save_path = "D:\\test\\face_res\\"
    view(txt_path,image_path,save_path)