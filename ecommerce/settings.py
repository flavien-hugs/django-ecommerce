"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import braintree
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^)c9&3f@b6wlc(e_6-c4cqo*@#$9fmvq)k)(7oajatasoz%%%m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEFAULT_FROM_EMAIL = 'flavienhgs@gmail.com'
ALLOWED_HOSTS = []

SITE_NAME = 'unsta'
META_KEYWORDS = 'Shopping, ecommerce, accessories, TV, Audio, smartphone, Mode'
META_DESCRIPTION = 'ecommerce shopping'

DEFAULT_CHARSET = 'utf-8'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = False
USE_X_FORWARRED_HOST = True

# Cookie name. This can be whatever you want.
SESSION_COOKIE_NAME = 'sessionid'
# The module to store sessions data.
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
# Whether a user's session cookie expires when the Web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# Whether the session cookie should be secure (https:// only).
SESSION_COOKIE_SECURE = False

# Application definition

INSTALLED_APPS = [
    # ajout application de coupons
    'accounts.apps.AccountsConfig',
    'django.contrib.sitemaps',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.redirects',

    # ajout application shop
    'shop.apps.ShopConfig',

    # ajout application panier
    'panier.apps.PanierConfig',

    # ajout commandes des clients
    'commandes.apps.CommandesConfig',

    # ajout application de paiement
    'payment.apps.PaymentConfig',

    # ajout application de coupons
    'coupons.apps.CouponsConfig',

    # ajout tinymce
    'tinymce',

    # ajout xadmin et crispy_forms

    # ajout application de rosetta translate interface
    'rosetta',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.contrib.messages.context_processors.messages',
                # ...
                # Processeur de contexte du panier
                'panier.context_processors.panier',
                'panier.context_processors.get_client_ip',
                'panier.context_processors.ecommerce',
            ],
        },
    },
]

BREADCRUMBS_HOME_LABEL = 'Home'

WSGI_APPLICATION = 'ecommerce.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# argon2
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/db_ecommerce.conf',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Configuration de redis : plugins pour proposer des articles similaires
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# Traduction du contenu
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('Francais')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/')
]

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# formatage des nombres avec les séparateurs de milliers
USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    'static/'
]

LOGIN_URL = _('/accounts/login/')
LOGIN_REDIRECT_URL = _('/profile/')

# Configuration des sessions
PANIER_SESSION_ID = 'cart'

# Configuration de l'API braintree
# https://www.braintreepayments.com/sandbox


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment=braintree.Environment.Sandbox,
        merchant_id='y5jkkwv943v76c9q',
        public_key='gmrrt6d9qggcjw2r',
        private_key='c70db4ac0b03d4df804b676ba19807a9'
    )
)
