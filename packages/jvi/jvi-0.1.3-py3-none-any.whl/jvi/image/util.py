from typing import Optional

import cv2
import numpy as np
from jvi.drawing.color import Color
from jvi.geo.point2d import Points, Point
from jvi.geo.rectangle import Rect
from jvi.geo.size2d import absolutize_points, Size
from jvi.image.image_nda import ImageNda, new_gray, ImageNdas


def np_shape(size: Size) -> tuple[int, int]:
    """Size转化成numpy形状"""
    return int(size.height), int(size.width)


def points_to_mat(roi: Points) -> np.ndarray:
    """点集转换为mat"""
    arr = [[p.x, p.y] for p in roi]
    # print('arr', arr)
    return np.array([arr], dtype=np.int32)


def mat_to_points(mat: np.ndarray) -> Points:
    """mat转换为点集"""
    mat = mat.reshape(-1, 2)
    return [Point(p[0], p[1]) for p in mat]


def make_mask(size: Size, roi: Points, mask: Optional[ImageNda] = None) -> ImageNda:
    """制造指定ROI掩码图"""
    shape = (size.height, size.width)
    if isinstance(mask, ImageNda) and mask.shape() == shape:  # 已经存在尺寸合适mark,则返回
        return mask

    mask = new_gray(size)

    roi = absolutize_points(roi, size)
    roi_mat = points_to_mat(roi)

    cv2.fillPoly(mask.data(), roi_mat, 255)
    return mask


def make_roi_surround_color(img: ImageNda, roi: Points, channel: int = 0) -> None:
    """让图像指定ROI之外部分变成单通道颜色, 用以凸显ROI. channel: 0-蓝色, 1-绿色, 2-红色"""
    mask = make_mask(img.size(), roi)
    cv2.bitwise_not(mask.data(), mask.data())
    # cv2.imshow("mask", mask)

    gray = cv2.cvtColor(img.data(), cv2.COLOR_RGB2GRAY)
    blue = ImageNda(img.size())
    blue.data()[:, :, channel] = gray

    copy_mask(blue, mask, img)


def copy_mask(src: ImageNda, mask: ImageNda, dst: Optional[ImageNda] = None,
              bg_color: Optional[Color] = None) -> ImageNda:
    """根据mask复制"""
    if dst is None or not src.same_shape_type(dst):
        dst = ImageNda.new_as(src, color=bg_color)
    data = cv2.copyTo(src.data(), mask.data(), dst.data())
    return ImageNda(data=data)


def image_to_tiles(image: ImageNda, size: Size) -> ImageNdas:
    """获取ndarray瓦片图"""
    rs = Rect.from_size(image.size()).to_tiles(size=size)
    return [image.roi(r) for r in rs]
