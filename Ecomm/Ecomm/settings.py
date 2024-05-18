"""
Django settings for Ecomm project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'ecomApp', 'staticfiles')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%lv*y_$*4n9v#m(#ggyvw*6hx%z*35bugvs4srd2k4ps0tezf('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition
import djongo

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecomApp',
    'backendlogin',
    'djongo',
    'registration',
    'rest_framework_api_key',
    'django_otp',
    'menu_management',
    'advertisement_management',
    'order',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'jazzmin',
    'banner_management',
    'cart',
    'walet',
    'report',
    'notification',
    'chart'



]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
AUTH_USER_MODEL = 'ecomApp.CustomUser'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
}


MIDDLEWARE = [
    'backendlogin.middleware.RevalidateBackHistoryMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

]

ROOT_URLCONF = 'Ecomm.urls'
CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Ecomm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'frozenwaladb',
#         'USER': 'Frozenwala',
#         'PASSWORD': 'Frozenwala_007',
#         'HOST': 'frozenwaladb.cpowoy2cei6a.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
import djongo

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'test_mongo',  # Specify your database name
#     }
# }
# the real databse one
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'testdb2',
#         'ENFORCE_SCHEMA': False,  # Enforce schema validation
#         'CLIENT': {
#             'host': 'mongodb+srv://user:user@cluster0.prxlwvh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
#             'port': 27017,  # Default MongoDB port
#             'username': 'user',
#             'password': 'user'
#
#         },
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'testdb1',
#         'ENFORCE_SCHEMA': False,  # Enforce schema validation
#         'CLIENT': {
#             'host': 'mongodb+srv://user:user@cluster0.a7xiyou.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
#             'port': 27017,  # Default MongoDB port
#             'username': 'user',
#             'password': 'user',
#             'ssl': False,
#             # 'connectTimeoutMS': 5000,  # 5 seconds timeout
#             # 'socketTimeoutMS': 5000,  # 1 minute timeout
#
#         },
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = 'static'
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ALLOWED_HOSTS = ['*']
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,'staticfiles'),
#     # Add other directories if needed
# ]
#
# # Define the directory where Django will collect static files for deployment
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# #216 219 212 database 221
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'mithai01234@gmail.com'
# EMAIL_HOST_PASSWORD = 'ubpz dnre zoen rkuq'
#
# RAZORPAY_API_KEY="rzp_test_enEwAJBwuY35MP"
# RAZORPAY_SECRET_KEY="GDMhskdQyL9mC1OohkGJAoKC"
# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ALLOWED_HOSTS = ['*']
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,'static'),
#     # Add other directories if needed
# ]

# Define the directory where Django will collect static files for deployment
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
#216 219 212 database 221
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mithai01234@gmail.com'
EMAIL_HOST_PASSWORD = 'ubpz dnre zoen rkuq'

RAZORPAY_API_KEY="rzp_test_enEwAJBwuY35MP"
RAZORPAY_SECRET_KEY="GDMhskdQyL9mC1OohkGJAoKC"


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#




STATIC_URL = 'staticfiles/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')