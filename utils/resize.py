import cv2
import numpy as np


def resize(img_path: str, dsize: tuple):
    img = cv2.imread(img_path)
    img = cv2.resize(img, dsize)
    return img


if __name__ == '__main__':
    img_path = "../images/houban_oee.png"
    img = resize(img_path, (640, 480))
    cv2.imwrite("../images/houban_oee.png", img)
