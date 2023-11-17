#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

from jvi.image.image_nda import ImageNda
from jvi.image.stat import value_map
from jvi.image.trace import trace_image

epilog = '''
Examples:

    jvi-imp src.png dst.png
    
'''


def main():
    parser = argparse.ArgumentParser(description='图片处理工具', epilog=epilog)
    parser.add_argument('src', type=Path, help='来源图片')
    parser.add_argument('dst', type=Path, help='目的图片')
    parser.add_argument('-s', '--size', type=str, help='画布尺寸')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    src_img = ImageNda.load(opt.src)

    print('source image shape:', src_img.shape())

    trace_image(src_img)
    m = value_map(src_img)
    print(f'{src_img} hist:')
    for v, p in m.items():
        print(f'\t{v}\t{int(p * 100)}%')


if __name__ == '__main__':
    main()
