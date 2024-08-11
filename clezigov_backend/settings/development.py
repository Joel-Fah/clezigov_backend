import dj_database_url
from .settings import *

# Settings overrides for development environment

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-czs0j+t6t4=ddh$5#6dzo%**3-88z79^^ia$v&j#h(!@27hn+0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Add compression and caching support for whitenoise
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}