from .base import *
from corsheaders.defaults import default_headers
from os import environ
import dj_database_url as heroku_postgres

SECRET_KEY = environ.get("SECRET_KEY")
API_TOKEN = environ.get("API_TOKEN")
DEBUG = environ.get("DEBUG", "False").lower() in ("true", "t", "+", "on", "yes", "y")
REDIS_URL = environ.get("REDIS_URL")

ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': 
        heroku_postgres.config(
            engine='django.db.backends.postgresql_psycopg2',
            default=environ.get("DATABASE_URL"),
            conn_max_age=None
        )
}

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Kaliningrad'

CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = REDIS_URL

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],
        },
    }
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    'Access-Control-Allow-Headers',
    'Access-Control-Allow-Credentials',
    'Access-Token',
    'access-token'
]

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