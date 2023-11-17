import sys
from copy import copy
from dataclasses import field, dataclass
from typing import TypeAlias, Optional

from jiv.geo.line_segment import LineSegments, LineSegment
from jiv.geo.point2d import Point, Points
from jiv.geo.rectangle import Rect
from jiv.geo.size2d import Size

Self: TypeAlias = 'Polygon'  # TODO: WAIT FOR 3.11


@dataclass
class Polygon:
    """多边形"""
    vertexes: Points = field(default_factory=list)

    @classmethod
    def by(cls, shape: Rect):
        pass

    def __len__(self) -> int:
        """获取节点数"""
        return len(self.vertexes)

    def at(self, i: int) -> Point:
        """获取指定索引的顶点，可回绕"""
        i = (i + len(self)) % len(self)
        return self.vertexes[i]

    def borders(self) -> LineSegments:
        """获取边界线段集"""
        ss = []
        for i in range(len(self)):
            ss.append(LineSegment(self.at(i), self.at(i + 1)))
        return ss

    def insert_best(self, p: Point) -> int:
        """插入一个顶点，保证多边形离原有几点最近，且不自相交，返回插入位置"""

        if len(self) < 3:
            self.vertexes.append(p)
            return len(self) - 1

        best_i = -1
        best_d = sys.float_info.max
        for i in range(len(self)):
            if self._check(p, i) or self._check(p, i + 1):
                continue
            d = p.dist(self.at(i)) + p.dist(self.at(i + 1))
            if d < best_d:
                best_d = d
                best_i = i + 1
        assert best_i >= 0
        self.vertexes.insert(best_i, p)
        return best_i

    def del_neighbors(self, p: Point) -> None:
        """删除一个顶点的两个邻居"""
        i = self.vertexes.index(p)
        neighbors = [self.vertexes[i - 1],
                     self.vertexes[(i + 1) % len(self.vertexes)]]
        for v in neighbors:
            if len(self.vertexes) > 1:
                self.vertexes.remove(v)

    def _check(self, p: Point, i: int) -> bool:
        """检查一点与指定顶点连线，是否与其他边相交"""
        p1 = self.at(i)
        line = LineSegment(p, p1)
        poly = self.polyline(i + 1, len(self) - 1)
        return line.intersects_polyline(poly)

    def polyline(self, start: int, size: int) -> Points:
        """从多边形上截取一段折线"""
        polygon = []
        for i in range(size):
            polygon.append(self.at(i + start))
        return polygon

    def is_normalized(self) -> bool:
        """判断坐标是否被归一化"""
        for p in self.vertexes:
            if not p.is_normalized():
                return False
        return True

    def normalize_me(self, size: Size) -> None:
        """绝对坐标归一化"""
        for p in self.vertexes:
            p.normalize_me(size)

    def normalize(self, size: Size) -> Self:
        """获取绝对坐标归一化"""
        p = copy(self)
        p.normalize_me(size)
        return p

    def absolutize_me(self, size: Size) -> None:
        """归一化坐标绝对化"""
        for p in self.vertexes:
            p.absolutize_me(size)
        self.round_me()

    def absolutize(self, size: Size) -> Self:
        """获取归一化坐标绝对化"""
        p = copy(self)
        p.absolutize_me(size)
        return p

    def round_me(self) -> None:
        """近似成整数"""
        for p in self.vertexes:
            p.round_me()

    def round(self) -> Self:
        """近似成整数"""
        s = copy(self)
        s.round_me()
        return s


def rect_polygon(rect: Rect) -> Optional[Polygon]:
    """长方形构造多边形"""
    return Polygon(rect.vertexes())


Polygons: TypeAlias = list[Polygon]
"""多边形集合"""
