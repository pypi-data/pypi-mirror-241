from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional

from jcx.ui.key import Key
from jvi.geo.size2d import Size, SIZE_HD
from jvi.gui.image_win import ImageWin
from jvi.image.image_nda import ImageNda


@dataclass
class ImageRecord:
    """传感器参数"""
    file: str = ''
    image: Optional[ImageNda] = None


class ImageViewer(ImageWin):
    """图像查看窗口"""

    def __init__(self, title: str, size: Size = SIZE_HD):
        super().__init__(title, size)
        self.key_tab = {
            ord("a"): -1,
            ord("d"): 1,
            ord("w"): 10,
            ord("s"): -10
        }
        self._src_dir = None  # 派生类使用
        self._index = 0
        self._pre_index = -1
        self._preload_step = 1
        self._preload_index = 0
        self.help_msgs = [
            "导航按键表：",
            "  [a] 导航到前一副图片",
            "  [d] 导航到后一副图片",
            "  [w] 导航到前十副图片",
            "  [s] 导航到后十副图片",
        ]

    @abstractmethod
    def image_at(self, index: int) -> ImageNda:
        """获取指定索引的图片"""
        pass

    @abstractmethod
    def image_count(self) -> int:
        """获取图片总数"""
        pass

    def on_change_image(self, index: int) -> None:
        """当图片改变时更新数据"""
        pass

    def on_key(self, key: int) -> int:
        """按键处理程序"""
        if key == Key.ESC:
            return 1
        elif key == -1:
            return 0
        elif key == Key.F1:
            self.show_help()
        else:
            # print('key:', key)
            self.jump_to(self.key_tab.get(key, 0))
        return 0

    def jump_to(self, offset: int) -> None:
        """导航到指定偏移量"""
        self._index += offset
        self._index = max(self._index, 0)
        self._index = min(self._index, self.image_count() - 1)
        self.change_background()

        self._preload_step = offset
        self._preload_index = self._index

    def change_background(self) -> None:
        """改变背景"""
        if self._index != self._pre_index:
            image = self.image_at(self._index)
            self.set_background(image)
            self._pre_index = self._index
            self.on_change_image(self._index)

    def show_help(self) -> None:
        """显示当前帮助"""
        for s in self.help_msgs:
            print(s)

    def on_idle(self) -> None:
        self._preload_index += self._preload_step
        if 0 <= self._preload_index < self.image_count():
            self.image_at(self._preload_index)
