from abc import ABC
from typing import Any

import cv2
from jcx.sys.fs import StrPath
from jcx.ui.key import Key
from jiv.drawing.color import RED, Color
from jiv.drawing.shape import polylines
from jiv.geo.point2d import Point, Points
from jiv.geo.size2d import Size, SIZE_HD
from jiv.image.image_nda import ImageNda
from jiv.image.proc import resize


def mouse_callback(event: int, x: int, y: int, flags: int, me: Any) -> None:
    if me:
        me.on_mouse(event, Point(x, y), flags)


class ImageWin(ABC):

    def __init__(self, title: str, size: Size = SIZE_HD):
        self._title = title
        cv2.namedWindow(self._title)
        cv2.setMouseCallback(self._title, mouse_callback, self)
        self._size = size
        self._canvas: ImageNda = ImageNda(size)
        self._background: ImageNda = ImageNda(size)
        self._pos = Point()

    def __del__(self) -> None:
        cv2.setMouseCallback(self._title, None, None)
        cv2.destroyWindow(self._title)

    def size(self) -> Size:
        """"获取窗口尺寸（客户区）"""
        return self._size

    def resize(self, size: Size) -> None:
        """"改变窗口尺寸（客户区）"""
        if self._size != size:
            self._size = size
            self._canvas = ImageNda(size)

    def background(self) -> ImageNda:
        """"获取背景图"""
        return self._background

    def background_size(self) -> Size:
        """"获取窗口尺寸（客户区）"""
        return self._background.size()

    def set_pos(self, p: Point) -> None:
        cv2.moveWindow(self._title, int(p.x), int(p.y))

    def set_background(self, image: ImageNda) -> None:
        """设置背景"""
        self._background = image.clone()

    def set_backcolor(self, color: Color) -> None:
        """设置背景色"""
        self._background.set_to(color)

    def canvas(self) -> ImageNda:
        return self._canvas

    def snapshot(self, file: StrPath) -> None:
        """抓图"""
        assert self
        self._canvas.save(file)
        print(f'抓图保存: {file}')

    def refresh(self) -> None:
        """刷新窗口"""
        resize(self._background, self._canvas)
        self.on_draw(self._canvas, self._pos)
        cv2.imshow(self._title, self._canvas.data())

    def run(self, interval: int = 200) -> int:
        """运行消息循环"""
        key = -1
        while True:
            self.refresh()
            if key > 0:
                r = self.on_key(key)
                if r:
                    cv2.destroyAllWindows()
                    return r
            else:
                self.on_idle()
            key = cv2.waitKey(interval)

    @staticmethod
    def wait_key(delay: int = 0) -> int:
        """等待按键，BUG:在接收鼠标消息后，小键盘按键消息无法接收"""
        return cv2.waitKey(delay)

    def on_mouse_move(self, _pos: Point, _flags: int) -> None:
        """设置鼠标移动事件响应"""
        pass

    def on_left_button_down(self, _pos: Point, _flags: int) -> None:
        """设置鼠标左键按下事件响应"""
        pass

    def on_right_button_down(self, _pos: Point, _flags: int) -> None:
        """设置鼠标右键按下事件响应"""
        pass

    def on_draw(self, _canvas: ImageNda, _pos: Point) -> None:
        """设置窗口重绘事件响应"""
        pass

    def on_key(self, key: int) -> int:
        """设置窗口重绘事件响应"""
        if key == Key.ESC:
            return 1
        return 0

    def on_mouse(self, event: int, pos: Point, flags: int) -> None:
        self._pos = pos
        if event == cv2.EVENT_MOUSEMOVE:
            self.on_mouse_move(pos, flags)
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.on_left_button_down(pos, flags)
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.on_right_button_down(pos, flags)

    def on_idle(self) -> None:
        """但窗口空闲时完成的工作"""
        pass


class PolylinesWin(ImageWin):

    def __init__(self, title: str, size: Size):
        super().__init__(title, size)
        self.points: Points = []
        self.counter = 0

    def on_key(self, key: int) -> int:
        if key == Key.ESC:
            return 1
        elif key == Key.BACKSPACE:
            if self.points:
                self.points.pop()
        elif key > 0:
            print('key:', key)
        return 0

    def on_draw(self, canvas: ImageNda, _pos: Point) -> None:
        color = RED
        if self.points:
            polylines(canvas, self.points, color, 2)

    def on_left_button_down(self, p: Point, flags: int) -> None:
        # print(flags)
        self.points.append(p)
        if flags & cv2.EVENT_FLAG_CTRLKEY:
            print('CTRL')
        if flags & cv2.EVENT_FLAG_ALTKEY:
            print('ALT')
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            print('SHIFT')
        # cv2.setWindowTitle()

    def on_idle(self) -> None:
        self.counter += 1
        if self.counter % 20 == 0:
            print('#%d idle' % self.counter)


def main() -> None:
    file = '../../static/black_flower.jpg'
    image = ImageNda.load(file)
    win = PolylinesWin(file, Size(640, 640))
    win.set_background(image)

    win.run()


if __name__ == '__main__':
    main()
