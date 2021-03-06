import pytest
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError

from unimap_base.factories import RoomFactory
from unimap_base.models import University, Room


class UniversityTest:

    @pytest.mark.parametrize(('name', 'slug'), [
        ('京都大学', "KU"),
        ('東京大学', "UT")
    ])
    @pytest.mark.django_db
    def test_create_instance(self, name, slug):
        univ = University(id=1, name=name, slug=slug)
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
        univ = University(id=1, name=name, slug=slug)
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
