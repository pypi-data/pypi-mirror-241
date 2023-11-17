#!/opt/ias/env/bin/python
import argparse

import sh


# 参考: http://amoffat.github.io/sh/

def main():
    parser = argparse.ArgumentParser('ffmpeg文件分割工具')  # TODO
    parser.add_argument('src_dir', type=Path, help='文件来源目录')
    parser.add_argument('-e', '--ext', type=str, default='jpg', help='文件扩展名')
    parser.add_argument('-m', '--mate_ext', type=str, default='lbl', help='文件伙伴文件扩展名')
    parser.add_argument('-i', '--invert_match', action='store_true', help='选中不匹配的文件')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    mates = files_in(opt.src_dir, opt.mate_ext)
    names = [f.stem for f in mates]


if __name__ == '__main__':
    main()
