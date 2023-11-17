from dataclasses import dataclass
from math import sqrt
from typing import Protocol, TypeVar, runtime_checkable

from jcx.m.number import Real

"""
泛型实验

Protocol问题:
- 不支持isinstance, 无法支持函数重载
- 提供的函数体无意义, 不能作为缺省实现
"""

T = TypeVar('T', int, float)


@runtime_checkable
class ISize2D(Protocol):
    """二维尺寸类型协议"""
    width: T
    height: T


def size_equal(s1: ISize2D, s2: ISize2D) -> bool:
    return s1.width == s2.width and s1.height == s2.height


def size_area(s: ISize2D) -> Real:
    """获取有二维尺寸对象面积"""
    return s.width * s.height


@runtime_checkable
class IHasSize2D(Protocol):
    """二维尺寸类型协议"""

    def size(self) -> ISize2D:
        pass


def area(s: ISize2D | IHasSize2D) -> Real:
    """获取有二维尺寸对象面积"""
    if isinstance(s, ISize2D):
        return size_area(s)
    elif isinstance(s, IHasSize2D):
        return size_area(s.size())
    raise 'Invalid type'


def same_size(s1: IHasSize2D, s2: IHasSize2D) -> bool:
    """对象二维尺寸相等"""
    return size_equal(s1.size(), s2.size())


class IArea(Protocol):
    """面积类型协议"""

    def area(self) -> Real:
        pass


def dist_tuple(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """计算2D距离"""
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == '__main__':
    @dataclass
    class P1:
        x: int
        y: int


    p = P1(0, 1)
