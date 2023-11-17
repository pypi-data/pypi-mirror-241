#!/opt/ias/env/bin/python

import argparse
from pathlib import Path

from jcx.text.txt_json import load_json, save_json
from jvi.drawing.color import COLORS7
from jvi.drawing.shape import grid
from jvi.geo.size2d import size_parse
from jvi.image.tile import PanoramaInfo, divide_sparse
from jvi.image.io import trace_image, save_image


def main():
    parser = argparse.ArgumentParser(description='瓦片全景查看工具')
    parser.add_argument('panorama', type=Path, help='匹配全景文件')
    parser.add_argument('-n', '--no-background', action='store_true', help='禁用背景图片')
    parser.add_argument('-d', '--divide-size', type=str, help='切分尺寸，比如：4x4')
    parser.add_argument('-o', '--output', type=Path, help='图输出文件/目录')
    parser.add_argument('-g', '--grid_thickness', type=int, default=None, help='绘制网格的线宽')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    opt = parser.parse_args()

    pano_info = load_json(opt.panorama, PanoramaInfo)
    assert pano_info, '瓦片全景信息加载失败'

    img_pano = pano_info.load_tiles(opt.no_background)
    print('pano shape:', img_pano.shape)
    if opt.grid_thickness:
        grid(img_pano, pano_info.tile_size(), colors=COLORS7, thickness=opt.grid_thickness)
    trace_image(img_pano)

    if opt.output:
        print('图片保存为：', opt.output)
        save_image(img_pano, opt.output)
        if opt.divide_size:
            size = size_parse(opt.divide_size)
            out_dir = Path(opt.output.stem)
            sparse_info = divide_sparse(img_pano, pano_info.tiles, out_dir, size.width, size.height)
            sparse_info.background = str(opt.output)
            out_file = out_dir.with_suffix('.json')
            print('稀疏全景信息信息保存到：', out_file)
            save_json(sparse_info, out_file)


if __name__ == '__main__':
    main()
