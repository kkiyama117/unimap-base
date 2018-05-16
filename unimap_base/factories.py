import factory
from django.contrib.gis.geos import Point, MultiPolygon, Polygon

from unimap_base import models


class UniversityFactory(factory.DjangoModelFactory):
    name = '京都大学'
    slug = "KU"

    class Meta:
        model = models.University


class CampusFactory(factory.DjangoModelFactory):
    name = "Yoshida-South"
    group = "Yoshida"
    university = factory.SubFactory(UniversityFactory)
    border = MultiPolygon(Polygon(((135.7788544893265, 35.02516649388852),
                                  (135.7787418365479, 35.02509401064209),
                                  (135.7786345481873, 35.02193982894778),
                                  (135.7811370491982, 35.02196399096925),
                                  (135.7811585068703, 35.02276572672252),
                                  (135.7813569903374, 35.02517747619297),
                                  (135.7810780405998, 35.02519285141673),
                                  (135.7804504036903, 35.02520383371765),
                                  (135.7788544893265, 35.02516649388852))
                                  ))

    class Meta:
        model = models.Campus


class BuildingFactory(factory.DjangoModelFactory):
    name = "Yoshida-South Campus Academic Center Bldg North Wing"
    location = Point(35.026304, 135.780816)
    campus = factory.SubFactory(CampusFactory)

    class Meta:
        model = models.Building


class RoomFactory(factory.DjangoModelFactory):
    name = "Kyokita22"
    floor = 2
    building = factory.SubFactory(BuildingFactory)

    class Meta:
        model = models.Room
