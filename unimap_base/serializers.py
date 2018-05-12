from rest_framework import serializers

from unimap_base.models import University, Campus, Building, Room


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ("id", "name", "slug", "location")


class CampusSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)

    class Meta:
        model = Campus
        fields = ('id', 'name', 'group', "location", "university")


class BuildingSerializer(serializers.ModelSerializer):
    campus = CampusSerializer(read_only=True)

    class Meta:
        model = Building
        fields = ('id', 'name', "location", "campus")


class RoomSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ("id", "name", "location", "floor", "building")
