from pathlib import Path
from os.path import join
from os import environ

BASE_DIR = Path(__file__).resolve().parent.parent


try:
    SECRET_KEY = environ['SECRET_KEY']
    API_TOKEN = environ['API_TOKEN']
    DEBUG = bool(int(environ['DEBUG']))
except KeyError:
    SECRET_KEY = 'django-insecure-y*j_0z96$b5sdyj)e_2v(*4%)ja)$&jw)=3g-8q3c3_=q=xq_a'
    API_TOKEN = 'dDha03LqkyCYI6NyRZysPXukX'
    DEBUG = True

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'common.apps.CommonConfig',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

WSGI_APPLICATION = 'Astromodel.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

CORS_ALLOW_HEADERS = (
    'Access-Control-Allow-Headers',
    'Access-Control-Allow-Credentials',
)

CORS_ALLOW_ALL_ORIGINS = True
