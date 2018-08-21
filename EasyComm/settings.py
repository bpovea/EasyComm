"""
Django settings for EasyComm project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import oscar

from oscar.defaults import *

from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hhycci%g2a#11-!eelp@*6b*4a$b@%a1dv3!$@f1lae!%1j(r$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'compressor',
    'rest_framework',
    'widget_tweaks',
    'EasyComm_apps.help',
    "EasyCommAPI",
    'django_seed',
    'corsheaders',
    #'reportesMongo',
] + get_core_apps([
    'EasyComm_apps.order',
    'EasyComm_apps.address',
    'EasyComm_apps.catalogue',
    'EasyComm_apps.customer',
    # dashboard applications
    'EasyComm_apps.dashboard',
    'EasyComm_apps.dashboard.reports',
    'EasyComm_apps.customer',
    'EasyComm_apps.checkout',
    ])

SITE_ID = 1

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    '127.0.0.1:8000',
)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

]

ROOT_URLCONF = 'EasyComm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            oscar.OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'EasyComm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
        'mongo_db': {
        'ENGINE': 'djongo',
        'NAME': 'proyectoDAW',
    },
}
DATABASE_ROUTERS = ['reportesMongo.routers.ReportesRouter',]

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/apps')
MEDIA_URL = '/static/apps/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_SHOP_NAME = 'EasyComm'
OSCAR_SHOP_TAGLINE = ''

OSCAR_DEFAULT_CURRENCY = '$'
OSCAR_CURRENCY_FORMAT='$'

#default oscar navegation bar
"""
OSCAR_DASHBOARD_NAVIGATION = [
    {
        'icon': 'icon-th-list', 
        'label': 'Dashboard', 
        'url_name': 'dashboard:index'
    },
    {
        'icon': 'icon-sitemap', 
        'label': 'Catalogue', 
        'children': [
            {'label': 'Products', 'url_name': 'dashboard:catalogue-product-list'}, 
            {'label': 'Product Types', 'url_name': 'dashboard:catalogue-class-list'}, 
            {'label': 'Categories', 'url_name': 'dashboard:catalogue-category-list'}, 
            {'label': 'Ranges', 'url_name': 'dashboard:range-list'}, 
            {'label': 'Low stock alerts', 'url_name': 'dashboard:stock-alert-list'}
        ]
    }, 
    {
        'icon': 'icon-shopping-cart', 
        'label': 'Fulfilment', 
        'children': [
            {'label': 'Orders', 'url_name': 'dashboard:order-list'}, 
            {'label': 'Statistics', 'url_name': 'dashboard:order-stats'}, 
            {'label': 'Partners', 'url_name': 'dashboard:partner-list'}
        ]
    }, 
    {
        'icon': 'icon-group', 
        'label': 'Customers', 
        'children': [
            {'label': 'Customers', 'url_name': 'dashboard:users-index'}, 
            {'label': 'Stock alert requests', 'url_name': 'dashboard:user-alert-list'}
        ]
    }, 
    {
        'icon': 'icon-bullhorn', 
        'label': 'Offers', 
        'children': [
            {'label': 'Offers', 'url_name': 'dashboard:offer-list'}, 
            {'label': 'Vouchers', 'url_name': 'dashboard:voucher-list'}, 
            {'label': 'Voucher Sets', 'url_name': 'dashboard:voucher-set-list'}
        ]
    }, 
    {
        'icon': 'icon-folder-close', 
        'label': 'Content', 
        'children': [
            {'label': 'Content blocks', 'url_name': 'dashboard:promotion-list'}, 
            {'label': 'Content blocksby page', 'url_name': 'dashboard:promotion-list-by-page'}, 
            {'label': 'Pages', 'url_name': 'dashboard:page-list'}, 
            {'label': 'Email templates', 'url_name': 'dashboard:comms-list'}, 
            {'label': 'Reviews', 'url_name': 'dashboard:reviews-list'}
        ]
    }, 
    {
        'icon': 'icon-bar-chart', 
        'label': 'Reports', 'url_name': 'dashboard:reports-index'
    }
]
"""

OSCAR_DASHBOARD_NAVIGATION += [
    {
        'icon': 'icon-question',
        'label': 'Help',
        'children': [
            {
                'label': 'Faq',
                'url_name': 'dashboard:faq-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
         ]
    },
]


# import local-settings

try:
    from .local_settings import *
except ImportError:
    pass
