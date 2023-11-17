from typing import Optional

import cv2  # type: ignore
from numpy import ndarray

from jiv.geo.point2d import Point
from jiv.geo.size2d import Size
from jiv.gui.image_viewer import ImageViewer


class VideoViewer(ImageViewer):
    """视频查看窗口"""

    def __init__(self, url, title: str, size: Size = Size()):
        super().__init__(title, size)  # REMARK：用URL可能因为汉字等字符报错
        self.__frames = {}
        self.__capture = cv2.VideoCapture(str(url))

        w = int(self.__capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.__capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.__image_size = Size(w, h)

        assert self.image_count() > 0
        self.change_background()

    def is_opened(self) -> bool:
        """判定是否成功打开"""
        return self.__capture.isOpened()

    def image_size(self) -> Size:
        """获取视频图片尺寸"""
        return self.__image_size

    def on_draw(self, canvas: ndarray, pos: Point):
        """设置窗口重绘事件响应"""
        # self.record().draw_on(canvas, pos)
        pass

    def image_at(self, index: int) -> Optional:
        """获取指定索引的图片"""

        print('index:', index)

        frame = self.__frames.get(index)
        if frame is None:
            pos = int(self.__capture.get(cv2.CAP_PROP_POS_FRAMES))
            assert pos <= index
            while pos <= index:
                ok, frame = self.__capture.read()
                if not ok:
                    break
                self.__frames[pos] = frame
                pos += 1
            frame = self.__frames.get(index)

        return frame

    def image_count(self) -> int:
        """获取图片总数，注意：实际帧数可能该值"""
        return int(self.__capture.get(cv2.CAP_PROP_FRAME_COUNT))


def main():
    file = 'file:///home/jiang/ws/lift/2021-08-19/1.mp4'
    # file = '/home/jiang/ws/nvidia/nano_test/data/1.h264'

    win = VideoViewer(file, size=Size(1280, 720))
    print("frame count:", win.image_count())
    print('video size:', win.image_size())
    win.run()


if __name__ == '__main__':
    main()
