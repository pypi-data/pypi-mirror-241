# from jiv.geo.point2d import Point
# from jiv.geo.rectangle import Rect
# from jiv.geo.size2d import Size


def is_normalized(v: float) -> bool:
    """判断坐标是否被归一化"""
    return 0 <= v <= 1


def to_zero(v: float) -> float:
    """接近零的数据转为零"""
    return v if abs(v) > 0.00001 else 0
