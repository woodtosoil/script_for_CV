import cv2
import numpy as np


def NV122RGB(yuv_path, width, height):
    with open(yuv_path, 'rb') as f:
        yuvdata = np.fromfile(f, dtype=np.uint8)
    cv_format = cv2.COLOR_YUV2BGR_NV12
    bgr_img = cv2.cvtColor(yuvdata.reshape((height*3//2, width)), cv_format)
    return bgr_img


if __name__ == "__main__":
    import glob
    imgs=glob.glob('track/*')
    width=640
    height=640
    for img in imgs:
        save_path = 'out'+img[:-3]+'jpg'
        img = NV122RGB(img, width, height)
        cv2.imwrite(save_path, img)