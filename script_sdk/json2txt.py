import cv2
import os
import json


def view(json_path, image_path,txt_path):
    with open(json_path, 'r') as json_fp:
        json_dict = json.load(json_fp)
    for img_name, label in json_dict.items():
        img_path = os.path.join(image_path, img_name)
        
        # print(img_path)
        name = img_path.split("\\")[-1]
        image = cv2.imread(img_path)
        txt = os.path.join(txt_path,name.split('.')[0]+'.txt')
        # print(image)
        h, w, _ = image.shape
        plate_label = label['gt']
        bbox = label['quad']
        x0 = int(bbox[0][0])
        y0 = int(bbox[0][1])
        x1 = int(bbox[2][0])
        y1 = int(bbox[2][1])
        bb = (x0,y0,x1,y1)
        with open(txt,'w') as txt_fb:
            txt_fb.write("0" + " " + " ".join([str(a) for a in bb])+" "+plate_label)
    txt_fb.close()

img_folder = 'D:\\datasets\\Face++\\plate_data\\'
# xml_folder = '/data/djw/plate_data/json2xml/'
txt_folder = 'D:\\datasets\\Face++\\plate_txt_rec\\'

json_folder = 'D:\\datasets\\Face++\\plate_data_label.json'

view(json_folder, img_folder,txt_folder)