#!/opt/ias/env/bin/python

import argparse
from pathlib import Path
from typing import Optional

from jcx.sys.fs import files_in
from jcx.text.txt_json import save_json
from jiv.geo.rectangle import Rect
from jiv.image.tile import PanoramaInfo, TileInfo
from jiv.image.util import ndarray_size
from jiv.match.match_template import find_template_tile

'''
从原图中查找模板（覆盖匹配），图片位置输出到到全景图数据中(JSON格式)。
'''


def main():
    parser = argparse.ArgumentParser(description='瓦片图片匹配工具')
    parser.add_argument('src', type=Path, help='待匹配图片文件')
    parser.add_argument('template', type=Path, help='模板图片文件/目录')
    parser.add_argument('-p', '--panorama', type=Optional[Path], default=None, help='匹配全景文件')
    parser.add_argument('-e', '--ext', type=str, default='.png', help='图片文件扩展名')
    parser.add_argument('-a', '--align', type=int, default=8, help='坐标对齐')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    flag = None  # cv2.IMREAD_UNCHANGED
    img_src = ImageNda.load(str(opt.src), flag)
    assert img_src is not None

    panorama = opt.panorama or opt.src.with_suffix('.json')

    print('匹配信息输出到：', opt.panorama)

    files = files_in(opt.template, opt.ext)
    pano_info = PanoramaInfo(ndarray_size(img_src), str(opt.src))

    for i, f in enumerate(files):
        print('开始搜索:', f.name)
        img_templ = ImageNda.load(str(f), flag)
        assert img_templ is not None
        size = ndarray_size(img_templ)

        pos, v = find_template_tile(img_src, img_templ)
        pos1 = pos.align_round(opt.align)
        msg = '' if pos == pos1 else '\talign'
        print(i, pos, v, msg)

        rect = Rect.from_ps(pos1, size)
        pano_info.tiles.append(TileInfo(str(f), rect))

        save_json(pano_info, panorama)


if __name__ == '__main__':
    main()
