"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jv#20+0b6rufp6(ug6wz-vt0h28yw-x&qg$ab^g6dh6kn)6uy$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'submission.apps.SubmissionConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'dj_test',
        'OPTIONS': {
            # 'read_default_file': '~/.my.cnf_dj',
            'read_default_file': '~/.my.cnf',
            'read_default_group': 'clientdj',
        },
    }
}
if 'test' not in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dj_test',
            'OPTIONS': {
                # 'read_default_file': '~/.my.cnf_dj',
                'read_default_file': '~/.my.cnf',
                'read_default_group': 'clientdj',
            },
        },
        # 'vampsdev': {
        #     'NAME': 'test',
        #     'ENGINE': 'django.db.backends.mysql',
        #     'OPTIONS': {
        #         'read_default_file': '~/.my.cnf',
        #         'read_default_group': 'clientvampsdev',
        #     },
        # },
        'local_env454': {
            'NAME': 'test_env454',
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': '~/.my.cnf',
                'read_default_group': 'clienthome',
            },
        },
        'local_vamps': {
            'NAME': 'test_vamps',
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': '~/.my.cnf',
                'read_default_group': 'clienthome',
            },
        },
    }

# class submissionRouter(object): 
#     def db_for_read(self, model, **hints):
#         "Point all operations on submission models to 'test_env454'"
#         if model._meta.app_label == 'submission':
#             return 'test_env454'
#         # if model._meta.app_label == 'submission':
#         #     return 'test_env454'
#         return 'default'
# 
#     def db_for_write(self, model, **hints):
#         "Point all operations on submission models to 'test_env454'"
#         return 'default'
# 
#     def allow_relation(self, obj1, obj2, **hints):
#         db_list = ('test_env454', 'test_vamps')
#         if obj1._state.db in db_list and obj2._state.db in db_list:
#             return True
#         return None
# 
#         # "Allow any relation if a both models in submission app"
#         # if obj1._meta.app_label == 'submission' and obj2._meta.app_label == 'submission':
#         #     return True
#         # # Allow if neither is submission app
#         # elif 'submission' not in [obj1._meta.app_label, obj2._meta.app_label]: 
#         #     return True
#         # return False
# 
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         All non-auth models end up in this pool.
#         """
#         return False
# 
# 
#     def allow_syncdb(self, db, model):
#         if db == 'test_vamps' or db == 'test_env454' or model._meta.app_label == "submission":
#             return False # we're not using syncdb on our legacy database
#         else: # but all other models/databases are fine
#             return True

DATABASE_ROUTERS = ['submission.db_router.submissionRouter']

DATABASE_APPS_MAPPING = {'submission': 'local_env454'}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
