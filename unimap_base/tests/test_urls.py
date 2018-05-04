import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from unimap_base.factories import UniversityFactory, RoomFactory


@pytest.mark.django_db
class UnivUrlsTest(TestCase):
    @pytest.mark.django_db
    def test_valid(self):
        room = RoomFactory()
        room.save()
        urls = (reverse("university-list"),
                reverse("campus-list"),
                reverse("building-list"),
                reverse("room-list"),
                reverse("university-detail", kwargs={"pk": "1"}),
                reverse("campus-detail", kwargs={"pk": "1"}),
                reverse("building-detail", kwargs={"pk": "1"}),
                reverse("room-detail", kwargs={"pk": "1"}))
        for url in urls:
            response = self.client.get(url, format="json")
            assert response.status_code == status.HTTP_200_OK
