from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, TypeAlias

import cv2  # type: ignore
from jcx.sys.fs import files_in
from jvi.geo.point2d import Point
from jvi.geo.rectangle import Rect
from jvi.geo.size2d import Size
from jvi.image.image_nda import ImageNda


@dataclass
class TileInfo:
    """瓦片信息"""
    file: str
    """瓦片所在文件"""
    rect: Rect
    """瓦片所在位置"""


TileInfos: TypeAlias = list[TileInfo]


@dataclass
class PanoramaInfo:
    """全景图信息"""
    size: Size
    """全图尺寸"""
    background: Optional[str] = None
    """背景图"""
    tiles: list[TileInfo] = field(default_factory=list)
    """瓦片图列表"""

    def tile_size(self) -> Size:
        """获取瓦片尺寸"""
        return self.tiles[0].rect.size()

    def load_tiles(self, no_background: bool) -> ImageNda:
        """"加载图片集合"""

        assert self.background
        pano = ImageNda.load(self.background, cv2.IMREAD_UNCHANGED) if not no_background else None
        tile_size = None
        print('开始加载图片:')
        for i, tile in enumerate(self.tiles):
            print('  #%d %s' % (i, tile.file))
            img = ImageNda.load(tile.file, cv2.IMREAD_UNCHANGED)  # FIXME:
            assert img is not None

            if pano is None:
                pano = ImageNda.new_as(img, size=self.size)  # 目标图是黑空图
            assert pano is not None
            assert self.size == pano.size()

            size = img.size()
            if tile_size is None:
                tile_size = size
            assert size == tile_size
            assert size == tile.rect.size()

            roi = pano.roi(tile.rect)
            cv2.copyTo(img, None, roi)

        return pano


def divide_sparse(image: ImageNda, tile_infos: TileInfos, dst_dir: Path, rows: int, cols: int,
                  file_name_fmt: str = '%02d-%02d.png') -> PanoramaInfo:
    """把拼接好的图像分割稀疏块"""

    pano_size = image.size()
    pano_info = PanoramaInfo(pano_size, None)

    tile_rects = Rect.from_size(pano_size).to_tiles(rows=rows, cols=cols)
    print('开始切分稀疏瓦片图：')
    for i, rect in enumerate(tile_rects):
        ok = False
        for t in tile_infos:
            r = rect.intersect(t.rect)
            if r.size().positive():
                ok = True
                break
        if ok:
            x = i % cols
            y = i // rows
            file = dst_dir / (file_name_fmt % (x, y))
            print('  #%d %s' % (i, file))
            roi = image.roi(rect)
            roi.save(file)
            pano_info.tiles.append(TileInfo(str(file), rect))

    return pano_info


def panorama_from_dir(src_dir: Path, cols: int, rows: int = 0, ext: str = '.png', verbose=False) -> PanoramaInfo:
    """从目录文件建立全景信息"""
    assert cols > 0

    files = files_in(src_dir, ext)
    assert len(files) > 0, '[ERROR] 目录中没有图片'

    rows = rows or (len(files) + cols - 1) // cols
    assert rows > 0

    pano_info = None
    tile_size = None

    for i, f in enumerate(files):
        img = ImageNda.load(str(f), cv2.IMREAD_UNCHANGED)
        assert img is not None, '[ERROR] 加载文件失败:'

        size = img.size()
        if not pano_info:
            tile_size = size
            pano_size = tile_size * Size(cols, rows)
            pano_info = PanoramaInfo(pano_size, None)
        assert size == tile_size

        x = i % cols
        y = i // rows
        pos = Point(x * size.width, y * size.height)
        rect = Rect.from_ps(pos, size)
        pano_info.tiles.append(TileInfo(str(f), rect))
        if verbose:
            print(i, pos)
    return pano_info
