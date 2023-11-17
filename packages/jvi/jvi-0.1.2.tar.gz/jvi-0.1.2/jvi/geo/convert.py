from collections.abc import Iterable

from jvi.geo.point2d import Point, Points
from jvi.geo.size2d import Size
from rustshed import Result, Err, Ok


def to_point(p: Point | Size | list | tuple) -> Result[Point, str]:
    """类型转换成Point，接受类型"""
    if isinstance(p, Point):
        return Ok(p)
    if isinstance(p, Size):
        return Ok(Point(p.width, p.height))
    if (isinstance(p, list) or isinstance(p, tuple)) and len(p) == 2:
        return Ok(Point(p[0], p[1]))
    return Err('[ERR] type %s cannot convert to Point' % type(p))


def to_points(points: Iterable) -> Result[Points, str]:
    """转换成点集"""
    if not isinstance(points, Iterable):
        return Err('[ERR] type %s is not iterable' % type(points))
    ps = []
    for p in points:
        p = to_point(p)
        if p.is_err():
            return p
        ps.append(p.unwrap())
    return Ok(ps)


def to_size(s: Size | Point | list | tuple) -> Result[Size, str]:
    """类型转换成Point，接受类型"""
    if isinstance(s, Size):
        return Ok(s)
    if isinstance(s, Point):
        return Ok(Size(s.x, s.y))
    if (isinstance(s, list) or isinstance(s, tuple)) and len(s) == 2:
        return Ok(Size(s[0], s[1]))
    return Err('[ERR] type %s cannot convert to Size' % type(s))
