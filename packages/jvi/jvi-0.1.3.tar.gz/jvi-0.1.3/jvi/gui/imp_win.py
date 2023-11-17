import cv2
from jcx.ui.key import Key
from jvi.drawing.color import RED, YOLO_GRAY
from jvi.drawing.shape import polylines
from jvi.geo.point2d import Point
from jvi.geo.size2d import Size
from jvi.gui.image_win import ImageWin
from jvi.image.image_nda import ImageNda


class ImpWin(ImageWin):
    """图像处理窗口"""

    def __init__(self, title: str, size: Size):
        super().__init__(title, size)
        self.points = []

    def on_key(self, key: int):
        if key == Key.ESC or key & 0xFF == ord("q"):
            return 1
        elif key == Key.BACKSPACE:
            if self.points:
                self.points.pop()
        elif key > 0:
            print('key:', key)

    def on_draw(self, canvas: ImageNda, _pos: Point):
        color = RED
        if self.points:
            polylines(canvas.data(), self.points, color, 2)

    def on_left_button_down(self, p: Point, flags: int):
        # print(flags)
        self.points.append(p)
        if flags & cv2.EVENT_FLAG_CTRLKEY:
            print('CTRL')
        if flags & cv2.EVENT_FLAG_ALTKEY:
            print('ALT')
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            print('SHIFT')
        # cv2.setWindowTitle()


def main():
    file = './black_flower.jpg'
    image = ImageNda.load(file)
    size = Size(1280, 720)
    win = ImpWin(file, size)

    win.set_backcolor(YOLO_GRAY)
    win.set_background(image)
    print(win.size())
    win.run()


if __name__ == '__main__':
    main()
