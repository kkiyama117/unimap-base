from django.db import models
from model_utils.managers import InheritanceManager


class BaseModel(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False,
                            unique=True)
    objects = InheritanceManager()

    class Meta:
        abstract = True
        ordering = ["name", ]

    def __str__(self):
        return self.name


class Place(BaseModel):
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)

    class Meta:
        abstract = True


class University(Place):
    """大学を表すクラス"""
    slug = models.SlugField(max_length=32)


class Campus(Place):
    """キャンパスを表すクラス"""
    name = models.CharField(max_length=256)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    group = models.CharField(max_length=128)


class Building(Place):
    """建物を表すクラス"""
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)


class Room(BaseModel):
    """部屋を表す"""
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    # Validator はmodelformを使うときだけ
    floor = models.IntegerField()
