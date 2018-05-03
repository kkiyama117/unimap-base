unimap-base
###########

 |circle| |coverage| |pyup| |pyup-python3|

.. class:: no-web no-pdf

Quick start
===========

1. Add "unimap-base" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'unimap_base',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('unimap/', include('unimap_base.urls')),

3. Run `python manage.py migrate` to create the unimap models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a unimap (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/unimap/ to participate in the unimap.

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
