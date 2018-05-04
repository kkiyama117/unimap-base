unimap-base
###########

 |circle| |coverage| |pyup| |pyup-python3| |code climate|

.. section-numbering::

Quick start
===========

1. Add "unimap-base" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = [
         ...
         'rest_framework',
         'unimap_base',
      ]

2. Include the polls URLconf in your project urls.py like this::

      path('unimap/', include('unimap_base.urls')),

3. Run `python manage.py migrate` to create the unimap models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a unimap (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/unimap/ to participate in the unimap.

Develop and Test
================

1. Download or clone this repo

2. Make virtual environment::

      python -m venv .venv
      source .venv/bin/activate

3. Install dependencies::

      pip install -r requirements.txt

4. Test::

      pytest

5. Develop
      If you want to know how to write code, but you're not familier with python, django, restframework or pytest, see

      * `python3 <https://www.python.org>`_
      * `django <https://docs.djangoproject.com/>`_
      * `Djangorestframework <http://www.django-rest-framework.org>`_
      * `pytest <https://docs.pytest.org/en/latest/>`_

Usage (it's alpha version so change suddenly and need to fix)
=============================================================

1. Create models needed to make API by django admin site

2. access to API
   <your site url>/<url for unimap_base>/api/



.. |circle| image:: https://circleci.com/gh/kkiyama117/unimap-base.svg?style=svg
    :target: https://circleci.com/gh/kkiyama117/unimap-base

.. |coverage| image:: https://codecov.io/gh/kkiyama117/unimap-base/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/kkiyama117/unimap-base

.. |pyup| image:: https://pyup.io/repos/github/kkiyama117/unimap-base/shield.svg
    :target: https://pyup.io/repos/github/kkiyama117/unimap-base/
    :alt: Updates

.. |pyup-python3| image:: https://pyup.io/repos/github/kkiyama117/unimap-base/python-3-shield.svg
    :target: https://pyup.io/repos/github/kkiyama117/unimap-base/
    :alt: Python 3

.. |code climate| image:: https://api.codeclimate.com/v1/badges/7aeba9eb7f370776b9d4/maintainability
   :target: https://codeclimate.com/github/kkiyama117/unimap-base/maintainability
   :alt: Maintainability
