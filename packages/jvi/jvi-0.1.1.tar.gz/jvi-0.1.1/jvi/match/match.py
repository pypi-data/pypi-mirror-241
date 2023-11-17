from dataclasses import dataclass
from pathlib import Path
from typing import Optional, TypeAlias

import cv2
import numpy as np
from jcx.sys.fs import files_in
from jiv.drawing.color import LIME
from jiv.geo.gp import dist_tuple
from jiv.geo.rectangle import Rect, Rects
from jiv.geo.size2d import Size, SIZE_HD
from jiv.image.image_nda import ImageNda
from jiv.image.proc import resize
from loguru import logger

DMatches: TypeAlias = list[cv2.DMatch]
"""匹配点集"""
DMatchMat: TypeAlias = list[DMatches]
"""匹配矩阵, 每个点匹配一个以上候选点, 但前只选择一个候补匹配点"""

KeyPoints: TypeAlias = tuple[cv2.KeyPoint, ...]
"""关键点集"""
DMatchPair: TypeAlias = tuple[cv2.DMatch, cv2.DMatch]
"""匹配点对"""

DMatchPairs: TypeAlias = tuple[DMatchPair, ...]
"""匹配点集合, 这里是257维"""


@dataclass(frozen=True)
class ImageMatchParams:
    """匹配参数"""

    nfeatures: int = 256
    """匹配的特征数上限"""
    min_match_count: int = 4
    """最少匹配特征数，低于该值表示完全失配"""
    max_top2_ratio: float = 0.7
    """最优/次优匹配点匹配距离比值，越小则最优匹配越可信，该特征越好"""
    size: Size = Size(224, 224)
    """图像尺寸"""


class ImageMatcher:
    """图像匹配器"""

    def __init__(self, params: ImageMatchParams = ImageMatchParams()):
        self.params = params
        self.detector = cv2.SIFT_create(nfeatures=params.nfeatures)
        # self.detector = cv2.ORB_create(nfeatures=params.nfeatures)

        flann_index_kdtree = 0
        index_params = dict(algorithm=flann_index_kdtree, trees=5)
        search_params = dict(checks=50)

        self.flann = cv2.FlannBasedMatcher(index_params, search_params)

        self.im1 = ImageNda(self.params.size)
        self.im2 = ImageNda(self.params.size)

    def match(self, image1: ImageNda, image2: ImageNda, match_im: Optional[ImageNda] = None) -> float:
        """匹配两幅图像，获取平均匹配距离(相对)"""
        size = self.params.size
        resize(image1, self.im1)
        resize(image2, self.im2)

        kp1, des1 = self.detector.detectAndCompute(self.im1.data(), None)
        kp2, des2 = self.detector.detectAndCompute(self.im2.data(), None)

        try:
            matches = self.flann.knnMatch(des1, des2, k=2)  # 取两个点，方便比较
        except cv2.error:
            # 因为图像内容突变或平坦触发异常，暂时无解
            # 参考：http://5.9.10.113/66064786/opencv-python-sift-crashing
            logger.error('flann.knnMatch error')
            return 0

        good_matches = self.get_good_matches(matches)
        # print('good:', len(good))

        dist = self.match_dist(good_matches, kp1, kp2, size.width)

        if match_im is not None:
            self.draw_match_image(dist, good_matches, kp1, kp2, match_im, size)

        return dist  # TODO: 归一化，将就

    def get_good_matches(self, matches: DMatchPairs) -> DMatchMat:
        """过滤掉两个候选匹配差异不大的情况，减少错配"""
        good_matches = []
        for m, n in matches:
            if m.distance < self.params.max_top2_ratio * n.distance:
                good_matches.append([m])
        return good_matches

    def draw_match_image(self, dist: float, good: DMatches, kp1: KeyPoints, kp2: KeyPoints,
                         match_im: ImageNda, size: Size) -> None:
        """画出匹配图, 用于调试"""
        out_size = match_im.size()
        in_size = size.scale((2, 1))
        r = Rect.from_oi(out_size, in_size)
        img_center = match_im.roi(r)
        cv2.drawMatchesKnn(self.im1.data(), kp1, self.im2.data(), kp2, good, img_center.data())
        label = 'matches=%d dist=%d' % (len(good), dist)
        cv2.putText(match_im.data(), label, (8, 16), 0, 0.5, LIME.bgr())

    def match_dist(self, good_matches: DMatchMat, kp1: KeyPoints, kp2: KeyPoints, max_dist: float) -> float:
        """计算良好匹配的距离"""
        dist = max_dist
        if len(good_matches) > self.params.min_match_count:
            dists = []
            for m in good_matches:
                d = dist_tuple(kp1[m[0].queryIdx].pt, kp2[m[0].trainIdx].pt)
                dists.append(d)
            dists = sorted(dists)
            dist = dists[len(dists) // 2]  # 取中位数作为距离
        return dist

    def match_tiles(self, image1: ImageNda, image2: ImageNda, tiles: Rects) -> list[float]:
        """按瓦片区域分块匹配"""

        dists = []
        for r in tiles:
            # print('r:', r)
            im1 = image1.roi(r)
            im2 = image2.roi(r)
            # rectangle(self.img_det, r, PINK)
            match_img = np.zeros_like(image2.data())  # FIXME
            d = self.match(im1, im2, match_img.data())
            dists.append(round(d, 2))
            # cv2.imshow('matches', match_img)
            # cv2.waitKey(0)
        return dists
