
=====
django-homeworking
=====

App for writing and handling homework sheets for students learning English.


1. Add "homeworking" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'homeworking',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^homeworking/', include('homeworking.urls')),

3. specify BASE_URL parameter in settings to be able to get full urls
for homework assignments

4. Run `python manage.py migrate` to create the homeworking models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a homeworking sheets (you'll need the Admin app enabled).
