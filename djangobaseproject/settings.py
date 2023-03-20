"""
Django settings for djangobaseproject project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
SHARED_URL = "https://shared.acdh.oeaw.ac.at/"
PROJECT_NAME = "fwm"


ACDH_IMPRINT_URL = (
    "https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID="
)
REDMINE_ID = 10459

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "vxAeLYeo")

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("DEBUG"):
    DEBUG = True
else:
    DEBUG = False
ADD_ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "*")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_celery_results",
    "django_filters",
    "django_tables2",
    "dal_select2",
    "dal",
    "leaflet",
    "mptt",
    "webpage",
    "browsing",
    "infos",
    "vocabs",
    "django_spaghetti",
    "appcreator",
    "archiv",
    "netvis",
    "django_extensions",
    "zotero_ac",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
SPAGHETTI_SAUCE = {
    "apps": [
        "archiv",
    ],
    "show_fields": False,
    "exclude": {"auth": ["user"]},
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "djangobaseproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "webpage.webpage_content_processors.installed_apps",
                "webpage.webpage_content_processors.is_dev_version",
                "webpage.webpage_content_processors.get_db_name",
                "webpage.webpage_content_processors.shared_url",
                "webpage.webpage_content_processors.my_app_name",
            ],
        },
    },
]

WSGI_APPLICATION = "djangobaseproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.environ.get("POSTGRES_DB", "fwm"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SHEET_ID = os.environ.get("SHEET_ID", "1C1nS4pPyqSouyfcfRZuXX7DGRGaRcg-NqtK2ioNJ63Y")


# vocabs specific settings

VOCABS_DEFAULT_LANG = "en"
VOCABS_LISTVIEW_PAGESIZE = 50
SPAGHETTI_SAUCE = {
    "apps": ["vocabs", "infos", "archiv", "zotero_ac"],
    "show_fields": False,
}

ZOTERO_URL = "https://api.zotero.org/groups/2745880/items"

CELERY_RESULT_BACKEND = "django-db"
CELERY_BROKER_URL = os.environ.get("amqp://")
CELERY_TASK_TRACK_STARTED = True
