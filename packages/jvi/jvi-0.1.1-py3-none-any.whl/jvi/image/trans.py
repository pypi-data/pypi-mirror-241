import cv2
import numpy as np
from PIL.Image import Image as PilImage, fromarray
from jiv.image.image_nda import ImageNda


def bgr_to_pil(bgr: np.ndarray) -> PilImage:
    """BGR图像转PIL图像"""
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    return fromarray(rgb)


def pil_to_bgr(pil: PilImage) -> np.ndarray:
    """PIL图像转BGR图像"""
    rgb = np.asarray(pil)
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    assert isinstance(bgr, np.ndarray)
    return bgr


def pil_to_nda(pil: PilImage) -> ImageNda:
    """PIL图像转ImageNda图像"""
    im = pil_to_bgr(pil)
    return ImageNda(data=im)
