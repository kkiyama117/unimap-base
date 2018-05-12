from django.contrib.gis.db import models as gismodels
from django.db import models
from model_utils.managers import InheritanceManager


class BaseModel(models.Model):
    """全モデルの基幹モデル

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


class Location(models.Model):
    """緯度経度を示す"""
    latitude = models.FloatField(null=False, default=35.026304)
    longitude = models.FloatField(null=False, default=135.780816)

    objects = InheritanceManager()

    class Meta:
        unique_together = ("latitude", "longitude")
        verbose_name_plural = "location"

    def __str__(self):
        return f"latitude: {self.latitude}, longitude: {self.longitude}"


class AbstractPlace(BaseModel):
    """場所を示す全てのクラスの元

    location を持つ.
    極限まで抽象化するならParentというForeignkeyを持たせて全ての建物,
    敷地の入れ子を管理する事になるだろうがそこまでするかは要検討と思われる.
    """
    location = models.ForeignKey("Location", on_delete=models.CASCADE,
                                 related_name="%(app_label)s_%(class)s"
                                              "_location",
                                 related_query_name="%(app_label)s_%(class)ss")

    class Meta(BaseModel.Meta):
        abstract = True


class Place(AbstractPlace):
    """大学に関係ない一般的な場所

    基本的に `AbstaractPlace` と同じ"""
    pass


class University(AbstractPlace):
    """大学を表すクラス"""
    slug = models.SlugField(max_length=32)

    class Meta(AbstractPlace.Meta):
        verbose_name_plural = "universities"


class Campus(AbstractPlace):
    """キャンパスを表すクラス"""
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    group = models.CharField(max_length=128)

    class Meta(AbstractPlace.Meta):
        verbose_name_plural = "campuses"


class Building(AbstractPlace):
    """建物を表すクラス"""
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)


class Room(AbstractPlace):
    """部屋を表す"""
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    # Validator はmodelformを使うときだけ
    floor = models.IntegerField()


class Border(gismodels.Model):
    prefecture = gismodels.CharField('都道府県名', max_length=10)
    branch = gismodels.CharField('支庁名', max_length=20, blank=True)
    major_city = gismodels.CharField('群・政令市名', max_length=20, blank=True)
    city = gismodels.CharField('市区町村名', max_length=20, blank=True)
    code = gismodels.CharField('行政区域コード', max_length=5)
    # longitude = models.FloatField()
    # latitude = models.FloatField()

    border = gismodels.MultiPolygonField(srid=4612)

    class Meta:
        verbose_name = "行政区域"
        verbose_name_plural = "行政区域一覧"

    def __str__(self):
        return "%s_%s_%s(%s)" % (
            self.prefecture, self.major_city, self.city, self.code)
