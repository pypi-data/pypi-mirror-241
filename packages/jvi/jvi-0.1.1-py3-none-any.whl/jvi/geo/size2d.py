import re
from copy import copy
from dataclasses import dataclass
from typing import Optional, TypeAlias, Final

from jcx.m.number import real_2d, Real1_2D, Real
from jiv.geo import is_normalized
from jiv.geo.point2d import Points, Point

Self: TypeAlias = 'Size'  # TODO: WAIT FOR 3.11


@dataclass
class Size:
    """二维尺寸"""
    width: float = 0
    height: float = 0

    def size(self) -> Self:
        """实现ISize2D"""
        return self

    def __bool__(self) -> bool:
        """判定是否存在非零属性"""
        return self != Size()

    def brief(self) -> str:
        """获取简要描述"""
        return "{}x{}".format(self.width, self.height)

    def area(self) -> Real:
        """获取面积"""
        return self.width * self.height

    def empty(self) -> bool:
        """判定面积为零"""
        return self.area() == 0

    def positive(self) -> bool:
        """判定长宽为正"""
        return self.width > 0 and self.height > 0

    def center(self) -> Point:
        """获取中心坐标"""
        return Point(self.width / 2, self.height / 2)

    def aspect_ratio(self) -> float:
        """纵横比"""
        return self.height / self.width

    def contains(self, other: Self) -> bool:
        """是否包含目标尺寸"""
        return self.width >= other.width and self.height >= other.height

    def clone(self) -> Self:
        """克隆对象"""
        return copy(self)

    def set(self, other: Self) -> None:
        """设置为目标对象值"""
        self.width = other.width
        self.height = other.height

    def scale_me(self, n: Real1_2D) -> None:
        """缩放指定的倍数"""
        x, y = real_2d(n)
        self.width *= x
        self.height *= y

    def scale(self, n: Real1_2D) -> Self:
        """缩放指定的倍数"""
        s = self.clone()
        s.scale_me(n)
        return s

    def to_tuple(self) -> tuple[float, float]:
        """获取tuple"""
        return self.width, self.height

    def to_tuple_int(self) -> tuple[int, int]:
        """转换为tuple"""
        return int(self.width), int(self.height)

    def to_shape(self) -> tuple[int, int]:
        """转换为 2D Shape"""
        return int(self.height), int(self.width)

    def to_shape3d_i(self, channel: int) -> tuple[int, int, int]:
        """转换为 3D Shape交错格式"""
        return int(self.height), int(self.width), channel

    def to_shape3d_p(self, channel: int) -> tuple[int, int, int]:
        """转换为 3D Shape平坦格式"""
        return channel, int(self.height), int(self.width)

    def to_point(self) -> Point:
        """转换为Point"""
        return Point(self.width, self.height)

    def normalize_me(self, size: Self) -> None:
        """绝对坐标归一化"""
        self.width /= size.width
        self.height /= size.height

    def normalize(self, size: Self) -> Self:
        """获取绝对坐标归一化"""
        p = copy(self)
        p.normalize_me(size)
        return p

    def absolutize_me(self, size: Self) -> None:
        """归一化坐标绝对化"""
        self.width *= size.width
        self.height *= size.height
        self.round_me()  # 存在非整数可能

    def absolutize(self, size: Self) -> Self:
        """获取归一化坐标绝对化"""
        p = copy(self)
        p.absolutize_me(size)
        return p

    def round_me(self) -> None:
        """近似成整数"""
        self.width = round(self.width)
        self.height = round(self.height)

    def round(self) -> Self:
        """近似成整数"""
        s = copy(self)
        s.round_me()
        return s

    def is_normalized(self) -> bool:
        """判断坐标是否被归一化"""
        return is_normalized(self.width) and is_normalized(self.height)

    def __mul__(self, s: Self) -> Self:
        """尺寸相乘"""
        return Size(self.width * s.width, self.height * s.height)

    def __truediv__(self, s: Self) -> Self:
        """尺寸相除"""
        return Size(self.width / s.width, self.height / s.height)

    def __or__(self, s: Self) -> Self:
        """尺寸并集"""
        return Size(max(self.width, s.width), max(self.height, s.height))

    def __and__(self, s: Self) -> Self:
        """尺寸并集"""
        return Size(min(self.width, s.width), min(self.height, s.height))

    def scale_in(self, box_size: Self) -> Self:
        """保证宽高比缩放到指定尺寸以内"""
        rx = box_size.width / self.width
        ry = box_size.height / self.height
        r = min(rx, ry)

        w = self.width * r
        h = self.height * r
        return Size(w, h)


def absolutize_points(points: Points, size: Size) -> Points:
    """点集归一化坐标绝对化"""
    arr = [p.absolutize(size) for p in points]
    return arr


# 参考：https://zh.wikipedia.org/wiki/%E6%98%BE%E7%A4%BA%E5%88%86%E8%BE%A8%E7%8E%87%E5%88%97%E8%A1%A8

SIZE_8K: Final = Size(8192, 4320)
SIZE_8K_UHD: Final = Size(7680, 4320)
SIZE_DCI_4K: Final = Size(4096, 2160)
SIZE_4K_UHD: Final = Size(3840, 2160)
SIZE_3K: Final = Size(2880, 1620)
SIZE_2K: Final = Size(2048, 1080)
SIZE_FHD: Final = Size(1920, 1080)
SIZE_qHD: Final = Size(960, 540)
SIZE_HD_PLUS: Final = Size(1600, 900)
SIZE_HD: Final = Size(1280, 720)
SIZE_nHD: Final = Size(640, 360)
SIZE_VGA: Final = Size(640, 480)
SIZE_QVGA: Final = Size(320, 240)
SIZE_PAL: Final = Size(768, 576)
SIZE_IM: Final = Size(224, 224)

SIZE_640: Final = Size(640, 640)
"""深度学习检测器常规尺寸"""
SIZE_720: Final = Size(720, 720)
"""深度学习检测器常规尺寸"""
SIZE_1280: Final = Size(1280, 1280)
"""深度学习检测器常规尺寸"""

resolutions: Final = {
    '8K': SIZE_8K,
    '8K_UHD': SIZE_8K_UHD,
    'DCI_4K': SIZE_DCI_4K,
    '4K_UHD': SIZE_4K_UHD,
    '3K': SIZE_3K,
    '2K': SIZE_2K,
    'FHD': SIZE_FHD,
    'qHD': SIZE_qHD,
    'HD+': SIZE_HD_PLUS,
    'HD': SIZE_HD,
    'nHD': SIZE_nHD,
    'VGA': SIZE_VGA,
    'QVGA': SIZE_QVGA,
    'PAL': SIZE_PAL,
    'IM': SIZE_IM,
}


def size_parse(s: str) -> Optional[Size]:
    """解析字符串获取尺寸"""

    size = resolutions.get(s)
    if size:
        return size

    p = re.compile(r"(\d+)x(\d+)")
    m = p.match(s.lower())
    if m:
        w = int(m.groups()[0])
        h = int(m.groups()[1])
        size = Size(w, h)
    else:
        size = None
    return size
