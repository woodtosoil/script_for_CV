import numpy as np
import cv2


def motion_blur(img_path, degree=3, angle=10):
  image = cv2.imread(img_path)
  image = np.array(image)
  # 这里生成任意角度的运动模糊kernel的矩阵， degree越大，模糊程度越高
  M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
  motion_blur_kernel = np.diag(np.ones(degree))
  motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))
  motion_blur_kernel = motion_blur_kernel / degree
  blurred = cv2.filter2D(image, -1, motion_blur_kernel)
  # convert to uint8
  cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
  blurred = np.array(blurred, dtype=np.uint8)
  return blurred


def guass_blur(image_path:str):
    img=cv2.imread(image_path,cv2.IMREAD_COLOR)
    # cv2.imshow('img',img)
    result=cv2.GaussianBlur(img,(0,0),3)
    return result


if __name__ == '__main__':
    img_path = "E:\\datasets\\+blur\\70.jpg"
    save_path = "E:\\datasets\\+blur\\70_1.png"
    # img_ = motion_blur(img_path)
    img_ = guass_blur(img_path)
    cv2.imwrite(save_path,img_)
    # cv2.imshow('Source image',img)
    # cv2.imshow('blur image',img_)
    # cv2.waitKey()