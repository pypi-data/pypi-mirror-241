from typing import Final, Optional

import cv2
import numpy as np
from PIL import Image as ImagePIL
from jcx.sys import fs
from jvi.image.image import *
from loguru import logger
from rustshed import Result, Err, Ok

Self: TypeAlias = 'ImageNda'  # type: ignore

type_map: Final = {
    DType.U8: np.uint8,
    DType.U16: np.uint16,
    DType.U32: np.uint32,
    DType.U64: np.uint64,
    DType.I8: np.int8,
    DType.I16: np.int16,
    DType.I32: np.int32,
    DType.I64: np.int64,
    DType.F16: np.float16,
    DType.F32: np.float32,
    DType.F64: np.float64,
}

name_map: Final = {
    'uint8': DType.U8,
    'uint16': DType.U16,
    'uint32': DType.U32,
    'uint64': DType.U64,
    'int8': DType.I8,
    'int16': DType.I16,
    'int32': DType.I32,
    'int64': DType.I64,
    'float16': DType.F16,
    'float32': DType.F32,
    'float64': DType.F64,
}


class ImageNda(Image):
    """图片: 由numpy.ndarray实现"""

    @classmethod
    def new_as(cls, image: Image, size: Optional[Size] = None, channel: int = 0, dtype=None,
               color: Optional[ImageColor] = None) -> 'ImageNda':
        """创建图片，缺省参数与指定图片相同"""
        s = size or image.size()
        c = channel or image.channel_num()
        t = dtype or image.dtype()
        return cls(shape=(s.height, s.width, c), dtype=t, color=color)

    @classmethod
    def try_load(cls, path: StrPath, flag: int = -1) -> Result[Self, str]:
        """尝试加载图片"""
        data = cv2.imread(str(path), flag)
        if data is None:
            return Err(f"Load image fail: {path}")
        return Ok(cls(data=data))

    @classmethod
    def load(cls, path: StrPath, flag: int = -1) -> 'ImageNda':
        """加载图片, 失败抛出异常"""
        return cls.try_load(path, flag).unwrap()

    def save(self, path: StrPath) -> bool:
        """保存图片"""
        fs.make_parents(path)
        r = cv2.imwrite(str(path), self._data)
        assert isinstance(r, bool)
        return r

    def __init__(self, size: Size = Size(),
                 channel: int = 3,
                 shape: Optional[tuple] = None,
                 dtype: DType = DType.U8,
                 data: Optional[np.ndarray] = None,
                 color: Optional[ImageColor] = None):
        """构造图像"""
        if data is not None:
            assert isinstance(data, np.ndarray)
            self._data = data
        else:
            assert bool(size) ^ (shape is not None)
            if size:
                if channel == 1:
                    shape = size.to_shape()
                else:
                    shape = size.to_shape3d_i(channel)
            dtype1 = type_map.get(dtype)
            assert dtype1 is not None
            assert shape
            self._data = np.zeros(shape, dtype=dtype1)
        # assert len(self._data.shape) == 3 # 单通道图片为2?
        assert self.dtype() is not None
        if color is not None:
            self.set_to(color)

    def __bool__(self) -> bool:
        """判断图像是否有效"""
        return self._data is not None

    def size(self) -> Size:
        return Size(self._data.shape[1], self._data.shape[0])

    def channel_num(self) -> int:
        return self._data.shape[2] if len(self.shape()) > 2 else 1

    def channel_at(self, idx: int) -> 'ImageNda':
        return ImageNda(data=self._data[..., idx])

    def channels(self) -> list['ImageNda']:
        """获取图像所有通道"""
        return [self.channel_at(i) for i in range(self.channel_num())]

    def shape(self) -> Shape3D:
        return self._data.shape

    def dtype(self) -> DType:
        return name_map.get(self._data.dtype.name)

    def clone(self) -> 'ImageNda':
        return ImageNda(data=self._data.copy())

    def copy_to(self, other: Self) -> None:
        cv2.copyTo(self._data, None, other.data())

    def convert_to(self, other: Self) -> None:
        raise NotImplementedError()

    def set_to(self, color: ImageColor) -> None:
        if isinstance(color, Color):
            color = color.bgr()

        if isinstance(color, Real):
            assert self.channel_num() == 1
        else:
            assert len(color) == self.channel_num()
        self._data[:] = color

    def roi(self, rect: Rect) -> 'ImageNda':
        rect = rect.clone()
        if rect.is_normalized():
            rect = rect.absolutize(self.size())
        rect.round_me()
        a, b = rect.ltrb()
        return ImageNda(data=self._data[a.y:b.y, a.x:b.x])

    def data(self) -> np.ndarray:
        return self._data

    def __eq__(self, other: Self) -> bool:
        return (self.data() == other.data()).all()

    def to_tiles(self, cols: int, rows: int) -> list['ImageNda']:
        """图像切成块, 各个块与原图像共享数据"""
        rects = Rect.from_size(self.size()).to_tiles(cols, rows)
        return [self.roi(r) for r in rects]


ImageNdas: TypeAlias = list[ImageNda]
"""图像数组"""


def new_gray(size: Size, color: Real = 0, dtype: DType = DType.U8) -> ImageNda:
    """产生一个灰度图"""
    return ImageNda(size, 1, dtype=dtype, color=color)


def is_image(f: StrPath) -> bool:
    """判断文件是否是图片"""
    r = ImageNda.try_load(f)
    match r:
        case Err(s):
            return False
    return True


def correct_image(f: StrPath) -> bool:
    """更正图片文件错误(CRC), FIXME: 好像没用"""
    r = ImageNda.try_load(f)
    match r:
        case Err(s):
            image = ImagePIL.open(f)
            image.save(f)
            logger.info(f"Correct image: {f}")
            return False
    return True
