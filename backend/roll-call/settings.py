import os.path
import environ
"""
Django settings for roll-call project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

EMAIL_HOST = env.str("EMAIL_HOST", default="localhost")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")
EMAIL_PORT = env.int("EMAIL_PORT", default=25)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
# False if not in os.environ because of casting above
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
USE_X_FORWARDED_HOST = True
# Application definition
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_DOMAIN = env.str("DEFAULT_DOMAIN", default="localhost")
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'django.contrib.sites',
    'allauth',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.nextcloud',
    'allauth.account',
    'simple_menu',
    'rest_framework',
    "corsheaders",
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rest_framework_simplejwt',
    'attendance',
    'debug_toolbar',
    'ajax_datatable',
    'dj_rest_auth',
    'rest_framework.authtoken',
    "django_htmx"

]

MEDIA_URL = env("MEDIA_ROOT", default="/media/")
MEDIA_ROOT = os.path.join(BASE_DIR, env('MEDIA_ROOT', default="media/"))
STATIC_URL = env('STATIC_URL', default='static/')
STATIC_ROOT = BASE_DIR / env('STATIC_ROOT', default='static')

SITE_ID = env.int("SITE_ID")
MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
]
SOCIALACCOUNT_PROVIDERS = {
    'nextcloud': {
        'SERVER': env('NEXTCLOUD_URL'),
    }
}
ROOT_URLCONF = 'roll-call.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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
URL_PREFIX = env.str('URL_PREFIX', default='backend')
WSGI_APPLICATION = 'roll-call.wsgi.application'
REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default':  env.db()
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/


LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
]

LANGUAGE_CODE = env('LANGUAGE_CODE', default='de')

TIME_ZONE = env('TIME_ZONE', default='UTC')

USE_I18N = env('USE_I18N ', default=True)

USE_TZ = env('USE_TZ', default=True)

INTERNAL_IPS = env.list("INTERNAL_IPS")




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = "index"
SPECTACULAR_SETTINGS = {
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'TITLE': 'Roll Call API',
    'DESCRIPTION': 'Attendance management',
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
CSRF_USE_SESSIONS = env('CSRF_USE_SESSIONS', default=True)
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")
CORS_ALLOWED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")
CORS_EXPOSE_HEADERS = env.list("CORS_EXPOSE_HEADERS", default=['Content-Type', 'X-CSRFToken'])

CORS_ALLOW_CREDENTIALS = env('CORS_ALLOW_CREDENTIALS', default=True)
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
}