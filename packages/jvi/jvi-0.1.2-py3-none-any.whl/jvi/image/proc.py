from typing import Optional

import cv2
import numpy as np
from jcx.m.number import Real1_2D
from jvi.drawing.color import Color
from jvi.geo.point2d import Points
from jvi.geo.rectangle import Rect
from jvi.geo.size2d import Size
from jvi.image.image_nda import ImageNda, ImageNdas
from jvi.image.util import make_mask, copy_mask


def resize(src: ImageNda,
           dst: Optional[ImageNda] = None,
           dst_size: Optional[Size] = None,
           scale: Optional[Real1_2D] = None) -> ImageNda:
    """缩放图片"""

    src_size = src.size()

    if dst_size is not None:
        assert isinstance(dst_size, Size)
        size = dst_size
    elif scale is not None:
        size = src_size.scale(scale).round()
    elif dst is not None:
        assert isinstance(dst, ImageNda)
        size = dst.size()
    else:
        raise RuntimeError('Invalid dst_size/scale argument')

    if dst:
        assert dst.same_channel_num(src)
    dst = cv2.resize(src.data(), size.round().to_tuple_int(), dst and dst.data())
    assert isinstance(dst, np.ndarray)
    return ImageNda(data=dst)


def resize_roi(src: ImageNda, rect: Rect, size: Optional[Size], dst: Optional[ImageNda]) -> ImageNda:
    """获取图像区域并缩放到指定尺寸"""
    size = size or (dst and dst.size())
    roi: ImageNda = src.roi(rect)
    dst = resize(roi, dst, size)
    return dst


def resize_to_box(src: ImageNda, dst_box: ImageNda) -> ImageNda:
    """图像缩放, 保持宽高比, 放入目标图像内"""
    dst_size = src.size().scale_in(dst_box.size()).round()
    rect = Rect.from_cs(dst_box.size().center(), dst_size)
    resize(src, dst_box.roi(rect))
    return dst_box


def tile(src_images: ImageNdas, cols: int = 0, box_size: Size = Size()) -> ImageNda:
    """多个图像平铺合并成一个"""
    cols = cols or len(src_images)
    rows = (len(src_images) + cols - 1) // cols
    if not box_size:
        tile_size = Size()
        for im in src_images:
            tile_size |= im.size()
        box_size = tile_size.scale((cols, rows))

    dst_image = ImageNda(box_size)
    tiles = dst_image.to_tiles(cols, rows)

    for src, dst in zip(src_images, tiles):
        if src.channel_num() == 1:
            src = to_color(src)  # 灰度图转彩色
        resize_to_box(src, dst)

    return dst_image


def get_roi_image(src: ImageNda, region: Optional[Points], background: Optional[Color] = None) -> ImageNda:
    """获取图片ROI图片"""
    size = src.size()
    region = region or Rect.one().vertexes()
    mask = make_mask(size, region)
    dst = ImageNda(size, color=background)
    copy_mask(src, mask, dst)
    return dst


def to_gray(src: ImageNda, dst: Optional[ImageNda] = None) -> ImageNda:
    """彩色图片抓换成灰度图"""
    assert src.channel_num() == 3

    dst_data = cv2.cvtColor(src.data(), cv2.COLOR_BGR2GRAY, dst and dst.data())
    return ImageNda(data=dst_data)


def to_color(src: ImageNda, dst: Optional[ImageNda] = None) -> ImageNda:
    """灰度图转为彩色图片"""
    assert src.channel_num() == 1

    dst_data = cv2.cvtColor(src.data(), cv2.COLOR_GRAY2BGR, dst and dst.data())
    return ImageNda(data=dst_data)


def merge(channels: ImageNdas) -> ImageNda:
    """合并通道成图像"""
    cs = [c.data() for c in channels]
    return ImageNda(data=cv2.merge(cs))


def split(image: ImageNda) -> ImageNdas:
    """合并通道成图像"""
    cs = cv2.split(image.data())
    return [ImageNda(data=c) for c in cs]


def laplacian_edge(src: ImageNda, dst: Optional[ImageNda] = None) -> ImageNda:
    """获取拉普拉斯边缘图"""
    lap = cv2.Laplacian(src.data(), cv2.CV_16S)  # CV_8U 抛弃负数, 不可用
    lap = np.absolute(lap).astype('uint8')
    im = ImageNda(data=lap)
    if dst is None:
        dst = im
    else:
        im.copy_to(dst)
    return dst


def blur(src: ImageNda, dst: Optional[ImageNda] = None, ksize: tuple[int, int] = (3, 3)) -> ImageNda:
    """图像模糊"""
    if dst is not None:
        assert src.same_shape_type(dst)
        dst = cv2.blur(src.data(), ksize, dst.data())
    else:
        dst = cv2.blur(src.data(), ksize)
    assert isinstance(dst, np.ndarray)
    return ImageNda(data=dst)


def erode(src: ImageNda, dst: Optional[ImageNda] = None, ksize: tuple[int, int] = (3, 3)) -> ImageNda:
    """图像腐蚀"""
    kernel = np.ones(ksize, np.uint8)
    if dst is not None:
        assert src.same_shape_type(dst)
        dst = cv2.erode(src.data(), kernel, dst.data())
    else:
        dst = cv2.erode(src.data(), kernel)
    assert isinstance(dst, np.ndarray)
    return ImageNda(data=dst)


def dilate(src: ImageNda, dst: Optional[ImageNda] = None, ksize: tuple[int, int] = (3, 3)) -> ImageNda:
    """图像碰撞"""
    kernel = np.ones(ksize, np.uint8)
    if dst is not None:
        assert src.same_shape_type(dst)
        dst = cv2.dilate(src.data(), kernel, dst.data())
    else:
        dst = cv2.dilate(src.data(), kernel)
    assert isinstance(dst, np.ndarray)
    return ImageNda(data=dst)


def threshold(src: ImageNda, thresh: int, dst: Optional[ImageNda] = None, max_value: int = 255,
              thr_type: int = cv2.THRESH_BINARY) -> ImageNda:
    """图像二值化, x > thresh"""
    if dst is not None:
        assert src.same_shape_type(dst)
        r, dst = cv2.threshold(src.data(), thresh, max_value, thr_type, dst.data())
    else:
        r, dst = cv2.threshold(src.data(), thresh, max_value, thr_type)
    assert isinstance(dst, np.ndarray)
    return ImageNda(data=dst)


def threshold_range(src: ImageNda, thr_range: tuple[int, int], dst: Optional[ImageNda] = None,
                    max_value: int = 255) -> ImageNda:
    """图像二值化, thr_range[0] < x <= thr_range[1]"""
    assert src.channel_num() == 1, '输入图像必须为灰度图'
    dst = threshold(src, thr_range[1], dst, 0, cv2.THRESH_TOZERO_INV)  # 高过阈值的部分设置为0
    dst = threshold(dst, thr_range[0], dst, max_value, cv2.THRESH_BINARY)
    return dst


def equalize_hist(src: ImageNda, dst: Optional[ImageNda] = None) -> ImageNda:
    """图像腐蚀"""
    data_dst = None
    if dst is not None:
        assert src.same_shape_type(dst)
        data_dst = dst.data()

    match src.channel_num():
        case 1:
            data_dst = cv2.equalizeHist(src.data(), data_dst)
        case 3:
            yuv = cv2.cvtColor(src.data(), cv2.COLOR_BGR2YUV)
            yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
            data_dst = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        case _:
            raise RuntimeError('Invalid image channel number')
    assert isinstance(data_dst, np.ndarray)
    return ImageNda(data=data_dst)


def alpha_blend(im_src: ImageNda, im_dst: ImageNda, alpha: ImageNda) -> None:
    """图像alpha混合"""
    assert im_src.same_shape_type(im_dst)
    assert im_src.channel_at(0).same_shape(alpha)

    a = alpha.data() / 255
    b = 1 - a

    for i in range(im_src.channel_num()):
        c1 = im_src.channel_at(i).data()
        c2 = im_dst.channel_at(i).data()
        c2[:, :] = c1 * a + c2 * b


def canny(src: ImageNda, thr1: int = 100, thr2: int = 200, dst: Optional[ImageNda] = None) -> ImageNda:
    if dst is not None:
        assert dst.channel_num() == 1
        assert dst.same_size(src)

    if src.channel_num() == 3:
        gray = to_gray(src)
    elif src.channel_num() == 1:
        gray = src
    else:
        raise Exception("not implemented")

    dst_data = cv2.Canny(gray.data(), thr1, thr2, dst and dst.data())
    return ImageNda(data=dst_data)
