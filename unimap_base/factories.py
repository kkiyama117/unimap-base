import factory
from unimap_base import models


class LocationFactory(factory.DjangoModelFactory):
    longitude = 0.0
    latitude = 0.0

    class Meta:
        model = models.Location


class UniversityFactory(factory.DjangoModelFactory):
    name = '京都大学'
    slug = "KU"
    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = models.University


class CampusFactory(factory.DjangoModelFactory):
    name = "Yoshida-South"
    group = "Yoshida"
    location = factory.SubFactory(LocationFactory)
    university = factory.SubFactory(UniversityFactory)

    class Meta:
        model = models.Campus


class BuildingFactory(factory.DjangoModelFactory):
    name = "Yoshida-South Campus Academic Center Bldg North Wing"
    location = factory.SubFactory(LocationFactory)
    campus = factory.SubFactory(CampusFactory)

    class Meta:
        model = models.Building


class RoomFactory(factory.DjangoModelFactory):
    name = "Kyokita22"
    floor = 2
    building = factory.SubFactory(BuildingFactory)
    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = models.Room
