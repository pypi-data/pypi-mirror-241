#!/opt/ias/env/bin/python

import argparse
from pathlib import Path
from typing import Optional

from jcx.text.txt_json import save_json
from jvi.image.tile import panorama_from_dir


def main():
    parser = argparse.ArgumentParser(description='目录图片瓦片平铺工具')
    parser.add_argument('src_dir', type=Path, help='来源图片目录')
    parser.add_argument('-p', '--panorama', type=Optional[Path], default=None, help='匹配全景文件')
    parser.add_argument('-e', '--ext', type=str, default='.png', help='来源图片文件扩展名')
    parser.add_argument('-c', '--cols', required=True, type=int, help='瓦片列数')
    parser.add_argument('-r', '--rows', type=int, help='瓦片行数')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    panorama = opt.panorama or opt.src_dir.with_suffix('.json')
    print('匹配信息输出到：', panorama)

    info = panorama_from_dir(opt.src_dir, cols=opt.cols, rows=opt.rows, ext=opt.ext, verbose=opt.verbose)
    save_json(info, panorama)


if __name__ == '__main__':
    main()
