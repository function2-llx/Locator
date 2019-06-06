import cv2
import numpy as np
import sys

def __get_kernel(self):
    return np.array([[0, -1, 0], [-1, 2000, -1], [0, -1, 0]], np.float32)

def get_blur(img):
    return cv2.blur(img, (15, 1))

def get_sharpen(img):
    kernel = __get_kernel()
    img = cv2.filter2D(img, -1, kernel=kernel)

    return img


if __name__ == "__main__":
    img = cv2.imread('con-3.jpg', 0)

    cv2.imshow('origin', img)
    cv2.imshow('blur', get_blur(img))
    cv2.imshow('sharpen', get_sharpen(img))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    sys.stderr.write('test\n')
    