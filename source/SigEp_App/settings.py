import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

with open('config.json') as json_file:
    config = json.load(json_file)

# Check and see what state the machine is in
# and set the settings to that machine
if config['state'] == 'dev':
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
else:
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = config['secret_key']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['database_name'],
        'USER': config['database_user'],
        'PASSWORD': config['database_password'],
        'HOST': config['database_host'],
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'home',
    'accounts',
    'fines',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SigEp_App.urls'

WSGI_APPLICATION = 'SigEp_App.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Kentucky/Louisville'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_URL = '/static/'

STATIC_ROOT = '/www/SigEp_App/'

AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = '/accounts/login/'
