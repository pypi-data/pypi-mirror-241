#!/opt/ias/env/bin/python

import argparse
import glob
import os
import sys

import cv2
import matplotlib
import matplotlib.pyplot as plt
from interval import Interval

from jcx.ui.key import Key


def main():
    parser = argparse.ArgumentParser(description='图像工具箱')
    parser.add_argument('source', type=str, help='数据源，文件/目录')
    parser.add_argument('--img-size', type=int, default=224, help='输入图像尺寸')
    parser.add_argument('-r', '--aspect-ratio', nargs=2, type=float, default=[0.0, 100.0], help='纵横比范围')
    parser.add_argument('-s', '--show-hist', action='store_true', help='显示直方图')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    if os.path.isdir(opt.source):
        s = os.path.join(opt.source, "**/*.jpg")
        files = sorted(glob.glob(s, recursive=True))
    elif os.path.isfile(opt.source):
        files = [opt.source]
    else:
        print("数据源不存在")
        sys.exit(0)

    radio_range = Interval(opt.aspect_ratio[0], opt.aspect_ratio[1])

    print(radio_range)

    ratio_list = []

    for i, f in enumerate(files):
        img = ImageNda.load(f)  # BGR
        if img is None:
            # print(i, f + '\tERROR')
            continue

        ratio = img.shape[0] / img.shape[1]
        if ratio not in radio_range:
            continue

        ratio_list.append(ratio)
        print(f)

        if opt.verbose:
            cv2.imshow(opt.source, img)
            if cv2.waitKey(0) == Key.ESC.value:
                break
    if opt.show_hist:
        matplotlib.use('TkAgg')
        plt.hist(ratio_list, bins=100, facecolor="blue", edgecolor="black")
        plt.xlabel("aspect ratio")
        plt.ylabel("amount")
        plt.title("aspect ratio hist")
        plt.show()


if __name__ == '__main__':
    main()
