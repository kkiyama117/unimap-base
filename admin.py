from django.contrib import admin

from .models import Room, Building, Campus, University


class UniversityAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Info", {'fields': ['name', "slug"]}),
        ('Location', {'fields': ['latitude', "longitude"]}),
    ]
    list_display = ('name', "latitude", "longitude")
    list_filter = ['name']


class CampusAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Info", {'fields': ['name', "group", "university"]}),
        ('Location', {'fields': ['latitude', "longitude"]}),
    ]
    list_display = ('name', "university", "latitude", "longitude")
    list_filter = ['name', "group"]


class BuildingAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Info", {'fields': ['name', "campus"]}),
        ('Location', {'fields': ['latitude', "longitude"]}),
    ]
    list_display = ('name', "campus", "latitude", "longitude")
    list_filter = ['name']


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Info", {'fields': ['name', "building", "floor"]}),
    ]
    list_display = ('name', "building", "floor")
    list_filter = ['name', "floor"]


admin.site.register(University, UniversityAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)
