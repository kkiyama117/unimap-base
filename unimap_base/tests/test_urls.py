import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from unimap_base.factories import UniversityFactory


@pytest.mark.django_db
class UnivUrlsTest(TestCase):
    @pytest.mark.django_db
    def test_valid(self):
        university = UniversityFactory()
        university.save()
        urls = (reverse("university-list"),
                reverse("university-detail", kwargs={"pk": "1"}))
        for url in urls:
            response = self.client.get(url, format="json")
            assert response.status_code == status.HTTP_200_OK
