from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'telefonia',
        'HOST': '127.0.0.1',
        'USER': 'postgres',
        'PASSWORD': 'sistemaspg',
        'PORT': 5432,
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)
