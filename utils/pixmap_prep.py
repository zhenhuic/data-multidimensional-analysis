import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage


def draw_Chinese_words(img_array, contents, coord, color=(255, 255, 255), size=40):
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img_array)

    # PIL图片上打印汉字
    draw = ImageDraw.Draw(img)  # 图片上打印
    font = ImageFont.truetype("simhei.ttf", size, encoding="utf-8")
    draw.text(coord, contents, color, font=font)

    # PIL 图片转 cv2 图片
    img_array = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img_array


def draw_triangle_center(img_array, side_length, color=(255, 255, 255)):
    img = img_array.copy()
    height, width, _ = img_array.shape
    x, y = int(width / 2), int(height / 2)  # 中心点坐标
    points = [(x - int(side_length * 0.2887), y - int(side_length / 2)),
              (x - int(side_length * 0.2887), y + int(side_length / 2)),
              (x + int(side_length * 0.5773), y)]
    triangle_array = np.array(points)
    img = cv2.drawContours(img, [triangle_array], 0, color, -1)
    return img


def draw_rectangle_center(img_array, side_length, color=(255, 255, 255)):
    img = img_array.copy()
    height, width, _ = img_array.shape
    x, y = int(width / 2), int(height / 2)  # 中心点坐标
    top_left = (x - int(side_length / 2), y - int(side_length / 2))
    bottom_right = (x + int(side_length / 2), y + int(side_length / 2))
    rect = cv2.rectangle(img, top_left, bottom_right, color, -1)
    return rect


def darken(img_array, rate):
    """
    使图像变暗
    :param img_array:
    :param rate: float, 变暗的比率(0 - 1)
    :return:
    """
    img = img_array.copy()
    mask = np.zeros_like(img)
    dim = cv2.addWeighted(img, (1 - rate), mask, rate, 0)
    return dim


def array_to_QImage(img, size):
    img_array = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, ch = img_array.shape
    bytes_per_line = ch * w
    qimage = QImage(img_array.data, w, h, bytes_per_line, QImage.Format_RGB888)
    if isinstance(size, QSize):
        qimage = qimage.scaled(size)
    else:
        qimage = qimage.scaled(size[0], size[1])
    return qimage


def images_prep_factory(label_images_dict: dict, projects_view_name_dict: dict):
    prep_images_dict = {}
    for name, img_path in label_images_dict.items():
        if img_path is not None and img_path != "":
            prep_images = []
            orig = cv2.imread(img_path)
            if orig is None:
                prep_images_dict[name] = None
                break

            dark = darken(orig, 0.5)
            dark = draw_Chinese_words(dark, projects_view_name_dict[name], (20, 400))
            prep_images.append(dark)

            tri = draw_triangle_center(orig, 65, (0, 255, 0))
            tri = draw_Chinese_words(tri, projects_view_name_dict[name], (20, 400))
            prep_images.append(tri)

            rect = draw_rectangle_center(orig, 60, (0, 0, 255))
            rect = draw_Chinese_words(rect, projects_view_name_dict[name], (20, 400))
            prep_images.append(rect)

            prep_images_dict[name] = prep_images
        else:
            prep_images_dict[name] = None

    return prep_images_dict


if __name__ == '__main__':
    orig = cv2.imread("../images/intrusion.jpg")

    tri = draw_triangle_center(orig, 65, (0, 255, 0))
    tri = draw_Chinese_words(tri, "智能安全监测系统", (20, 400))

    dark = darken(orig, 0.5)
    dark = draw_Chinese_words(dark, "智能安全监测系统", (20, 400))

    rect = draw_rectangle_center(orig, 60, (0, 0, 255))
    rect = draw_Chinese_words(rect, "智能安全监测系统", (20, 400))

    cv2.imshow("orig", orig)
    cv2.imshow("tri", tri)
    cv2.imshow("rect", rect)
    cv2.imshow("dark", dark)
    cv2.waitKey(0)


