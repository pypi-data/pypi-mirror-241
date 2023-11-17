from typing import Optional

from jiv.geo.rectangle import Rect
from jiv.geo.size2d import Size, SIZE_HD
from jiv.image.image_nda import ImageNda, ImageNdas
from jiv.image.trace import trace_image


class TileSet:
    """图片分割成的瓦片集合"""

    def __init__(self, tile_size: Size = Size(), rows: int = 0, cols: int = 0, size: Size = Size(),
                 image: Optional[ImageNda] = None):
        """构造瓦片集合"""
        if tile_size and rows * cols:
            size = Size(tile_size.width * cols, tile_size.height * rows)
        size = size or image.size()
        tile_size = tile_size or Size(size.width / cols, size.height / rows)
        assert tile_size and size

        self._image: ImageNda = image or ImageNda(size)
        rs = Rect.from_size(size).to_tiles(size=tile_size)
        self._tiles: ImageNdas = [self._image.roi(r) for r in rs]

    def __len__(self) -> int:
        """获取瓦片数量"""
        return len(self._tiles)

    def size(self) -> Size:
        """获取图片尺寸"""
        return self._image.size()

    def tile_size(self) -> Size:
        """获取瓦片尺寸"""
        return self._tiles[0].size()

    def image(self) -> ImageNda:
        """获取图片"""
        return self._image

    def tiles(self) -> ImageNdas:
        """获取全部瓦片"""
        return self._tiles


def show_tile():
    from jiv.drawing.color import COLORS7

    size = Size(30, 20)
    tile_size = Size(10, 10)

    ts = TileSet(tile_size=tile_size, size=size)
    assert ts.size() == size
    assert ts.tile_size() == tile_size

    ts = TileSet(rows=2, cols=3, size=size)
    assert ts.size() == size
    assert ts.tile_size() == tile_size

    for i, im in enumerate(ts.tiles()):
        im.set_to(COLORS7[i])

    trace_image(ts.image(), box_size=SIZE_HD)


if __name__ == '__main__':
    show_tile()
