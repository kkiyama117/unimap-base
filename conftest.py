"""Pytest のフック
"""
import subprocess
import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        item.keywords['django_db'] = pytest.mark.django_db


def pytest_unconfigure(config):
    """pytest の実行時に一度だけ実行される

    """
    subprocess.run(['python', '-Wd', 'manage.py', 'check'], shell=True)
    print("manage.py check done")
