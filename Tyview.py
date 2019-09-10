import cv2
import glob
import os
import xml.etree.ElementTree as ET
import random
import shutil


view_dir = "/home/djw/Fine-grained-erro/check/新增三轮车"
images_dir = "/home/djw/Fine-grained-erro/新增三轮车"
new_img="/home/djw/Fine-grained-erro/ignore/imag/"
new_xml="/home/djw/Fine-grained-erro/ignore/_xml/"
random_select = list()
anns_images = 0
no_anns_images = 0
class_number = {"Sedan":0,"MiniBus":0,"SUV":0,"MPV":0,"MiddleBus":0,"BigBus":0,"Pickup":0,"MiniTruck":0,"LightTruck":0,
                "BigTruck":0,"LongTruck":0,"Tricycle": 0,"Motorcycle":0,"Electrombile":0,"Bicycle":0,"Person":0}
xml_list = glob.glob(os.path.join(view_dir,"*.xml"))
# number = len(xml_list)
# select_number = int(number*0.05)
# for i in range(0,select_number):
#     random_select.append(random.randint(0,number))

# for i in random_select:
for xml in xml_list:
    # xml = xml_list[i]
    have_vehicle = False
    image_path = os.path.join(images_dir,xml.split("/")[-1].replace("xml","jpg"))

    if not os.path.exists(image_path):
        image_path = os.path.join(images_dir,xml.split("/")[-1].replace("xml","JPG"))
        if not os.path.exists(image_path):
            print("The xml {} don't have image".format(xml.split("/")[-1]))
            no_anns_images += 1
            continue
    image = cv2.imread(image_path)
    h,w,_ = image.shape
    tree = ET.parse(xml)
    root = tree.getroot()
    for obj in root.findall("object"):
        name = obj.find("name").text
        if name == "Ignore":
            bndbox = obj.find("bndbox")
            x1 = int(bndbox.find('xmin').text)
            y1 = int(bndbox.find('ymin').text)
            x2 = int(bndbox.find('xmax').text)
            y2 = int(bndbox.find('ymax').text)
            image[y1:y2,x1:x2,:]=0
        else:
            #print(name)
            class_number[name] += 1
            bndbox = obj.find("bndbox")
            x1 = int(bndbox.find('xmin').text)
            y1 = int(bndbox.find('ymin').text)
            x2 = int(bndbox.find('xmax').text)
            y2 = int(bndbox.find('ymax').text)
            c1, c2 = (x1, y1), (x2, y2)
            cv2.rectangle(image, c1, c2, (0, 255, 0), thickness=3)
            cv2.putText(image, name, (c1[0], c1[1] - 2), cv2.FONT_HERSHEY_PLAIN, 3, [0, 255, 0], thickness=3)
            have_vehicle = True
    if have_vehicle:
        # cv2.namedWindow(image_path.split("/")[-1],0)
        # cv2.resizeWindow(image_path.split("/")[-1],w,h)
        # cv2.imshow(image_path.split("/")[-1],image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imwrite(os.path.join("/home/djw/Fine-grained-erro/2",image_path.split("/")[-1]),image)
        anns_images += 1
    else:
        shutil.move(image_path, new_img)

print("Summary ......")
print("There are total {} anns in datas :".format(anns_images))
print("There are total {} no_anns in datas :".format(no_anns_images))
for k,v in class_number.items():
    print("There {} numbers in data is {}".format(k,v))

