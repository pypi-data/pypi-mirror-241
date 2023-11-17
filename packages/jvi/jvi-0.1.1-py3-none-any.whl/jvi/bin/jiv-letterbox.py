#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

from jcx.sys.fs import files_in
from jiv.drawing.color import YOLO_GRAY
from jiv.geo.rectangle import Rect
from jiv.geo.size2d import size_parse
from jiv.image.image_nda import ImageNda
from jiv.image.trace import trace_image

epilog = '''
Examples:

    jiv-letterbox src_dir dst_dir -S 256x256
    
'''


def main() -> None:
    parser = argparse.ArgumentParser(description='图片嵌入工具', epilog=epilog)
    parser.add_argument('src_dir', type=Path, help='来源图片目录')
    parser.add_argument('dst_dir', type=Path, help='目的图片目录')
    parser.add_argument('-S', '--dst_size', type=str, default='HD', help='目标图片裁切尺寸(中心裁切)')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    dst_size = size_parse(opt.dst_size)
    assert dst_size

    files = files_in(opt.src_dir, '.jpg')
    assert len(files)
    for src_file in files:
        src = ImageNda.load(src_file)
        assert src is not None
        dst = ImageNda(dst_size, color=YOLO_GRAY)
        center = dst_size.center()
        r = Rect.from_cs(center, src.size()).round()
        src.copy_to(dst.roi(r))
        dst_file = Path(opt.dst_dir, src_file.name)
        trace_image(dst, dst_file.name)
        dst.save(dst_file)


if __name__ == '__main__':
    main()
