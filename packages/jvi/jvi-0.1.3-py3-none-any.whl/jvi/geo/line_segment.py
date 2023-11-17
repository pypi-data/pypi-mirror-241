from copy import copy
from dataclasses import field, dataclass
from typing import TypeAlias

from jvi.geo.point2d import Point, Points

Self: TypeAlias = 'LineSegment'  # TODO: WAIT FOR 3.11


@dataclass
class LineSegment:
    """线段"""
    start: Point = field(default_factory=Point)
    end: Point = field(default_factory=Point)

    def clone(self) -> Self:
        """克隆对象"""
        return copy(self)

    def cross(self, p: Point):
        """跨立实验"""
        p1 = self.end - self.start
        p2 = p - self.start
        return p1.x * p2.y - p2.x * p1.y

    def intersects(self, other) -> bool:
        """判断线段是否与另一相交"""
        c1 = self.cross(other.start) * self.cross(other.end)
        c2 = other.cross(self.start) * other.cross(self.end)
        return c1 <= 0 and c2 <= 0

    def intersects_polyline(self, polyline: Points) -> bool:
        """判断线段是否与折线相交"""
        for i in range(len(polyline) - 1):
            p1 = polyline[i]
            p2 = polyline[i + 1]
            if self.intersects(LineSegment(p1, p2)):
                return True
        return False


def line_segment(x1, y1, x2, y2) -> LineSegment:
    """从坐标值构造"""
    return LineSegment(Point(x1, y1), Point(x2, y2))


LineSegments: TypeAlias = list[LineSegment]
