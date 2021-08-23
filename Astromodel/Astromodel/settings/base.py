from pathlib import Path
from os.path import join

DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'api.apps.ApiConfig',
    'common.apps.CommonConfig',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'channels_redis',
    'django_celery_beat',
    'django_celery_results'
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Astromodel.urls'

ASGI_APPLICATION = "Astromodel.asgi.application"
WSGI_APPLICATION = 'Astromodel.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


USE_I18N = True
USE_L10N = True
USE_TZ = True


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = join(BASE_DIR, 'files', 'media')
MEDIA_URL = '/media/'
