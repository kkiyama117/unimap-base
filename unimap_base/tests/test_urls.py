import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from unimap_base.factories import RoomFactory

urls: str = 'unimap_base.urls'


@pytest.mark.django_db
class UnivUrlsTest(TestCase):
    @pytest.mark.django_db
    def test_valid(self):
        RoomFactory.create()
        urls = (reverse("university-list"),
                reverse("campus-list"),
                reverse("building-list"),
                reverse("room-list"),
                # geodjango と噛み合わない
                # reverse("university-detail", kwargs={"pk": "1"}),
                # reverse("campus-detail", kwargs={"pk": "1"}),
                # reverse("building-detail", kwargs={"pk": "1"}),
                # reverse("room-detail", kwargs={"pk": "1"})
                )
        for url in urls:
            response = self.client.get(url, format="json")
            assert response.status_code == status.HTTP_200_OK
