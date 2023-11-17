from abc import abstractmethod
from enum import IntEnum
from typing import TypeAlias, TypeVar, Protocol

from jcx.m.number import Real
from jcx.sys.fs import StrPath
from jiv.drawing.color import Color
from jiv.geo.rectangle import Rect
from jiv.geo.size2d import Size

Self = TypeVar('Self', bound='Image')

Shape2D: TypeAlias = tuple[int, int]
"""三维形状"""
Shape3D: TypeAlias = tuple[int, int, int]
"""三维形状"""

ImageShape: TypeAlias = tuple


# ImageShape: TypeAlias = Shape3D | Shape2D


class DType(IntEnum):
    """数据类型"""
    U8 = 1
    U16 = 2
    U32 = 4
    U64 = 8
    I8 = 11
    I16 = 12
    I32 = 14
    I64 = 18
    F8 = 21
    F16 = 22
    F32 = 24
    F64 = 28


ImageColor: TypeAlias = Real | tuple | Color
"""Image可用颜色类型"""


class Image(Protocol):
    """图像抽象类"""

    def __str__(self) -> str:
        """图像描述信息"""
        s = self.size()
        return '%s(%dx%dx%d,%s)' % (self.__class__.__name__, s.width, s.height, self.channel_num(), self.dtype())

    @abstractmethod
    def __bool__(self) -> bool:
        """判断图像是否有效"""
        pass

    @abstractmethod
    def size(self) -> Size:
        """获取图像尺寸"""
        pass

    def same_size(self, other: Self) -> bool:
        """判定尺寸相等"""
        return self.size() == other.size()

    @abstractmethod
    def channel_num(self) -> int:
        """获取图像通道数"""
        pass

    def same_channel_num(self, other: Self) -> bool:
        """判定通道数相等"""
        return self.channel_num() == other.channel_num()

    @abstractmethod
    def channel_at(self: Self, idx: int) -> Self:
        """获取图像指定通道"""
        pass

    @abstractmethod
    def channels(self) -> list[Self]:
        """获取图像所有通道"""
        pass

    @abstractmethod
    def shape(self) -> Shape3D:
        """获取图像形状: (高, 宽, 通道)"""
        s = self.size()
        return s.to_shape3d_i(self.channel_num())

    def same_shape(self, other: Self) -> bool:
        """判定形状相等"""
        return self.shape() == other.shape()

    @abstractmethod
    def dtype(self) -> DType:
        """获取数据类型"""
        pass

    def same_dtype(self, other: Self) -> bool:
        """判定数据类型相等"""
        return self.dtype() == other.dtype()

    def same_shape_type(self, other: Self) -> bool:
        """判定形状&类型相等"""
        return self.same_shape(other) and self.same_dtype(other)

    @abstractmethod
    def clone(self: Self) -> Self:
        """克隆图片对象"""
        pass

    @abstractmethod
    def copy_to(self, other: Self) -> None:
        """复制数据到目标图像"""
        pass

    @abstractmethod
    def convert_to(self, other: Self) -> None:
        """复制转换数据类型到目标图像"""
        pass

    @abstractmethod
    def set_to(self, color: ImageColor) -> None:
        """图像设置为指定颜色"""
        pass

    @abstractmethod
    def roi(self: Self, r: Rect) -> Self:
        """获取ndarray区域"""
        pass

    @abstractmethod
    def save(self, path: StrPath) -> bool:
        """保存图片"""
        pass
