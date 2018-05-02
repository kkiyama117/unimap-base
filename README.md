# unimap-base

## Quick start

1. Add "unimap-base" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'unimap-base',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('unimap/', include('unimap-base.urls')),

3. Run `python manage.py migrate` to create the unimap models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a unimap (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/unimap/ to participate in the unimap.
