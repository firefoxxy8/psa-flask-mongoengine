Python-social-auth + MongoEngine + Flask-Security
-------------------------------------------------


In order to get this up running just follow these steps:

1. Copy ``example/local_settings.py.template`` as ``example/local_settings.py``
   and fill the application keys in it

2. Create a ``virtualenv`` or similar virtualzation environment

3. Install requirements with ``pip install requirements.txt``

4. Ensure that ``mongodb`` is accessible (modify ``example/settings.py`` to
   point to properly point to it)

5. Run the application with ``python manage.py runserver`` and test it in the
   browser.
