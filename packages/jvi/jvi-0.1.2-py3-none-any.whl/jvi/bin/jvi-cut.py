#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import cv2  # type: ignore
from jcx.sys.fs import files_in, stem_append
from jvi.geo.rectangle import Rect
from jvi.geo.size2d import Size
from jvi.image.image_nda import ImageNda

epilog = '''
Examples:

    jvi-cut src.png dst.png -a 1:1
    
'''


def cut_square(src_dir: Path, dst_dir: Path, ext: str):
    files = files_in(src_dir, ext)

    for src_file in files:
        src_im: ImageNda = ImageNda.load(src_file)
        src_size = src_im.size()
        side = min(src_size.width, src_size.height)
        dst_size = Size(side, side)
        tiles = Rect.from_size(src_size).to_tiles(size=dst_size)
        for i, r in enumerate(tiles):
            dst_im: ImageNda = src_im.roi(r)
            dst_file = dst_dir / src_file.name
            dst_file = stem_append(dst_file, f'_{i}')
            print(f'save to: {dst_file}')
            dst_im.save(dst_file)


def main() -> None:
    parser = argparse.ArgumentParser(description='图片切分工具', epilog=epilog)
    parser.add_argument('src_dir', type=Path, help='来源图片')
    parser.add_argument('dst_dir', type=Path, help='目的图片')
    parser.add_argument('-e', '--exp', type=str, default='.jpg', help='图片文件扩展名')
    parser.add_argument('-a', '--aspect', type=float, default=1, help='纵横比')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    cut_square(opt.src_dir, opt.dst_dir, opt.exp)


if __name__ == '__main__':
    main()
