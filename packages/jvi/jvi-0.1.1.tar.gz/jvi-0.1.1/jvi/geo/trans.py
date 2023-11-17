from typing import Iterable

from jiv.geo.point2d import Point, Points
from jiv.geo.rectangle import Rect
from jiv.geo.size2d import Size


def point_cs_trans_in_size(point: Point, src_cs: Size, dst_cs: Size) -> Point:
    """点变换坐标系-坐标系缩放, 点未归一化"""
    x = point.x * dst_cs.width / src_cs.width
    y = point.y * dst_cs.height / src_cs.height
    return Point(x, y)


def point_cs_trans_in_rect(point: Point, src_cs: Rect, dst_cs: Rect) -> Point:
    """点变换坐标系-区域到区域, 点未归一化"""
    return point_cs_trans_in_size(point - src_cs.lt(), src_cs.size(), dst_cs.size()) + dst_cs.lt()


def points_cs_trans_in_rect(points: Iterable[Point], src_cs: Rect, dst_cs: Rect) -> Points:
    """点变换坐标系-区域到区域, 点未归一化"""
    return [point_cs_trans_in_rect(p, src_cs, dst_cs) for p in points]


def rect_cs_trans_in_size(rect: Rect, src_cs: Size, dst_cs: Size) -> Rect:
    """矩形变换坐标系-区域到区域, 点未归一化"""
    x = rect.x * dst_cs.width / src_cs.width
    y = rect.y * dst_cs.height / src_cs.height
    w = rect.width * dst_cs.width / src_cs.width
    h = rect.height * dst_cs.height / src_cs.height
    return Rect(x, y, w, h)
