#!/usr/bin/python
#-*- coding:utf-8 -*-
# pip install lxml

import sys
import os
import cv2
import json
import glob
import shutil
import xml.etree.ElementTree as ET
from pycocotools.coco import COCO

START_BOUNDING_BOX_ID = 1
# PRE_DEFINE_CATEGORIES = {"BigTruck":1,"MiddleBus":2,"Bicycle":3,"Motorcycle":4,"BigBus":5,"MPV":6,
#                  "Electrombile":7,"LongTruck":8,"Person":9,"Sedan":10,"MiniTruck":11,"Pickup":12,
#                  "LightTruck":13,"MiniBus":14,"Tricycle":15,"SUV":16}
PRE_DEFINE_CATEGORIES = {"BigTruck":1,"MiddleBus":2,"BigBus":3,"MPV":4,"LongTruck":5,"Sedan":6,
                         "Pickup":7,"LightTruck":8,"MiniBus":9,"SUV":10}

# vehicle_index= {1:"BigTruck",2:"MiddleBus",3:"Bicycle",4:"Motorcycle",5:"BigBus",
#                  6:"MPV",7:"Electrombile",8:"LongTruck",9:"Person",10:"Sedan",
#                  11:"MiniTruck",12:"Pickup",13:"LightTruck",14:"MiniBus",15:"Tricycle",
#                  16:"SUV"}
vehicle_index= {1:"BigTruck",2:"MiddleBus",3:"BigBus",4:"MPV",5:"LongTruck",
                6:"Sedan",7:"Pickup",8:"LightTruck",9:"MiniBus",10:"SUV"}

def get(root, name):
    vars = root.findall(name)
    return vars


def get_and_check(root, name, length):
    vars = root.findall(name)
    if len(vars) == 0:
        raise NotImplementedError('Can not find %s in %s.' % (name, root.tag))
    if length > 0 and len(vars) != length:
        raise NotImplementedError('The size of %s is supposed to be %d, but is %d.' % (name, length, len(vars)))
    if length == 1:
        vars = vars[0]
    return vars


def get_filename_as_int(filename):
    try:
        filename = os.path.splitext(filename)[0]
        return int(filename)
    except:
        raise NotImplementedError('Filename %s is supposed to be an integer.' % (filename))


def convert(image_path,xml_dir, json_file):
    json_dict = {"images": [], "type": "instances", "annotations": [],
                 "categories": []}
    categories = PRE_DEFINE_CATEGORIES
    bnd_id = START_BOUNDING_BOX_ID
    for xml_f in xml_dir:
        print("Processing %s" % (xml_f))
        tree = ET.parse(xml_f)
        root = tree.getroot()
        filename = xml_f.split("/")[-1].replace("xml","jpg")
        image_dir = os.path.join(image_path,xml_f.split("/")[-1].replace("xml","jpg"))
        image_id = get_filename_as_int(xml_f.split("/")[-1].split(".")[0])
        h,w,_ = cv2.imread(image_dir).shape
        image = {'file_name': filename, 'height': h, 'width': w,
                 'id': image_id}
        json_dict['images'].append(image)
        for obj in root.findall('object'):
            category = get_and_check(obj, 'name', 1).text
#  11:"Bicycle",12:"Motorcycle",13:"Electrombile",14:"Tricycle",15:"Person"

            if category  == "Ignore" or category == "Person" or category == "Tricycle" or category == "Electrombile":
                continue
            if category  == "Motorcycle" or category  == "Bicycle":
                continue

	
	
            # if category not in categories:
            #     new_id = len(categories)
            #     categories[category] = new_id
            category_id = categories[category]
            bndbox = get_and_check(obj, 'bndbox', 1)
            xmin = int(get_and_check(bndbox, 'xmin', 1).text) - 1
            ymin = int(get_and_check(bndbox, 'ymin', 1).text) - 1
            xmax = int(get_and_check(bndbox, 'xmax', 1).text)
            ymax = int(get_and_check(bndbox, 'ymax', 1).text)
            assert (xmax > xmin)
            assert (ymax > ymin)
            o_width = abs(xmax - xmin)
            o_height = abs(ymax - ymin)
            ann = {'area': o_width * o_height, 'iscrowd': 0, 'image_id':
                image_id, 'bbox': [xmin, ymin, o_width, o_height],
                   'category_id': category_id, 'id': bnd_id, 'ignore': 0,
                   'segmentation': []}
            json_dict['annotations'].append(ann)
            bnd_id = bnd_id + 1

    for cate, cid in categories.items():
        cat = {'supercategory': 'none', 'id': cid, 'name': cate}
        json_dict['categories'].append(cat)
    json_fp = open(json_file, 'w')
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()

def view(json_path,image_path):
    coco = COCO(json_path)
    anns = coco.anns
    imgToAnns = coco.imgToAnns
    catToImgs = coco.catToImgs
    imgs = coco.imgs
    cats = coco.cats
    for index, img in imgs.items():
        img_path = os.path.join(image_path, img["file_name"])
        name = img_path.split("/")[-1]
        image = cv2.imread(img_path)
        h, w, _ = image.shape
        ann_boxes = imgToAnns[index]
        # res_boxes = res_imgToAnns[index]

        for box in ann_boxes:
            bbox = box["bbox"]
            category_id = box["category_id"]
            vehicle_type = vehicle_index[category_id]
            x1 = int(bbox[0])
            x2 = int(bbox[0] + bbox[2])
            y1 = int(bbox[1])
            y2 = int(bbox[1] + bbox[3])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, vehicle_type, (x1, y1 - 3), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.namedWindow(name, 0)
        cv2.resizeWindow(name, w, h)
        cv2.imshow(name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':

    train_xml_folder = "/media/root/硬盘2/huizhi/train/train_xml"
    val_xml_folder = "/media/root/硬盘2/huizhi/val/val_xml"
    train_json_path = "/media/root/硬盘2/huizhi/json/train.json"
    val_json_path = "/media/root/硬盘2/huizhi/json/val.json"
    train_image_path = "/media/root/硬盘2/huizhi/train/train_img"
    val_image_path = "/media/root/硬盘2/huizhi/val/val_img"
    train_xmls = glob.glob(os.path.join(train_xml_folder,"*.xml"))
    val_xmls = glob.glob(os.path.join(val_xml_folder,"*.xml"))
    convert(train_image_path,train_xmls,train_json_path)
    convert(val_image_path,val_xmls,val_json_path)

    #view(val_json_path,val_image_path)

    # xml_list = glob.glob(val_xml_folder+"/*.xml")
    # for i in xml_list:
    #     image_path = os.path.join("/home/rah/huizhishuju/2019_5_20/1",i.split("/")[-1].replace("xml","jpg"))
    #     new_image_path = os.path.join("/home/rah/huizhishuju/2019_5_20/2",i.split("/")[-1].replace("xml","jpg"))
    #     shutil.copy(image_path,new_image_path)
