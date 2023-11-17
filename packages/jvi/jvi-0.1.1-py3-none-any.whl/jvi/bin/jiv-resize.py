#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import cv2
from jiv.geo.rectangle import Rect
from jiv.geo.size2d import size_parse
from jiv.image.image_nda import ImageNda

epilog = '''
Examples:

    jiv-resize src.png dst.png -c 256x256
    
'''


def main():
    parser = argparse.ArgumentParser(description='图片缩放工具', epilog=epilog)
    parser.add_argument('src', type=Path, help='来源图片')
    parser.add_argument('dst', type=Path, help='目的图片')
    parser.add_argument('-c', '--crop_size', type=str, help='目标图片裁切尺寸(中心裁切)')
    parser.add_argument('-s', '--scale', type=float, default=1, help='图片缩放比例')
    parser.add_argument('-i', '--interpolation', type=int, default=1, help='差之方法: 1-INTER_LINEAR, 2-INTER_CUBIC')

    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    assert opt.interpolation in (1, 2)

    src = ImageNda.load(str(opt.src), cv2.IMREAD_UNCHANGED)  # BGR
    assert src is not None
    dst = cv2.resize(src, (0, 0), None, fx=opt.scale, fy=opt.scale, interpolation=opt.interpolation)

    dst_size = dst.size()

    if opt.crop_size:
        crop_size = size_parse(opt.crop_size)

        if dst_size.contains(crop_size):
            r = Rect.from_cs(dst_size.center(), crop_size)
            crop = dst.roi(r)
        else:
            crop = ImageNda(crop_size, src.shape[2])
            center = crop_size.center()
            r = Rect.from_cs(center, dst_size).round()
            roi = crop.roi(r)
            cv2.copyTo(dst, None, roi)
        dst = crop
        if opt.verbose:
            cv2.imshow('crop', crop)

    if opt.verbose:
        cv2.imshow('src', src)
        cv2.imshow('dst', dst)
        cv2.waitKey(0)

    cv2.imwrite(str(opt.dst), dst)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
