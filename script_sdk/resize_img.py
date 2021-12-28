import cv2

imgpath="D:\\test\\face_img\\face.jpg"
savepath="D:\\test\\face_img\\face640.jpg"
img = cv2.imread(imgpath)
resize_img = cv2.resize(img,(640,640))
cv2.imwrite(savepath,resize_img)