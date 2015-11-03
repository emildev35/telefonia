from unipath import Path
import djcelery

# Celery settings
djcelery.setup_loader()
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '*aj=%r!v%q)sqe#e&(1wy)tkxh7s*#62)tzov#iiekl+a+8x1g'


DJANGO_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
OTHER_APPS = (
    'djcelery',
    'django_ajax',
    'widget_tweaks',
    'drealtime',
    'rest_framework',
)
LOCAL_APPS = (
    'apps.Home',
    'apps.Accounts',
    'apps.Llamadas',
    'apps.Reportes',
    'apps.Notificaciones',
    'apps.Personal',
)

INSTALLED_APPS = DJANGO_APPS + OTHER_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'drealtime.middleware.iShoutCookieMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'apps.Accounts.context_processors.menus',
            ],
        },
    },
]


ROOT_URLCONF = 'telefonia.urls'

WSGI_APPLICATION = 'telefonia.wsgi.application'

AUTH_USER_MODEL = 'Personal.Funcionario'

LANGUAGE_CODE = 'es-bo'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Cron Jobs

CRONJOBS = [
    ('* * * * *', 'apps.Reportes.cron.crear_cuentas'),
]
