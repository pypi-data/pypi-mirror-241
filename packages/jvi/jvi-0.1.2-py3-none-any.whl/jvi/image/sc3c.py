from dataclasses import dataclass
from typing import Optional

import numpy as np
from jvi.geo.rectangle import Rect
from jvi.geo.size2d import Size
from jvi.image.image_nda import ImageNda, ImageNdas
from jvi.image.proc import to_gray, merge, split
from jvi.image.tile_set import TileSet


# args = /home/jiang/ws/scene/cnooc/sources/31010102100700101 -v

@dataclass
class ImageItem:
    """图像条目"""
    image: ImageNda
    gray: ImageNda

    def channel_roi(self, channel: int, rect: Rect) -> ImageNda:
        """获取指定通道的指定区域"""
        return self.image.channel_at(channel).roi(rect)

    def roi(self, rect: Rect) -> ImageNda:
        """获取指定区域"""
        return self.image.roi(rect)


CHANNEL_NUM = 3


class Sc3cImageFactory:
    """同色三通道图像工厂"""

    def __init__(self):
        self._size = Size()
        self._items: list[ImageItem] = []
        self._tile3: Optional[TileSet] = None

    def __len__(self) -> int:
        """获取图片数量"""
        return len(self._items)

    def empty(self):
        return len(self) == 0

    def ready(self):
        return len(self) >= CHANNEL_NUM

    def size(self) -> Size:
        return self._size

    def images(self) -> ImageNdas:
        """获取全部图片"""
        return [item.image for item in self._items]

    def push(self, image: ImageNda):
        """压入图片, 图片超过3张, 第一张丢弃"""
        image = image.clone()
        item = ImageItem(image, to_gray(image))

        size = image.size()
        if size != self._size:
            self._size = size
            self._items = []
        if self.ready():
            self._items.pop(0)
        self._items.append(item)

    def sc3c_images(self, rect: Rect = Rect.zero()) -> ImageNdas:
        """获取同色三通道图像:B3,G3,R3,Gray3"""
        rect = rect if rect else Rect.from_size(self.size())
        assert len(self._items) == CHANNEL_NUM
        images = []
        for i in range(CHANNEL_NUM):
            channels = [item.channel_roi(i, rect) for item in self._items]
            images.append(merge(channels))
        channels = [item.gray.roi(rect) for item in self._items]
        images.append(merge(channels))
        return images

    def t3_image(self, rect: Rect = Rect.zero()) -> ImageNda:
        """获取3个源图像上指定区域, 合并成1x3(块)图像"""
        rect = rect if rect else Rect.from_size(self.size())
        assert len(self._items) == CHANNEL_NUM

        if self._tile3 is None or self._tile3.tile_size() != rect.size():
            self._tile3 = TileSet(tile_size=rect.size(), cols=3, rows=1)

        for i, tile in enumerate(self._tile3.tiles()):
            self._items[i].roi(rect).copy_to(tile)
        return self._tile3.image()


def a_test():
    f = '/home/jiang/ws/scene/cnooc/samples_i3/0/31010102100700101_003_2022-11-15_11-05-51.943.jpg'
    im = ImageNda.load(f)
    cs = split(im)
    print(im.shape(), cs[0].shape())
    print(im.data()[:, :, 0:1].shape)
    print(im.data()[..., 0].shape)
    print(im.data()[..., 1].shape)


def a_test1():
    a3d = np.array([
        [[10, 20, 30], [10, 20, 30]],
        [[10, 20, 30], [10, 20, 30]]], dtype=np.uint8
    )
    print(a3d)
    print('shape:', a3d.shape)
    print('p00:', a3d[0, 0])
    print('c0:', a3d[..., 1])

    fac = Sc3cImageFactory()
    fac.push(a3d)
    fac.push(a3d)
    fac.push(a3d)
    ims = fac.sc3c_images(Rect(0, 0, 2, 1))

    for i, im in enumerate(ims):
        print('sc3cim%d' % i, im.shape, ':\n', im)
    ts = fac.t3_image(Rect(0, 0, 2, 2))
    print('tile1x3', ts.shape, ':\n', ts)

    b = 10
    g = 20
    r = 30
    gray = 0.30 * r + 0.59 * g + 0.11 * b
    print('gray:', gray)


if __name__ == '__main__':
    # a_test1()
    a_test()
    # a_mark()
    # mask_test()
