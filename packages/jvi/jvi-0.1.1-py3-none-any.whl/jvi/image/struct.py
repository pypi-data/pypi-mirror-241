from dataclasses import dataclass, field
from typing import Optional, TypeAlias

import cv2
import numpy as np
from jiv.drawing.color import random_color
from jiv.drawing.shape import polylines
from jiv.geo.point2d import Point, Points, array_normalize
from jiv.geo.size2d import Size
from jiv.image.image_nda import ImageNda
from jiv.image.proc import to_gray, threshold_range, erode, resize, dilate, threshold
from jiv.image.trace import trace_images
from jiv.image.util import mat_to_points


@dataclass
class BoxObject:
    """盒子目标, TODO"""

    id: int = 0
    """"目标ID"""
    polygon: Points = field(default_factory=list)
    """目标范围"""
    area: float = 0
    """目标面积"""

    def normalize_me(self, size: Size) -> None:
        """归一化自身坐标 & 面积"""
        self.polygon = array_normalize(self.polygon, size)
        self.area = self.area / size.area()


BoxObjects: TypeAlias = list[BoxObject]
"""盒子目标集定义"""


def find_polygons(mask: ImageNda, min_area: float = 0, min_area_ratio: float = 0, epsilon: int = 13,
                  make_box: bool = False) -> BoxObjects:
    """
    图像中获取目标的外包多边形.

    Parameters
        -------
        mask: 二值化图像.

        min_area: 为最小面积.

        min_area_ratio: 为最小面积比率, 二者取其大

        epsilon: 多边形拟合步长

        make_box: True-拟合长方形, False-拟合多边形
    Returns
        -------
        out: 盒子目标集, 未归一化.

    """
    assert mask.channel_num() == 1
    full_area = mask.size().area()
    min_area = max(min_area, full_area * min_area_ratio)
    assert 0 <= min_area_ratio <= 1
    assert min_area >= 1
    # print('min_area:', min_area)

    contours, hierarchy = cv2.findContours(mask.data(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    objects: BoxObjects = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            continue
        if make_box:  # 拟合矩形
            rect = cv2.minAreaRect(contour)  # 输出浮点坐标
            box = cv2.boxPoints(rect)
            assert isinstance(box, np.ndarray)
            box1 = np.int0(box)
            assert isinstance(box1, np.ndarray)
            polygon = [Point(x, y) for x, y in box1]
        else:  # 拟合多边形
            approx1 = cv2.approxPolyDP(contour, epsilon, True)  # 拟合精确度
            polygon = mat_to_points(approx1)
        objects.append(BoxObject(0, polygon, area))
    return objects


@dataclass
class OscrParams:
    """多边形"""
    color_range: tuple[int, int] = (0, 0)
    """颜色范围, 默认使用OTSU自动阈值(目前全图范围效果不好, 可以实施ROI)"""
    ksize: tuple[int, int] = (7, 7)
    """开运算卷积核尺寸"""
    min_area_ratio: float = 1 / 64
    """目标最小面积比率, 计算得到的面积值会远小于感官, 该值不宜过大"""
    scale: float = 0.5
    """图像缩放比例"""


class OscrDetector:
    """特定颜色范围目标检测器(Objects with a Specific Color Range)"""

    def __init__(self, params: OscrParams = OscrParams()):
        self._color_range = params.color_range
        self._ksize = params.ksize
        self._min_area_ratio = params.min_area_ratio
        self._scale = params.scale

        self._im_color: Optional[ImageNda] = None  # 彩色图
        self._im_gray: Optional[ImageNda] = None  # 灰度图
        self._im_bin: Optional[ImageNda] = None  # 二值图
        self._objects: BoxObjects = []  # 检测到的目标

    def size(self) -> Size:
        """获取内部图像尺寸"""
        return self._im_color.size() if self._im_color else Size()

    def detect(self, image: ImageNda) -> BoxObjects:
        """灰度范围目标检测器, 返回归一化目标"""
        self._im_color = resize(image, self._im_color, scale=0.5)
        self._im_gray = to_gray(self._im_color, self._im_gray)

        if self._color_range == (0, 0):
            self._im_bin = threshold(self._im_gray, 0, self._im_bin, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        else:
            self._im_bin = threshold_range(self._im_gray, self._color_range, self._im_bin)
        erode(self._im_bin, self._im_bin, self._ksize)
        dilate(self._im_bin, self._im_bin, self._ksize)

        objects = find_polygons(self._im_bin, min_area_ratio=self._min_area_ratio)
        for ob in objects:
            ob.normalize_me(self._im_bin.size())
        self._objects = objects
        return self._objects

    def debug_images(self) -> None:
        """显示内部图片, 用于调试"""
        assert self._im_color and self._im_gray and self._im_bin
        for ob in self._objects:
            polylines(self._im_color, ob.polygon, random_color())
        trace_images([self._im_color, self._im_gray, self._im_bin], 'Infrared')
