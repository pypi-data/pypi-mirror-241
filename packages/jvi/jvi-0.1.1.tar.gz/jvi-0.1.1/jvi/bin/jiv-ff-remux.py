#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import sh
from jcx.sys import fs


def main() -> None:
    parser = argparse.ArgumentParser('批量转码工具')
    parser.add_argument('src_dir', type=Path, help='文件来源目录')
    parser.add_argument('dst_dir', type=Path, help='文件目标目录')
    parser.add_argument('-e', '--src_ext', type=str, default='.mp4', help='来源视频文件扩展名')
    parser.add_argument('-d', '--dst_ext', type=str, default='.mp4', help='目标视频文件扩展名')
    parser.add_argument('-V', '--vcodec', type=str, default='h264', help='视频编码: h264/h265')
    parser.add_argument('-a', '--acodec', type=str, default=None, help='音频编码codec')
    parser.add_argument('-s', '--subtitle_ext', type=str, default='.srt', help='字幕文件扩展名')
    parser.add_argument('--crop', type=str, default=None, help='裁切尺寸, 如: 960:720')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    files = fs.files_in(opt.src_dir, opt.src_ext)

    print('src files:', len(files))

    vcodec_opts = {
        'h264': ['-c:v', 'h264_nvenc'],
        'h265': ['-vcodec', 'hevc']
    }
    vcodec_opt = vcodec_opts[opt.vcodec]

    ff = sh.Command('/usr/local/bin/ffmpeg')
    for i, src in enumerate(files):
        print(f'#{i + 1} {src} ...')
        sub = src.with_suffix(opt.subtitle_ext)
        dst = opt.dst_dir / (src.stem + opt.dst_ext)
        if dst.is_file():
            print(f'  SKIP: {dst}')
            continue
        args = ['-i', src]
        if sub.is_file():
            args.extend(['-i', sub])
        if opt.crop:
            args.extend(['-vf', f'crop={opt.crop}'])
        args.extend(vcodec_opt)
        if opt.acodec:
            args.extend(['-acodec', opt.acodec])
        args.append(dst)
        ff(*args)


if __name__ == '__main__':
    main()
