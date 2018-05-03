from django.urls import path, include
from rest_framework import routers

from unimap_base.api import UniversityViewSet, CampusViewSet, BuildingViewSet, \
    RoomViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'universities', UniversityViewSet, base_name="university")
router.register(r'campuses', CampusViewSet, base_name="campus")
router.register(r'buildings', BuildingViewSet, base_name="building")
router.register(r'rooms', RoomViewSet, base_name="room")

urlpatterns = [
    path('', views.index, name='index'),
    path("api/", include(router.urls))
]
