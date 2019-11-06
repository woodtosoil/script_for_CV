#-*- coding:utf-8 -*-
import cv2
img_name="/media/root/硬盘2/ccpd_dataset/label-huizhi/06-109_53-131&464_477&660-453&647_191&555_165&473_427&565-0_0_13_28_28_33_31-96-71.jpg"




iname = img_name.rsplit('/', 1)[-1].rsplit('.', 1)[0].split('-')
        # fps = [[int(eel) for eel in el.split('&')] for el in iname[3].split('_')]
        # leftUp, rightDown = [min([fps[el][0] for el in range(4)]), min([fps[el][1] for el in range(4)])], [
        #     max([fps[el][0] for el in range(4)]), max([fps[el][1] for el in range(4)])]
[leftUp, rightDown] = [[int(eel) for eel in el.split('&')] for el in iname[2].split('_')]
image = cv2.imread(img_name)
x1 = int(leftUp[0])
y1 = int(leftUp[1])
x2 = int(rightDown[0])
y2 = int(rightDown[1])

c1, c2 = (x1, y1), (x2, y2)
cv2.rectangle(image, c1, c2, (0, 255, 0), thickness=3)
#cv2.namedWindow(img_name.split("/")[-1],0)
#cv2.resizeWindow(img_name.split("/")[-1],w,h)
#cv2.imshow(img_name.split("/")[-1],image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite(img_name,image)

