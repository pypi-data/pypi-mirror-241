from typing import Optional

import cv2
from jvi.geo.size2d import Size
from jvi.image.image_nda import ImageNda, ImageNdas
from jvi.image.proc import tile


def trace_image(image: ImageNda, title: Optional[str] = None, delay: int = 0, box_size: Optional[Size] = None,
                auto_close: bool = True) -> tuple[int, ImageNda]:
    """跟踪显示图片，自动缩放"""
    assert isinstance(image, ImageNda)

    src_size = image.size()
    title = title or str(image)
    if box_size:
        dst_size = src_size.scale_in(box_size).round()
        img_dst = cv2.resize(image.data(), dst_size.to_tuple_int())
    else:
        img_dst = image.data()
    cv2.imshow(title, img_dst)
    key = cv2.waitKey(delay)
    if auto_close:
        cv2.destroyWindow(title)
    assert isinstance(key, int)
    return key, ImageNda(data=img_dst)


def trace_images(images: ImageNdas, title: Optional[str] = None, delay: int = 0, box_size: Size = Size(),
                 auto_close: bool = True) -> tuple[int, ImageNda]:
    """跟踪显示多张图片(并列)"""
    image = tile(images, box_size=box_size)
    return trace_image(image, title, delay, box_size, auto_close)


def close_all_windows() -> None:
    """关闭所有窗口"""
    cv2.destroyAllWindows()
