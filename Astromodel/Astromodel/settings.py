from pathlib import Path
from os.path import join
from os import environ
from corsheaders.defaults import default_headers

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = environ.get("SECRET_KEY", "lYeOe7oHmDTlEnue3HA7DrKXpn4hm9y8xuAkyiLkmDxdZUB1tqTB74oqodrSpY0ed")
API_TOKEN = environ.get("API_TOKEN", "dDha03LqkyCYI6NyRZysPXukX")
DEBUG = environ.get("DEBUG", "False").lower() in ("1", "true", "t", "yes", "y", "+", "ohhhh yeah!!!")


ALLOWED_HOSTS = ['*', ]

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


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


ASGI_APPLICATION = "Astromodel.asgi.application"
WSGI_APPLICATION = 'Astromodel.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': environ.get('DATABASE_HOST', "postgres"),
        'NAME': environ.get('DATABASE_NAME'),
        'USER': environ.get('DATABASE_USER'),
        'PASSWORD': environ.get('DATABASE_PASSWORD'),
        'PORT': int(environ.get('DATABASE_PORT', 5432)),
    }
}

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


LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Kaliningrad'

USE_I18N = True
USE_L10N = True
USE_TZ = True


CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = environ.get("REDIS_URL", "redis://localhost:6379/0")


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = join(BASE_DIR, 'files', 'media')
MEDIA_URL = '/media/'


CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    'Access-Control-Allow-Headers',
    'Access-Control-Allow-Credentials',
    'Access-Token',
    'access-token'
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [environ.get("REDIS_URL", "redis://localhost:6379/0")],
        },
    }
}