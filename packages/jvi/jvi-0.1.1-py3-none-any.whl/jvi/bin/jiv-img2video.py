#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import cv2
from jiv.geo.size2d import size_parse


def main():
    parser = argparse.ArgumentParser(description='图片转视频工具')
    parser.add_argument('src_dir', metavar='SRC_DIR', type=Path, help='来源图片所在目录')
    parser.add_argument('dst_file', metavar='DST_FILE', type=Path, help='目的视频文件')
    parser.add_argument('-p', '--pattern', type=str, default='*.jpg', help='图片文件模式(*.jpg)')
    parser.add_argument('-s', '--size', type=str, default='HD', help='输出视频尺寸(HD)')
    parser.add_argument('-f', '--fps', type=float, default=5, help='视频帧率(5)')
    parser.add_argument('-r', '--repeat', type=int, default=1, help='视频帧的重复次数(1)')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    size = size_parse(opt.size)

    fourcc_tab = {'.mp4': 'mp4v', '.mjpg': 'mjpg', '.webp': 'webp'}  # require libwebp-dev
    # TODO: avc1/MJPG报错，https://stackoverflow.com/questions/52932157/ \
    #  opencv-ffmpeg-tag-0x34363268-h264-is-not-supported-with-codec/56723380

    fourcc = fourcc_tab.get(opt.dst_file.suffix)
    if not fourcc:
        print('[ERROR] 不支持的文件格式:', opt.dst_file.suffix)
        return -1
    fourcc = cv2.VideoWriter_fourcc(*fourcc)
    writer = cv2.VideoWriter(str(opt.dst_file), fourcc, opt.fps, size.to_tuple_int())

    files = opt.src_dir.rglob(opt.pattern)
    files = sorted(files)
    print('源图片目录：%s' % opt.src_dir)

    dst_img = None
    ok = 0
    err = 0
    for i, f in enumerate(files):
        src_img = ImageNda.load(str(f))  # BGR
        name = f.name
        if src_img is None:
            err += 1
            print(i, name, '\tERROR')
            continue
        else:
            ok += 1
            if opt.verbose:
                print(i, name, '\tOK')

        dst_img = cv2.resize(src_img, size.to_tuple_int(), dst_img)
        for _i in range(opt.repeat):
            writer.write(dst_img)

    print('\n压缩帧数：(%d/%d)\n' % (ok, ok + err))


if __name__ == '__main__':
    main()
