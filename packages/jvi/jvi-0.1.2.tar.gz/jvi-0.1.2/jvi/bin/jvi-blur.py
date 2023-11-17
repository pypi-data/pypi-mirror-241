#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import cv2  # type: ignore


def main():
    parser = argparse.ArgumentParser(description='图片模糊工具')
    parser.add_argument('src_dir', type=Path, help='来源图片目录')
    parser.add_argument('dst_dir', type=Path, help='目的图片目录')
    parser.add_argument('level', type=int, help='视频模糊级别')
    parser.add_argument('-p', '--pattern', type=str, default='*.jpg', help='图片文件模式(*.jpg)')
    parser.add_argument('-t', '--tail', type=str, default='_b', help='图片后缀')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    files = opt.src_dir.rglob(opt.pattern)
    print('源图片目录：%s' % opt.src_dir)

    n = 2 * opt.level + 1
    ksize = (n, n)

    for i, f in enumerate(files):
        src = ImageNda.load(str(f))  # BGR
        if src is None:
            print(i, f.name, '\tERROR')
            continue
        if opt.verbose:
            print(i, f.name, '\tOK')
        dst = cv2.blur(src, ksize)

        name = f.stem + opt.tail + str(opt.level) + f.suffix
        file = opt.dst_dir / name
        print(file)
        cv2.imwrite(str(file), dst)
        # cv2.imshow('src', src)
        # cv2.imshow('dst', dst)
        # cv2.waitKey(0)

    # cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
