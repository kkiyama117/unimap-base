import pytest
from django.core.exceptions import ValidationError

from unimap_base.factories import RoomFactory
from unimap_base.models import University, Room, Location


class UniversityTest:

    @pytest.mark.parametrize(('name', 'slug'), [
        ('京都大学', "KU"),
        ('東京大学', "UT")
    ])
    @pytest.mark.django_db
    def test_create_instance(self, name, slug):
        location = Location(latitude=35.026304, longitude=135.780816)
        location.save()
        univ = University(id=1, name=name, slug=slug,
                          location=location)
        univ.save()
        assert univ.name == name
        assert univ.slug == slug
        assert str(univ) == name
        assert University.objects.count() == 1

    @pytest.mark.parametrize(('name', 'slug'), [
        ('京都大学', "KU"),
        ('東京大学', "UT")
    ])
    @pytest.mark.django_db
    def test_assertion(self, name, slug):
        location = Location(latitude=35.026304, longitude=135.780816)
        location.save()
        univ = University(id=1, name=name, slug=slug,
                          location=location)
        try:
            univ.full_clean()
        except ValidationError as e:
            pytest.fail()
            print(e)


class RoomTest:
    @pytest.mark.django_db
    def test_create_instance(self):
        room = RoomFactory()
        assert room.name == "Kyokita22"
        assert room.floor == 2
        assert str(room) == room.name
        assert Room.objects.count() == 1

    @pytest.mark.django_db
    def test_assertion(self):
        room = RoomFactory()
        try:
            room.full_clean()
        except ValidationError as e:
            pytest.fail()
            print(e)
