from math import isclose

import cv2
import numpy as np

from jvi.drawing.color import Color
from jvi.image.image_nda import ImageNda


def value_map(img_1c: ImageNda) -> dict[int, float]:
    """获取图像分布"""
    assert img_1c.channel_num() == 1
    # https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
    # 参见：[Python numpy.histogram函数方法的使用](https://www.cjavapy.com/article/1103/)
    hist, edge = np.histogram(img_1c.data(), 256, (0, 255), density=True)
    print('hist1.shape:', hist.shape, edge.shape)

    m = {i: v for i, v in enumerate(hist) if v > 0}
    return m


def hue_hist(image: ImageNda, bins: int = 256) -> tuple[np.ndarray, np.ndarray]:
    """计算图像色度直方图"""

    hsv = cv2.cvtColor(image.data(), cv2.COLOR_BGR2HSV)
    hue = hsv[..., 0]

    hist, edge = np.histogram(hue, bins, (0, 255), density=True)
    return hist, edge


def hist_vector(image: ImageNda, bins: int = 256) -> np.ndarray:
    """获取图像分布向量"""

    hist, edge = np.histogram(image.data(), bins, (0, 255), density=True)
    hist *= edge[1] - edge[0]
    assert hist.shape == (bins,)
    assert isclose(np.sum(hist), 1)
    return hist


'''
from matplotlib import pyplot as plt

def show_hist(hist: np.ndarray, edge: np.ndarray, width_factor: float = 0.7) -> None:
    """
绘制直方图
"""
    width = width_factor * (edge[1] - edge[0])
    center = (edge[:-1] + edge[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.show()
"""


def calc_show_hist(image: ImageNda, bins: int = 128, width_factor: float = 0.7) -> None:
    """计算并绘制直方图"""

    hist, edge = np.histogram(image.data(), bins, (0, 255), density=True)

    show_hist(hist, edge, width_factor)
'''


def top_color_3c(_image: ImageNda, _ratio: float = 0.9) -> list[tuple[Color, float]]:
    """获取3通道图像前ratio颜色"""

    return []
