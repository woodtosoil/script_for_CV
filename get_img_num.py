import glob
import os

image_dir = "/home/djw/Fine-grained-erro/images"
images_list = glob.glob(os.path.join(image_dir,"*.jpg"))
number = 0
for image_path in images_list:
    image_name = image_path.split("/")[-1]
    number += 1
    with open("fine-grained.txt","a")as f:
        f.write(image_name)
        f.write("\n")
print("total number is :".format(str(number))










