#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

import arrow
from jcx.sys.fs import files_in, stem_append
from jvi.common import JIV_STATIC
from jvi.drawing.color import *
from jvi.drawing.shape import polylines, cross, rectangle
from jvi.geo.point2d import array_normalize
from jvi.geo.rectangle import Rect
from jvi.geo.size2d import Size
from jvi.geo.trans import points_cs_trans_in_rect
from jvi.image.infrared import *
from jvi.image.proc import resize
from jvi.image.struct import OscrDetector, OscrParams
from jvi.image.trace import trace_image

IR_ROI: Final = Rect(x=396.0, y=140.0, width=1060, height=800)
"""红外ROI"""

epilog = '''
Examples:

    jvi-infrared src.png
    
'''


def main() -> None:
    parser = argparse.ArgumentParser(description='红外图片处理工具', epilog=epilog)
    parser.add_argument('image_file', type=Path, help='来源图片')
    parser.add_argument('-e', '--exp', type=str, default='.jpg', help='图片文件扩展名')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    assert opt.image_file.exists(), f'图片文件不存在: {opt.image_file}'

    image = ImageNda.load(opt.image_file, cv2.IMREAD_COLOR)

    params = OscrParams((0, 80))
    # params = OscrParams()
    detector = OscrDetector(params)

    objects = detector.detect(image)

    image1 = ImageNda.load('/home/jiang/1/a.jpg', cv2.IMREAD_COLOR)
    resize(image, image1.roi(IR_ROI))

    for ob in objects:
        polygon = points_cs_trans_in_rect(ob.polygon, Rect.one(), IR_ROI)
        polygon = array_normalize(polygon, image1.size())
        polylines(image1, polygon, random_color())
        rectangle(image1, IR_ROI, random_color())

    trace_image(image1, 'test')
    detector.debug_images()


def match_image() -> None:
    a = '/home/jiang/1/a.jpg'
    b = '/home/jiang/1/b.jpg'

    im_a = ImageNda.load(a)
    im_b = ImageNda.load(b)

    size_b = Size(1060, 800)
    center_b = im_a.size().center()
    center_b.x += -34
    center_b.y += -0

    rx = 0.828125
    ry = 1.111111

    r = Rect.from_cs(center_b, size_b)
    print('roi:', r)
    im_roi = im_a.roi(r)
    resize(im_b, im_roi)

    cross(im_a, im_a.size().center(), 15, BLUE, 5)
    cross(im_roi, im_roi.size().center(), 15, PURPLE, 5)

    trace_image(im_a, 'test')

    print('area ratio:', im_roi.size().area() / im_a.size().area())


def show_color() -> None:
    """尝试利用彩虹调色板分类热度图"""
    rainbow_file = JIV_STATIC / 'infrared/rainbow.jpg'
    palette = load_palette_hs(rainbow_file)

    folder = '/home/jiang/ws/trash/sewage/demo/rainbow/'
    files = files_in(folder, '.jpg')
    for file in files:
        im_src = ImageNda.load(file)
        now = arrow.now()
        im_dst = extract_image_ir(palette, im_src)
        print('duration:', arrow.now() - now)

        # trace_image(im_dst, 'dst')
        im_dst.save(stem_append(file, 'dst'))


"""
    src_file = JIV_STATIC / 'infrared/wh1.jpg'
    src = ImageNda.load(src_file)
    src_1c = to_gray(src)
    dst = map_color(src_1c, rainbow_color) # 彩虹调色板

    print(src, dst)

    trace_images([src, dst], 'Infrared', box_size=Size(1920, 540))
    close_all_windows()
"""

if __name__ == '__main__':
    # main()
    # match_image()
    show_color()
