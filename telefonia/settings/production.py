from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSS = []

# MIDDLEWARE_CLASSES += ('apps.Accounts.middleware.IpAccessMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbtarifacion   ',
        'HOST': '127.0.0.1',
        'USER': 'postgres',
        'PASSWORD': 'sistemas',
        'PORT': 5432,
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)
