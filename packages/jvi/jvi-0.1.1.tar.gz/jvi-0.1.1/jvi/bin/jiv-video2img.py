#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import arrow
import cv2
from arrow import Arrow
from numpy import ndarray

from jcx.sys.fs import time_to_file, make_parents
from jcx.ui.key import Key
from jiv.geo.point2d import Point
from jiv.geo.size2d import size_parse, Size
from jiv.gui.video_viewer import VideoViewer

TITLE = 'video2image'


class ImageCapture(VideoViewer):
    """图片抓取"""

    def __init__(self, url, dst_dir: Path, size: Size = Size(), start_time: Arrow = arrow.now()):
        super().__init__(url, TITLE, size)
        self.__dst_dir = dst_dir
        self.__start_time = start_time

    def on_key(self, key: int):
        """按键响应"""
        if key == Key.BLANK:
            self.__save_image()
        else:
            return super().on_key(key)
        return 0

    def on_draw(self, canvas: ndarray, pos: Point):
        """设置窗口重绘事件响应"""
        # self.record().draw_on(canvas, pos)
        pass

    def __save_image(self):
        """保存图片"""
        image = self.image_at(self._index)
        if image is None:
            print('[ERROR] image is none')
            return

        interval = self._index * 1000000 / 25
        time = self.__start_time.shift(microseconds=interval)
        file = self.__dst_dir / time_to_file(time, '.jpg')
        make_parents(file)
        cv2.imwrite(str(file), image)
        print('save to:', file)


# file = 'file:///home/jiang/ws/lift/2021-08-19/1.mp4'

def main():
    parser = argparse.ArgumentParser(description='视频转图片工具')
    parser.add_argument('src_url', type=Path, help='来源视频URL')
    parser.add_argument('dst_dir', type=Path, help='目的图片所在目录')
    parser.add_argument('-e', '--ext', type=str, default='.jpg', help='图片文件扩展名')
    parser.add_argument('-s', '--size', type=str, default='HD', help='输出视频尺寸(HD)')
    parser.add_argument('-i', '--interval', type=float, default=1, help='时间间隔')
    parser.add_argument('-t', '--start_time', type=str, help='图片开始时间')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    size = size_parse(opt.size)
    # TODO: start_time解析
    win = ImageCapture(opt.src_url, opt.dst_dir, size=Size(1280, 720))
    if not win.is_opened():
        print('[ERROR] cannot open url:', opt.src_url)
    print("frame count:", win.image_count())
    print('video size:', win.image_size())
    # print(opt.start_time)

    win.run()


if __name__ == '__main__':
    main()
