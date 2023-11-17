import math
from copy import copy
from dataclasses import dataclass
from typing import TypeAlias, Sequence, Iterable, Protocol

import cv2
import numpy as np
from jcx.m import number
from jcx.m.number import Real1_2D, real_2d
from jiv.geo import is_normalized
from jiv.geo.protocol import PSize2D

Self: TypeAlias = 'Point'


@dataclass
class Point:
    """二维点"""
    x: float = 0
    y: float = 0

    @classmethod
    def zero(cls) -> Self:
        return Point()

    @classmethod
    def one(cls) -> Self:
        return Point(1, 1)

    def __bool__(self) -> bool:
        """判定是否存在非零属性"""
        return bool(self.x or self.y)

    def clone(self) -> Self:
        """克隆对象"""
        return copy(self)

    def round_me(self) -> None:
        """近似成整数"""
        self.x = round(self.x)
        self.y = round(self.y)

    def round(self) -> Self:
        """近似成整数"""
        p = self.clone()
        p.round_me()
        return p

    def align_round_me(self, align: int) -> None:
        """近似对齐"""
        self.x = number.align_round(self.x, align)
        self.y = number.align_round(self.y, align)

    def align_round(self, align: int) -> Self:
        """近似对齐"""
        p = self.clone()
        p.align_round_me(align)
        return p

    def scale_me(self, n: Real1_2D) -> None:
        """缩放指定的倍数"""
        x, y = real_2d(n)
        self.x *= x
        self.y *= y

    def scale(self, n: Real1_2D) -> Self:
        """获取缩放指定的倍数的新对象"""
        p = self.clone()
        p.scale_me(n)
        return p

    def normalize_me(self, size: PSize2D) -> None:
        """绝对坐标归一化"""
        self.x /= size.width
        self.y /= size.height

    def normalize(self, size: PSize2D) -> Self:
        """获取绝对坐标归一化"""
        p = copy(self)
        p.normalize_me(size)
        return p

    def is_normalized(self) -> bool:
        """判断坐标是否被归一化"""
        return is_normalized(self.x) and is_normalized(self.y)

    def absolutize_me(self, size: PSize2D) -> None:
        """归一化坐标绝对化"""
        self.x = round(self.x * size.width)
        self.y = round(self.y * size.height)

    def absolutize(self, size: PSize2D) -> Self:
        """获取归一化坐标绝对化"""
        p = copy(self)
        p.absolutize_me(size)
        return p

    def to_tuple(self) -> tuple[float, float]:
        """获取tuple"""
        return self.x, self.y

    def to_tuple_int(self) -> tuple[int, int]:
        """获取tuple"""
        return int(self.x), int(self.y)

    def dist2(self, p: Self) -> float:
        """获取点到点距离平方"""
        dx = self.x - p.x
        dy = self.y - p.y
        return dx * dx + dy * dy

    def dist(self, p: Self) -> float:
        """获取点到点距离"""
        return math.sqrt(self.dist2(p))

    def __add__(self, p: Self) -> Self:
        """点相加"""
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: Self) -> Self:
        """点相减"""
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p: Self) -> Self:
        """点相乘"""
        return Point(self.x * p.x, self.y * p.y)

    def dist_polygon(self, polygon: Sequence[Self]) -> float:
        """点到多边形距离, 返回值: 正数-点在多边形**内部**, 0-点在多边形边上, 负数-点在多边形**外部**"""
        ps = [p.to_tuple() for p in polygon]
        ps1 = np.asarray(ps, dtype=np.float32)
        d = cv2.pointPolygonTest(ps1, self.to_tuple(), True)
        assert isinstance(d, float)
        return d

    def inside(self, polygon: Sequence[Self]) -> bool:
        """判定点是否在多边形内部"""
        return self.dist_polygon(polygon) > 0

    def outside(self, polygon: Sequence[Self]) -> bool:
        """判定点是否在多边形内部"""
        return self.dist_polygon(polygon) < 0


Points: TypeAlias = list[Point]
"""点集定义"""


def rect_vertexes(x1: float, y1: float, x2: float, y2: float) -> Points:
    """生成矩形顶点点集"""
    return [Point(x1, y1), Point(x2, y1), Point(x2, y2), Point(x1, y2)]


class Normalized(Protocol):
    def is_normalized(self) -> bool:
        pass


def array_is_normalized(arr: Iterable[Normalized]) -> bool:
    """判断数组是否归一化"""
    for e in arr:
        if not e.is_normalized():
            return False
    return True


def array_absolutize(points: Iterable[Point], size: PSize2D) -> Points:
    """数组元素绝对化"""
    return [e.absolutize(size) for e in points]


def array_normalize(points: Iterable[Point], size: PSize2D, offset: Point = Point()) -> Points:
    """数组元素归一化"""
    return [(p + offset).normalize(size) for p in points]


def closest_point(point: Point, points: Points) -> tuple[float, Point]:
    """获取点到点集的最近距离"""
    assert len(points) > 0
    p1 = points[0]
    d2_min = point.dist2(p1)
    for p in points:
        d2 = point.dist2(p)
        if d2 < d2_min:
            d2_min = d2
            p1 = p

    return d2_min, p1


def insert_closest(arr: Points, p: Point, new_p: Point) -> None:
    """在点集中p点前或后插入点，距离p的前一个点近，则插入p前，否则插入p后"""
    assert len(arr) > 0
    i = arr.index(p)
    i2 = (i + 1) % len(arr)
    d1 = new_p.dist2(arr[i - 1])
    d2 = new_p.dist2(arr[i2])
    pos = i if d1 < d2 else i2
    arr.insert(pos, new_p)
