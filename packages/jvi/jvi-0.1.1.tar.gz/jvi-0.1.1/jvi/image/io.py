from pathlib import Path
from typing import Optional

import cv2
import imageio.v2 as iio
from jcx.sys.fs import StrPath, make_parents, files_in
from jiv.geo.size2d import Size
from jiv.image.image_nda import ImageNda, ImageNdas
from jiv.image.proc import resize
from jiv.image.trans import bgr_to_pil


# 参考: [PIL Image file formats](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html)

def _save_images_cv(images: ImageNdas, path: StrPath, fps: float, size: Size = Size()) -> None:
    """保存图片集合成动画/视频文件, 只有 'mp4v'勉强能用 """
    assert images
    path = Path(path)
    size = size or images[0].size()
    make_parents(path)

    fourcc_tab = {'.mp4': 'avc1', '.mjpg': 'mjpg', '.webp': 'webp'}  # require libwebp-dev
    # TODO: avc1/MJPG报错，https://stackoverflow.com/questions/52932157/ \
    #  opencv-ffmpeg-tag-0x34363268-h264-is-not-supported-with-codec/56723380
    fourcc = fourcc_tab.get(path.suffix)
    assert fourcc, '不支持的文件格式'

    fourcc = cv2.VideoWriter_fourcc(*fourcc)
    writer = cv2.VideoWriter(str(path), fourcc, fps, size.to_tuple_int())

    dst_img = ImageNda(size)
    for i, src_img in enumerate(images):
        resize(src_img, dst_img)
        # print('write', i, dst_img.data().shape)
        writer.write(dst_img.data())

    writer.release()


def save_images(images: ImageNdas, path: StrPath, fps: float, size: Size = Size()) -> None:
    """保存图片集合成动画/视频文件"""
    assert images, '没有待保存的图片'
    path = Path(path)
    # print(path.suffix)
    match path.suffix:
        case '.mp4':
            fun = _save_images_iio
        case '.gif' | '.pdf' | '.png' | '.tiff' | '.webp':
            fun = _save_images_pil
        case _:
            raise RuntimeError('不支持的文件格式')
    make_parents(path)

    size = size or images[0].size()
    images = [resize(im, dst_size=size) for im in images]
    fun(images, path, fps)


def _save_images_iio(images: ImageNdas, path: Path, fps: float) -> None:
    """保存图片集合成动画/视频文件"""

    fourcc_tab = {'.mp4': 'h264'}  # require libwebp-dev
    codec = fourcc_tab.get(path.suffix)
    assert codec, '不支持的文件格式'

    writer = iio.get_writer(str(path), format='FFMPEG', mode='I', fps=fps, codec=codec)  # type: ignore

    for im in images:
        writer.append_data(im.data())

    writer.close()


def _save_images_pil(images: ImageNdas, path: Path, fps: float) -> None:
    """保存图片集合成动画/视频文件"""
    ims = [bgr_to_pil(im.data()) for im in images]
    # print(ims)
    duration = int(1 / fps * 1000)
    ims[0].save(path, save_all=True, append_images=ims[1:], duration=duration, loop=0)


def load_images_in(folder: StrPath, ext: str = '.jpg') -> ImageNdas:
    """加载目录下所有指定图片文件"""
    files = files_in(folder, ext)
    return [ImageNda.load(f) for f in files]


def load_image_pairs_in(folder: StrPath, ext: str = '.jpg') -> list[tuple[Path, ImageNda]]:
    """加载目录下所有指定图片文件, 返回路径/图片对数组"""
    files = files_in(folder, ext)
    return [(f, ImageNda.load(f)) for f in files]


class Capture:
    """推向捕获器"""

    def __init__(self, path: StrPath):
        self._capture = cv2.VideoCapture(str(path))

    def at(self, seconds: float) -> Optional[ImageNda]:
        """获取指定位置(时间)的图像"""
        ms = int(seconds * 1000)
        self._capture.set(cv2.CAP_PROP_POS_MSEC, ms)
        ok, frame = self._capture.read()
        return ImageNda(data=frame) if ok else None

    def position(self) -> float:
        """获取位置, 单位秒"""
        return self._capture.get(cv2.CAP_PROP_POS_MSEC) / 1000
