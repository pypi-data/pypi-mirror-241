import itertools

import cv2  # type: ignore
import numpy as np
from jiv.drawing.color import Color, Colors
from jiv.geo.point2d import array_is_normalized, array_absolutize, Points, Point
from jiv.geo.rectangle import Rect
from jiv.geo.size2d import Size
from jiv.image.image_nda import ImageNda
from typing import Optional


def put_text(canvas: ImageNda, text: str, left_bottom: Point, color: Color, thickness: int = 1,
             scale: float = 0.7) -> None:
    """显示文字"""
    cv2.putText(canvas.data(), text, left_bottom.to_tuple_int(), 0, scale, color.bgr(), thickness, lineType=cv2.LINE_AA)


def rectangle(canvas: ImageNda, rect: Rect, color: Color, thickness: int = 1) -> None:
    """绘制矩形"""
    if rect.is_normalized():
        rect = rect.absolutize(canvas.size())

    p1, p2 = rect.ltrb_tuple_int()
    cv2.rectangle(canvas.data(), p1, p2, color.bgr(), thickness)


def points_to_contour(points: Points):
    """点集转轮廓"""
    pts = []
    for p in points:
        pts.append([p.x, p.y])
    contours = np.array(pts, np.int32)
    return contours.reshape((-1, 1, 2))


def in_polygon(p: Point, polygon: Points) -> int:
    """判定点在多边形内"""

    contour = points_to_contour(polygon)
    return cv2.pointPolygonTest(contour, (p.x, p.y), False)


def line(canvas: ImageNda, p1: Point, p2: Point, color: Color, thickness: int = 1) -> None:
    """绘制直线"""
    canvas_size = canvas.size()
    if p1.is_normalized():
        p1 = p1.absolutize(canvas_size)
    if p2.is_normalized():
        p2 = p2.absolutize(canvas_size)

    cv2.line(canvas.data(), p1.to_tuple_int(), p2.to_tuple_int(), color.bgr(), thickness)


def polylines(canvas: ImageNda, points: Points, color: Color, thickness: int = 1) -> None:
    """绘制多边形"""

    if array_is_normalized(points):
        points = array_absolutize(points, canvas.size())

    contours = points_to_contour(points)
    cv2.polylines(canvas.data(), [contours], True, color.bgr(), thickness)


# [opencv-python3 | cv2.findContours()检测图像中物体轮廓](https://blog.csdn.net/Just_do_myself/article/details/124215020)


def cross(canvas: ImageNda, center: Point, radius: int, color: Color, thickness: int = 1) -> None:
    """绘制十字"""

    if center.is_normalized():
        center = center.absolutize(canvas.size())

    p1 = center + Point(-radius, 0)
    p2 = center + Point(radius, 0)
    cv2.line(canvas.data(), p1.to_tuple_int(), p2.to_tuple_int(), color.bgr(), thickness)

    p1 = center + Point(0, -radius)
    p2 = center + Point(0, radius)
    cv2.line(canvas.data(), p1.to_tuple_int(), p2.to_tuple_int(), color.bgr(), thickness)


def grid(canvas: ImageNda, tile_size: Size, color: Optional[Color] = None, thickness: int = 1,
         colors: Colors = []) -> None:
    """绘制网格"""

    canvas_size = canvas.size()
    if tile_size.is_normalized():
        tile_size = tile_size.absolutize(canvas_size)

    colors1 = itertools.cycle([color] if color else colors)
    for x in range(0, int(canvas_size.width), int(tile_size.width)):
        color1 = next(colors1)
        p1 = Point(x, 0)
        p2 = Point(x, canvas_size.height)
        line(canvas, p1, p2, color1, thickness)

    colors1 = itertools.cycle([color] if color else colors)
    for y in range(0, int(canvas_size.height), int(tile_size.height)):
        color1 = next(colors1)
        p1 = Point(0, y)
        p2 = Point(canvas_size.width, y)
        line(canvas, p1, p2, color1, thickness)
