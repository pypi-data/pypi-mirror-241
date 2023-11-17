from typing import Optional, TypeAlias

import cv2
import numpy as np
from jcx.sys.fs import StrPath
from jvi.image.image_nda import ImageNda


def map_color(src: ImageNda, colormap: int | np.ndarray, dst: Optional[ImageNda] = None) -> ImageNda:
    """灰度图转换为彩色图"""
    # 参考: https://docs.opencv.org/4.x/d3/d50/group__imgproc__colormap.html
    # assert src.channel_num() == 1, '输入图像必须为灰度图'
    if dst:
        assert dst.same_size(src), '输出图片必须与输入图片尺寸相同'
    dd = cv2.applyColorMap(src.data(), colormap, dst and dst.data())
    assert isinstance(dd, np.ndarray)
    return ImageNda(data=dd)


PaletteHS: TypeAlias = list[tuple[int, int]]
"""调色板类型定义"""


def load_palette_hs(path: StrPath) -> PaletteHS:
    """从调色板图片加载(色度,饱和度)调色板数据"""
    im = ImageNda.load(path)
    mat = im.data()
    bgr_col = np.ascontiguousarray(mat[:, 1:2])  # 只截取一列

    hsv_col = cv2.cvtColor(bgr_col, cv2.COLOR_BGR2HLS_FULL)
    hs_col = hsv_col[:, :, 0:2]  # 去掉亮度通道
    # print('h1 max:', hs_col.max())

    palette = hs_col.reshape(-1, 2)  # 变为(h, s)对数组, 温度:高->低
    palette = palette[::-1]  # 逆序, 温度:低->高
    return [(h, s) for h, s in palette.tolist()]


def extract_image_ir(palette: PaletteHS, im_src: ImageNda, im_dst: Optional[ImageNda] = None) -> ImageNda:
    """利用调色版从伪彩色热图中分类单通道热图"""
    im_dst = im_dst or ImageNda.new_as(im_src, channel=1)  # 同尺寸灰度图

    assert im_src.same_size(im_dst), '图像尺寸不一致'
    assert im_src.channel_num() == 3, '输入图像必须为BGR格式'
    assert im_dst.channel_num() == 1, '输入图像必须为单通'

    mat_hsv = cv2.cvtColor(im_src.data(), cv2.COLOR_BGR2HLS_FULL)  # 转成HSV图
    mat_hs = mat_hsv[:, :, 0:2]  # 只取H和S通道
    arr_hs = mat_hs.reshape(-1, 2)  # 转成点数组
    mat_dst = im_dst.data().reshape(-1)  # 用一维方式访问图像
    for i, (h, s) in enumerate(arr_hs):  # 遍历HS图像
        # print(f'#{i} {h} {s}')
        d2_min = 100000
        idx_min = 0
        for j in range(len(palette)):  # 搜索最接近的调色板项
            h1, s1 = palette[j]
            d2 = (h - h1) ** 2 + (s - s1) ** 2
            if d2 < d2_min:
                d2_min = d2
                idx_min = j
        mat_dst[i] = idx_min
    return im_dst


def to_color(src: ImageNda, dst: Optional[ImageNda] = None) -> ImageNda:
    """灰度图转换为彩色图"""
    '''
    
    rainbow_file = JIV_STATIC / 'infrared/rainbow.jpg'
    rainbow = ImageNda.load(rainbow_file)
    m = rainbow.data()
    rainbow_color = np.ascontiguousarray(m[:, 1:2])
    print(m.shape, rainbow_color.shape)

    src_file = JIV_STATIC / 'infrared/wh1.jpg'
    src = ImageNda.load(src_file)
    src_1c = to_gray(src)
    dst = map_color(src_1c, rainbow_color) # 彩虹调色板

    print(src, dst)

    trace_images([src, dst], 'Infrared', box_size=Size(1920, 540))
    close_all_windows()

    '''
    return map_color(src, cv2.COLORMAP_JET, dst)
