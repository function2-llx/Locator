import numpy as np
import cv2

class Sharpener:
    def __init__(self):
        pass

    def __get_sharpen_kernel(self):
        return np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)

    def get_sharpen(self, src):
        img = cv2.imread(src, 0)
        kernel = self.__get_sharpen_kernel()
        dst = cv2.filter2D(img, -1, kernel=kernel)
        return dst

    def sharpen(self, src):
        import re
        pattern = re.compile('(.*)\.(.*)')
        pre = pattern.match(src)[1] + '-sharpen'
        suf = pattern.match(src)[2]
        cv2.imwrite('%s.%s' % (pre, suf), self.get_sharpen(src))