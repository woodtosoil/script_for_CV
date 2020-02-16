import cv2
import os
import glob
import xml.etree.ElementTree as ET


img_list = glob.glob("*.jpg")
for img in img_list:
    ignore_boxes = list()
    vehicle_boxes = list()
    xml_name = img.split(".jpg")[0].split("-")[0]+".xml"
    tree = ET.parse(os.path.join("/home/rah/datas/DETRAC/DETRAC-Train-Annotations-XML/train",xml_name))
    root = tree.getroot()
    for ignored_region in root.findall("ignored_region"):
        for box in ignored_region.findall("box"):
            left = int(float(box.attrib["left"]))
            top  = int(float(box.attrib["top"]))
            width = int(float(box.attrib["width"]))
            height = int(float(box.attrib["height"]))
            ignore_boxes.append([left,top,width,height])
    for frame in root.findall("frame"):
        if frame.attrib["num"] == "1":
            target_list = frame.find("target_list")
            for target in target_list.findall("target"):
                box = target.find("box")
                left = int(float(box.attrib["left"]))
                top = int(float(box.attrib["top"]))
                width = int(float(box.attrib["width"]))
                height = int(float(box.attrib["height"]))
                vehicle_boxes.append([left, top, width, height])
    image = cv2.imread(img)
    for box in ignore_boxes:
        cv2.rectangle(image,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),color=(0, 0, 255), thickness=1)
    for box in vehicle_boxes:
        cv2.rectangle(image,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),color=(0, 255, 0), thickness=1)
    cv2.imwrite("new" + img, image)

