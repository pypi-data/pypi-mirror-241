#!/opt/ias/env/bin/python

import cv2
import numpy as np
from jiv.geo.point2d import Point
from jiv.geo.rectangle import Rect
from jiv.image.util import ndarray_rect, ndarray_size
from numpy import uint8


def find_template(src: np.ndarray, templ: np.ndarray) -> tuple[Point, float]:
    """多通道图像模板匹配，逐像素搜索，大图难行"""

    assert src.dtype == templ.dtype
    assert src.shape[2] == templ.shape[2]  # 图像通道数一致

    src = src.astype(int)
    templ = templ.astype(int)

    size = ndarray_size(templ)

    h = templ.shape[0]
    w = templ.shape[1]
    h_max = src.shape[0] - h + 1
    w_max = src.shape[1] - w + 1
    var_min = float('inf')
    pos = Point(0, 0)
    for y in range(h_max + 1):
        # if y % 100 == 0:
        print('搜索行：', y)
        for x in range(w_max + 1):
            print('搜索列：', x, var_min)
            r = Rect(x, y, w, h)
            roi = ndarray_rect(src, r)
            v = np.var(roi - templ)
            if v < var_min:
                var_min = v
                pos = Point(x, y)
    return pos, var_min


def find_template2(src: np.ndarray, templ: np.ndarray) -> tuple[Point, float]:
    """单通道图像模板匹配"""

    # src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # templ = cv2.cvtColor(templ, cv2.COLOR_BGR2GRAY)

    method = cv2.TM_SQDIFF
    result = cv2.matchTemplate(src, templ, method)

    index = np.argmin(result)
    row = index // result.shape[1]
    col = index % result.shape[1]

    return Point(col, row), result[row, col]


def find_template_tile(src: np.ndarray, templ: np.ndarray) -> tuple[Point, float]:
    """多通道图像模板匹配，基于对齐的块"""

    assert src.dtype == templ.dtype
    assert src.shape[2] == templ.shape[2]  # 图像通道数一致

    src = src.astype(int)
    templ = templ.astype(int)

    rect = Rect.from_size(ndarray_size(src))
    size = ndarray_size(templ)

    var_min = float('inf')
    pos = Point(0, 0)
    rects = rect.to_tiles(size=size, need_round=True)
    for r in rects:
        # print('搜索列：', r, var_min)
        roi = ndarray_rect(src, r)
        v = np.var(roi - templ)
        if v < var_min:
            var_min = v
            pos = r.lt()

    return pos, var_min


def find_template_test():
    img = np.ones([5, 6, 1], dtype=uint8)
    img[3, 3] = 10

    temp = np.ones([2, 2, 1], dtype=uint8)
    temp[1, 1] = 11

    print('img:', img)
    print('temp:', temp)

    p, v = find_template2(img, temp)
    print(p, v)


if __name__ == '__main__':
    find_template_test()
