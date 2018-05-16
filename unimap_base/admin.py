from django.contrib.gis import admin

from .models import Room, Building, Campus, University, Place, Border
from leaflet.admin import LeafletGeoAdmin


class PlaceAdmin(LeafletGeoAdmin):
    fieldsets = [
        ("Info", {'fields': ['name']}),
        ('Location', {'fields': ["location"]}),
    ]
    list_display = ('name', "location")
    list_filter = ['name']


class UniversityAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Info", {'fields': ['name', "slug"]}),
    ]
    list_display = ('name',)
    list_filter = ['name']


class CampusAdmin(LeafletGeoAdmin):
    fieldsets = [
        ("Info", {'fields': ['name', "group", "university"]}),
        ('Location', {'fields': ["border"]}),
    ]
    list_display = ('name', "university", "border")
    list_filter = ['name', "group"]


class BuildingAdmin(LeafletGeoAdmin):
    fieldsets = [
        ("Info", {'fields': ['name', "campus"]}),
        ('Location', {'fields': ['location']}),
    ]
    list_display = ('name', "campus", "location")
    list_filter = ['name']


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Info", {'fields': ['name', "building", "floor"]}),
    ]
    list_display = ('name', "building", "floor")
    list_filter = ['name', "floor"]


class BorderAdmin(LeafletGeoAdmin):
    search_fields = ['prefecture', 'major_city', 'city']
    list_filter = ('prefecture',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Border, BorderAdmin)
