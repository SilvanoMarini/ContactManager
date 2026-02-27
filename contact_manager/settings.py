"""
Django settings for contact_manager project.
Base configuration for production and development.
"""

import os
from pathlib import Path
import dj_database_url

# ==========================================================
# Base Directory
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================================
# Security Settings
# ==========================================================
# In production, values come from environment variables.
# In development, they will be overridden by local_settings.py.

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.onrender.com']


# ==========================================================
# Application Definition
# ==========================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps
    'contacts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise for static files in production
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'contact_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'base_templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'contact_manager.wsgi.application'


# ==========================================================
# Database Configuration
# ==========================================================
# - Local: SQLite
# - Production (Render): PostgreSQL via DATABASE_URL

DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# ==========================================================
# Password Validation
# ==========================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==========================================================
# Internationalization
# ==========================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# ==========================================================
# Static & Media Files
# ==========================================================
STATIC_URL = '/static/'

# Local static files (development)
STATICFILES_DIRS = [
    BASE_DIR / 'base_static'
]

# Collected static files (production)
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==========================================================
# Authentication Flow
# ==========================================================
LOGIN_URL = 'contacts:login'
LOGIN_REDIRECT_URL = 'contacts:index'
LOGOUT_REDIRECT_URL = 'contacts:login'


# ==========================================================
# Default Primary Key Field
# ==========================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==========================================================
# Local Development Override
# ==========================================================
# This file should NOT be committed to version control.
# Used only for local development settings.

try:
    from .local_settings import *
except ImportError:
    pass
