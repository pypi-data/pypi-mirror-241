#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import cv2
import numpy as np

from jcx.ui.key import Key
from jml.iqa.a import estimate_clearness


def trans(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    print(gray.dtype)
    edge = cv2.Sobel(gray, -1, 1, 1, ksize=3)
    print('edge:', edge.shape, edge.dtype)
    hist = cv2.calcHist([edge], [0], None, [256], [0, 256])
    # edge = cv2.Canny(gray, 100, 200)
    hist *= 255 / np.sum(hist)
    hist = hist.astype(np.uint8)
    hist = hist[:224]
    print('hist:', hist.shape, np.sum(hist))

    print('t:', np.transpose(hist))

    hist = np.repeat(hist, 224, axis=1)
    print('hist:', hist.shape, np.sum(hist))

    return hist


def main():
    parser = argparse.ArgumentParser(description='图片模糊度评估工具')
    parser.add_argument('src_dir', type=Path, help='来源图片目录')
    parser.add_argument('dst_dir', type=Path, help='目的图片目录')
    parser.add_argument('-p', '--pattern', type=str, default='*.jpg', help='图片文件模式(*.jpg)')
    parser.add_argument('-t', '--tail', type=str, default='_b', help='图片后缀')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    files = opt.src_dir.rglob(opt.pattern)
    print('源图片目录：%s' % opt.src_dir)

    colors = []

    for i, f in enumerate(files):
        src = ImageNda.load(str(f))  # BGR
        if src is None:
            print(i, f.name, '\tERROR')
            continue
        if opt.verbose:
            print(i, f.name, '\tOK')

        color = estimate_clearness(src, 0.9)
        colors.append(color)
        # print('#%d' % i, color)

        if opt.verbose and color == 0:
            cv2.imshow('src', src)
            if cv2.waitKey(0) == Key.ESC:
                break

    print('range: [%d, %d] mean: %d' % (min(colors), max(colors), np.mean(colors)))
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
