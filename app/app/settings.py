"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['APP_SECRET_KEY'] 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
		'/home/vrootic/myproject/app/templates/'
        ],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }        
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
	'console': {
	    'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
	},
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
	    'formatter': 'console',
        },
    },
    'loggers': {
    	'': {
    	    'handlers': ['console'],
    	    'level': 'WARNING',
    	},
	#'django': {
        #    'handlers': ['console'],
        #    'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        #    'propagate': False,
        #},
    }
}

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'formatters': {
#        'normal': {
#            'format': '[%(levelname)s] %(asctime)s | %(name)s:%(lineno)d | %(message)s'
#        },
#        'simple': {
#            'format': '[%(levelname)s] %(message)s'
#        },
#    },
#    # 'filters': {
#    #     'require_debug_true': {
#    #         '()': 'django.utils.log.RequireDebugTrue',
#    #     },
#    # },
#    'handlers': {
#        'console': {
#            'class': 'logging.StreamHandler',  # Default logs to stderr
#            'formatter': 'normal',  # use the above "normal" formatter
#            # 'filters': ['require_debug_true'],  # add filters
#        },
#    },
#    'loggers': {
#        '': {  # means "root logger"
#            'handlers': ['console'],  # use the above "console" handler
#            'level': 'INFO',  # logging level
#        },
#        'some_app.some_module': {  # Modify logger in some modules
#            'handlers': ['console'],
#            'level': 'DEBUG',
#            'propagate': True, 
#        },
#    },
#}
