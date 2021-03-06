"""Pytest のフック
"""
import subprocess

import django_webtest
import pytest
from django_webtest import WebTestMixin


def pytest_collection_modifyitems(items):
    for item in items:
        item.keywords['django_db'] = pytest.mark.django_db


def pytest_unconfigure(config):
    """pytest の実行時に一度だけ実行される

    """
    subprocess.run(['python', '-Wd', 'manage.py', 'check'], shell=True)
    print("manage.py check done")


@pytest.fixture(scope='function', autouse=True)
def app(request):
    wtm = django_webtest.WebTestMixin()
    wtm._patch_settings()
    request.addfinalizer(wtm._unpatch_settings)
    return django_webtest.DjangoTestApp()
