# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from unimap_base.models import Border

# モデルクラスとShapefileのカラムのマッピング
border_mapping = {
    'prefecture': 'N03_001',
    'branch': 'N03_002',
    'major_city': 'N03_003',
    'city': 'N03_004',
    'code': 'N03_007',
    'border': 'POLYGON',
}

# ロード対象のShapefile
border_shp = os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)),
                 'data/N03-17_170101.shp'))


def run(verbose=True):
    lm = LayerMapping(Border, border_shp, border_mapping, transform=False,
                      encoding='utf-8')
    lm.save(strict=True, verbose=verbose)


if __name__ == '__main__':
    run()
