from django.contrib.gis.db import models
from model_utils.managers import InheritanceManager


class BaseModel(models.Model):
    """基本モデルの基幹モデル

    django model utils の InheritanceManager を使う.
    """
    name = models.CharField(max_length=256, null=False, blank=False,
                            unique=True)
    objects = InheritanceManager()

    class Meta:
        abstract = True
        ordering = ["name", ]

    def __str__(self):
        return self.name


class Place(BaseModel):
    """建物を表すクラス"""
    location = models.PointField(unique=True)


class University(BaseModel):
    """大学を表すクラス"""
    slug = models.SlugField(max_length=32)

    class Meta:
        verbose_name = "大学"
        verbose_name_plural = "大学"


class Campus(BaseModel):
    """キャンパスを表すクラス"""
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    # 京大の吉田キャンパス(本部構内, 吉田南構内 etc. を示すためのグループ)
    group = models.CharField(max_length=128)
    border = models.MultiPolygonField(srid=4612)

    class Meta:
        verbose_name = "キャンパス"
        verbose_name_plural = "キャンパス"


class Building(BaseModel):
    """建物を表すクラス"""
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    location = models.PointField(unique=True)

    class Meta:
        verbose_name = "建物"
        verbose_name_plural = "建物"


class Room(BaseModel):
    """部屋を表す"""
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.PositiveIntegerField()

    class Meta:
        verbose_name = "教室"
        verbose_name_plural = "教室"


class Border(models.Model):
    """行政区域のクラス

    大学に関係ないところで使うか?"""
    prefecture = models.CharField('都道府県名', max_length=10)
    branch = models.CharField('支庁名', max_length=20, blank=True)
    major_city = models.CharField('群・政令市名', max_length=20, blank=True)
    city = models.CharField('市区町村名', max_length=20, blank=True)
    code = models.CharField('行政区域コード', max_length=5)

    border = models.MultiPolygonField(srid=4612)

    class Meta:
        verbose_name = "行政区域"
        verbose_name_plural = "行政区域一覧"

    def __str__(self):
        return "%s_%s_%s(%s)" % (
            self.prefecture, self.major_city, self.city, self.code)
