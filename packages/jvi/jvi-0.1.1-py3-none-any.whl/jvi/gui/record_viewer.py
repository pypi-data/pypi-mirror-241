from dataclasses import dataclass
from pathlib import Path
from typing import TypeAlias, Protocol

from jcx.sys.fs import StrPath
from jiv.geo.point2d import Point
from jiv.geo.size2d import Size, SIZE_HD
from jiv.gui.image_viewer import ImageViewer
from jiv.image.image_nda import ImageNda
from rustshed import Option, Null


@dataclass
class ImageEntry(Protocol):
    """图片信息"""

    def load_image(self) -> ImageNda:
        """加载图片"""
        pass

    def image_file(self) -> Path:
        """获取图片路径"""
        pass

    def draw_on(self, canvas: ImageNda, pos: Point) -> None:
        """把图片信息绘制在画板上"""
        pass


ImageEntries: TypeAlias = list[ImageEntry]
"""图片信息集合"""


class RecordViewer(ImageViewer):
    """记录图片查看窗口"""

    def __init__(self, title: str, size: Size = SIZE_HD):
        super().__init__(title, size)
        self._records: ImageEntries = []

    def on_draw(self, canvas: ImageNda, pos: Point) -> None:
        """设置窗口重绘事件响应"""
        self.record().draw_on(canvas, pos)

    def image_at(self, index: int) -> ImageNda:
        """获取指定索引的图片"""
        return self._records[index].load_image()

    def cur_image_file(self) -> Path:
        return self._records[self._index].image_file()

    def image_count(self) -> int:
        """获取图片总数"""
        return len(self._records)

    def set_records(self, records: ImageEntries) -> None:
        """设置记录"""
        # self._records = sorted(records)
        self._records = records
        if self._records:
            self.change_background()

    def record(self) -> ImageEntry:
        """获取当前记录"""
        return self._records[self._index]


@dataclass
class FileRecord(ImageEntry):
    """文件记录"""
    path: Path
    """图片路径"""
    image: Option[ImageNda] = Null
    """图片对象, 内存中的图片数据"""

    def load_image(self) -> ImageNda:
        """加载图片"""
        return ImageNda.load(self.path)

    def image_file(self) -> Path:
        """获取图片路径"""
        return self.path

    def draw_on(self, canvas: ImageNda, _pos: Point) -> None:
        """把记录绘制在画板上"""
        # label = self.path.name
        # draw_boxf(canvas, Rect(0.25, 0.25, 0.5, 0.5), GREEN, label, 3)
        pass


FileRecords: TypeAlias = list[FileRecord]
"""文件记录列表"""


def load_dir_records(src_dir: StrPath) -> FileRecords:
    """加载目录下的图片信息记录"""
    src_dir = Path(src_dir)
    # print(src_dir)
    files = sorted(src_dir.rglob('*.jpg'))

    rs = [FileRecord(f) for f in files]
    return rs


def main():
    folder = '/home/jiang/ws/trash/dates/2023-02-25/image'

    rs = load_dir_records(folder)
    assert len(rs) > 0

    win = RecordViewer('files://' + folder)
    win.set_records(rs)

    print('image number:', win.image_count())
    win.run()


if __name__ == '__main__':
    main()
