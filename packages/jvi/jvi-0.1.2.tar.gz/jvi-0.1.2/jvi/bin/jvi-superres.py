#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import cv2
from jcx.sys.fs import files_in, real_exe_path

'''
图片超分辨率工具

不适合整合为resize工具，因为分辨率受限。

'''


def resize_file(model, src: Path, dst: Path, scale: int, verbose: bool):
    img_src = ImageNda.load(str(src))
    if img_src is None:
        print("[ERROR] load image fail: " + str(src))
        return
    print('upsample source image ...')
    img_dst = model.upsample(img_src)
    print('imwrite image to:', dst)
    cv2.imwrite(str(dst), img_dst)

    if verbose:
        img_linear = cv2.resize(img_src, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
        img_bicubic = cv2.resize(img_src, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

        cv2.imshow('img_src', img_src)
        cv2.imshow('img_dst', img_dst)
        cv2.imshow('img_linear', img_linear)
        cv2.imshow('img_bicubic', img_bicubic)

        cv2.waitKey(0)


def main():
    parser = argparse.ArgumentParser(description='图片超分辨率工具')
    parser.add_argument('src', type=Path, help='来源图片文件/目录')
    parser.add_argument('dst', type=Path, help='目的图片文件/目录')
    parser.add_argument('-s', '--scale', type=int, default=2, help='图片放大倍数: 2,3,4')
    parser.add_argument('-e', '--ext', type=str, help='目录内待转换文件扩展名')
    parser.add_argument('-a', '--algorithm', type=str, default='edsr', help='放缩算法')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    model_dir = real_exe_path().parent.parent / 'model/superres'
    models = {2: 'EDSR_x2.pb', 3: 'EDSR_x3.pb', 4: 'EDSR_x4.pb'}

    if opt.scale not in models:
        print('[ERROR] 无效放大倍数')
        return -2

    model = cv2.dnn_superres.DnnSuperResImpl_create()
    model_file = model_dir / models[opt.scale]
    print('load model:', model_file)
    model.readModel(str(model_file))

    model.setModel(opt.algorithm, opt.scale)

    if opt.ext:
        files = files_in(opt.src, opt.ext)
        for src in files:
            dst = opt.dst / src.name
            resize_file(model, src, dst, opt.scale, opt.verbose)
    else:
        resize_file(model, opt.src, opt.dst, opt.scale, opt.verbose)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
