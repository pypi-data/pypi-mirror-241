from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np
from arrow import Arrow
from jvi.geo.size2d import Size
from jvi.image.image_nda import ImageNda


@dataclass
class ImageFactory:
    """抓图配置"""

    origin: ImageNda
    """原始图片"""
    path: Optional[Path] = None
    """图片路径"""
    gray: Optional[ImageNda] = None
    """对应的灰度图"""

    def size(self) -> Size:
        """获取图像原始尺寸"""
        return self.origin.size()

    def rgb_data(self) -> np.ndarray:
        """获取图像RGB顺序的数据"""
        return self.origin.data()[:, :, ::-1]  # BGR => RGB


@dataclass
class ImageFactorySet:
    """图片工厂集合"""

    factories: list[Optional[ImageFactory]]
    """图片工厂数组"""
    time: Arrow

    def file_at(self, i: int) -> Path:
        """指定索引的文件"""
        fac = self.factories[i]
        assert fac
        f = fac.path
        assert f
        return f

    def image_at(self, i: int) -> ImageNda:
        """指定索引的图片"""
        fac = self.factories[i]
        assert fac
        im = fac.origin
        assert im
        return im
