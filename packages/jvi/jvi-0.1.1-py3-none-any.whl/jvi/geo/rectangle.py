from copy import copy
from dataclasses import dataclass
from random import uniform
from typing import TypeAlias, Any, Protocol

from jcx.m.number import align_down, Real
from jiv.geo import to_zero
from jiv.geo.point2d import Point, Points
from jiv.geo.size2d import Size
from rustshed import Option, Null, Some

Self: TypeAlias = 'Rect'  # TODO: WAIT FOR 3.11


@dataclass
class Rect:
    """长方形"""

    x: float = 0
    y: float = 0
    width: float = 0
    height: float = 0

    @classmethod
    def zero(cls) -> Self:
        """长方形-空"""
        return Rect(0, 0, 0, 0)

    @classmethod
    def one(cls) -> Self:
        """长方形-归一化全图"""
        return Rect(0.0, 0.0, 1.0, 1.0)

    @classmethod
    def from_size(cls, s: Size) -> Self:
        """长方形-以Size构建"""
        return Rect(0, 0, s.width, s.height)

    @classmethod
    def from_ps(cls, p: Point, s: Size) -> Self:
        """长方形-以左上角和尺寸构建"""
        return Rect(p.x, p.y, s.width, s.height)

    @classmethod
    def from_ltrb(cls, p1: Point, p2: Point) -> Self:
        """长方形-以左上右下两点构建"""
        return Rect(p1.x, p1.y, p2.x - p1.x, p2.y - p1.y)

    @classmethod
    def from_cs(cls, center: Point, size: Size) -> Self:
        """长方形-以中心坐标+尺寸构建"""
        return Rect.from_cs_list(center.x, center.y, size.width, size.height)

    @classmethod
    def from_cs_list(cls, cx: float, cy: float, width: float, height: float) -> Self:
        """长方形-以中心坐标+尺寸构建"""
        return Rect(to_zero(cx - width / 2), to_zero(cy - height / 2), width, height)

    @classmethod
    def from_oi(cls, outer: Size, inner: Size) -> Self:
        """以外部长方形的中心为中心-以及内部尺寸为尺寸+尺寸构建"""
        center = Point(outer.width / 2, outer.height / 2)
        return Rect.from_cs(center, inner)

    def cs(self) -> tuple[Point, Size]:
        """获取中心+尺寸"""
        return self.center(), self.size()

    def cs_list(self) -> list[Real]:
        """获取中心+尺寸"""
        return [self.x + self.width / 2, self.y + self.height / 2, self.width, self.height]

    @classmethod
    def from_ltrb_list(cls, ll: list) -> Self:
        """长方形-以左上右下两点坐标列表构建，即：[x1, y1, x2, y2]"""
        return Rect(ll[0], ll[1], ll[2] - ll[0], ll[3] - ll[1])

    @classmethod
    def try_bounding(cls, points: Points) -> Option[Self]:
        """点集的外包长方形"""
        if len(points) < 1:
            return Null
        p1 = copy(points[0])
        p2 = copy(p1)
        for p in points:
            p1.x = min(p1.x, p.x)
            p1.y = min(p1.y, p.y)
            p2.x = max(p2.x, p.x)
            p2.y = max(p2.y, p.y)
        return Some(Rect.from_ltrb(p1, p2))

    @classmethod
    def bounding(cls, points: Points) -> Self:
        """点集的外包长方形"""
        return cls.try_bounding(points).unwrap()

    def __bool__(self) -> bool:
        """判定是否存在非零属性"""
        return self != Rect()

    def center(self) -> Point:
        """获取中心坐标"""
        return Point(self.x + self.width / 2, self.y + self.height / 2)

    def center_rect(self, size: Size) -> Self:
        """获取同心矩形"""
        return Rect.from_cs(self.center(), size)

    def size(self) -> Size:
        """获取尺寸"""
        return Size(self.width, self.height)

    def area(self) -> Real:
        """获取面积"""
        return self.width * self.height

    def aspect_ratio(self) -> Real:
        """获取纵横比"""
        return self.height / self.width

    def right(self) -> Real:
        """获取右侧值"""
        return self.x + self.width

    def bottom(self) -> Real:
        """获取底部值"""
        return self.y + self.height

    def lt(self) -> Point:
        """获取左上点"""
        return Point(self.x, self.y)

    def rt(self) -> Point:
        """获取右上点"""
        return Point(self.x + self.width, self.y)

    def rb(self) -> Point:
        """获取右下点"""
        return Point(self.x + self.width, self.y + self.height)

    def lb(self) -> Point:
        """获取左下点"""
        return Point(self.x, self.y + self.height)

    def ltrb(self) -> tuple[Point, Point]:
        """获取左上右下两点坐标"""
        return self.lt(), self.rb()

    def ltrb_tuple(self) -> tuple[tuple[float, float], tuple[float, float]]:
        """获取左上右下两点坐标 - tuple 表示"""
        return self.lt().to_tuple(), self.rb().to_tuple()

    def ltrb_tuple_int(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """获取左上右下两点坐标 - tuple 表示"""
        return self.lt().to_tuple_int(), self.rb().to_tuple_int()

    def ltrb_list(self) -> list[Real]:
        """获取左上右下两点坐标列表"""
        return [self.x, self.y, self.x + self.width, self.y + self.height]

    def to_tuple_int(self) -> tuple[int, int, int, int]:
        """获取数据的tuple表示"""
        return int(self.x), int(self.y), int(self.width), int(self.height)

    def vertexes(self) -> Points:
        """获取四个定点坐标"""
        return [self.lt(), self.rt(), self.rb(), self.lb()]

    def clone(self) -> Self:
        """克隆对象"""
        return copy(self)

    def normalize_me(self, size: Size) -> None:
        """绝对坐标归一化"""
        self.x /= size.width
        self.y /= size.height
        self.width /= size.width
        self.height /= size.height

    def normalize(self, size: Size) -> Self:
        """获取绝对坐标归一化"""
        r = copy(self)
        r.normalize_me(size)
        return r

    def is_normalized(self) -> bool:
        """判断坐标是否被归一化"""
        p1, p2 = self.ltrb()
        return p1.is_normalized() and p2.is_normalized()

    def absolutize_me(self, size: Size) -> None:
        """归一化坐标绝对化"""
        self.x = round(self.x * size.width)
        self.y = round(self.y * size.height)
        self.width = round(self.width * size.width)
        self.height = round(self.height * size.height)

    def absolutize(self, size: Size) -> Self:
        """获取绝对坐标归一化对象"""
        r = copy(self)
        r.absolutize_me(size)
        return r

    def to_origin(self) -> Self:
        """产生新矩形: 左上角移动到原点"""
        return Rect.from_size(self.size())

    def scale_me(self, n: Real) -> None:
        """缩放指定的倍数"""
        self.x *= n
        self.y *= n
        self.width *= n
        self.height *= n

    def scale(self, n: Real) -> Self:
        """获取缩放指定的倍数的新对象"""
        r = self.clone()
        r.scale_me(n)
        return r

    def dilate_me(self, n: Real) -> None:
        """向四边膨胀指定值"""
        self.x -= n
        self.y -= n
        self.width += n * 2
        self.height += n * 2

    def dilate(self, n: Real) -> Self:
        """向四边膨胀指定值"""
        r = copy(self)
        r.dilate_me(n)
        return r

    def erode_me(self, n: Real) -> None:
        """向四边腐蚀指定值"""
        self.dilate_me(-n)

    def erode(self, n: Real) -> Self:
        """向四边腐蚀指定值"""
        return self.dilate(-n)

    def round_me(self) -> None:
        """近似成整数"""
        self.x = round(self.x)
        self.y = round(self.y)
        self.width = round(self.width)
        self.height = round(self.height)

    def round(self) -> Self:
        """近似成整数"""
        r = copy(self)
        r.round_me()
        return r

    def add_offset(self, offset: Point) -> None:
        """增加偏移量"""
        self.x += offset.x
        self.y += offset.y

    def contains_point(self, p: Point) -> bool:
        """判定矩形是否包含点"""
        rb = self.rb()
        return self.x <= p.x < rb.x and self.y <= p.y < rb.y

    def contains_rect(self, r: Self) -> bool:
        """判定矩形是否包含矩形"""
        p = r.rb()
        rb = self.rb()
        return self.contains_point(r.lt()) and self.x <= p.x <= rb.x and self.y <= p.y <= rb.y

    def contains(self, v: Any) -> bool:
        """判定矩形是否包含对象"""
        if isinstance(v, Point):
            return self.contains_point(v)
        if isinstance(v, Rect):
            return self.contains_rect(v)
        return False

    def intersect(self, r: Self) -> Self:
        """获取矩形交集矩形"""
        a, b = self.ltrb()
        c, d = r.ltrb()
        x1 = max(a.x, c.x)
        y1 = max(a.y, c.y)
        x2 = min(b.x, d.x)
        y2 = min(b.y, d.y)

        return Rect.from_ltrb_list([x1, y1, x2, y2])

    def unite(self, r: Self) -> Self:
        """获取矩形并集矩形"""
        a, b = self.ltrb()
        c, d = r.ltrb()
        x1 = min(a.x, c.x)
        y1 = min(a.y, c.y)
        x2 = max(b.x, d.x)
        y2 = max(b.y, d.y)

        return Rect.from_ltrb_list([x1, y1, x2, y2])

    def to_tiles(self, cols: int = 0, rows: int = 0, size: Size = Size(), need_round: bool = False) \
            -> list[Self]:
        """把长方形切成瓦片"""
        assert (not cols) == (not rows)  # col/row 存在性一致
        assert (not cols) != (not size)  # col/size 存在性不同

        if cols:
            dx = self.width / cols
            dy = self.height / rows
        else:
            assert size
            dx = size.width
            dy = size.height
            cols = int(self.width / dx)
            rows = int(self.height / dy)

        rs = []
        for y in range(rows):
            for x in range(cols):
                r = Rect(self.x + x * dx, self.y + y * dy, dx, dy)
                if need_round:
                    r.round_me()
                rs.append(r)
        return rs

    def to_center_tiles(self, size: Size) -> list[Self]:
        """把长方形切成指定尺寸瓦片, 中心对称, 超出边界部分舍弃"""
        assert not self.is_normalized()
        assert not size.is_normalized()
        w = align_down(int(self.width), int(size.width))
        h = align_down(int(self.height), int(size.height))
        r = Rect.from_cs(self.center(), Size(w, h))
        return r.to_tiles(size=size)


Rects: TypeAlias = list[Rect]
"""长方形组"""


class PHasRect(Protocol):
    """可获取Rect类型"""

    def rect(self) -> Rect:
        """获取对象Rect"""
        pass


def letterbox(src: Size, dst: Size) -> Rect:
    """信封盒，把一个尺寸不改变宽高比，映射到新尺寸中的一个区域"""
    r = min(dst.width / src.width, dst.height / src.height)
    s = src.scale(r)
    return Rect.from_cs_list(dst.width / 2, dst.height / 2, s.width, s.height).round()


def center_tile_rect(size: Size, tile_side: int, row: int, col: int) -> Rect:
    """"计算瓦片所在矩形区域"""

    x = (size.width - col * tile_side) / 2
    y = (size.height - row * tile_side) / 2

    return Rect(x, y, col * tile_side, row * tile_side)


def point_trans(p: Point, r: Rect) -> Point:
    """点坐标变换到目标区域内归一化坐标"""
    x = (p.x - r.x) / r.width
    y = (p.y - r.y) / r.height
    return Point(x, y)


def points_trans(ps: Points, r: Rect) -> Points:
    """点集坐标变换到目标区域内归一化坐标"""
    return [point_trans(p, r) for p in ps]


def random_point(range_: Size | Rect) -> Point:
    """获取指定范围内的随机点"""
    if isinstance(range_, Size):
        r = Rect.from_size(range_)
    elif isinstance(range_, Rect):
        r = range_
    else:
        raise 'Invalid range type'
    x = uniform(r.x, r.right())
    y = uniform(r.y, r.bottom())
    return Point(x, y)
