# -*- coding: utf-8 -*-

import os.path
from base import *

# WEB SITE URL
THIS_BOOKTYPE_SERVER = os.environ['HTTP_HOST']
#BOOKTYPE_URL = ''
BOOKTYPE_URL = 'http://{}'.format(THIS_BOOKTYPE_SERVER)

STATIC_URL = '{}/static/'.format(BOOKTYPE_URL)
DATA_URL = '{}/data/'.format(BOOKTYPE_URL)
MEDIA_URL = DATA_URL

# URL where is publishing engine located. By default it is on local machine.
CONVERT_URL = BOOKTYPE_URL

# MPDF RENDERER SETTINGS
# Change lines below in case you want to use other version
# of php or mpdf in dev profile
MPDF_DIR = '/var/www/mpdf60/'
PHP_PATH = '/usr/bin/php'
MPDF_SCRIPT = '/usr/local/src/booktype/scripts/mpdf.php'

# DEBUG
DEBUG = TEMPLATE_DEBUG = False

# PROFILE
PROFILE_ACTIVE = 'prod'

# URL ROUTER
ROOT_URLCONF = '{}.urls.prod'.format(BOOKTYPE_SITE_DIR)

# REDIS
#REDIS_HOST = os.environ['REDIS_HOST']
#REDIS_PORT = 6379
#REDIS_DB = 0
#REDIS_PASSWORD = None

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['BOOKTYPE_DB'],
        'USER': os.environ['BOOKTYPE_USER'],
        'PASSWORD': os.environ['BOOKTYPE_PASS'],
        'HOST': os.environ['PG_HOST'],
        'PORT': os.environ['PG_PORT']
    }
}



# E-MAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# COMPRESSION
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s", # noqa
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BOOKTYPE_ROOT + "/logs/booktype.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'booktype': {
            'handlers': ['logfile'],
            'level': 'INFO'
        }
    }
}

# READ CONFIGURAION
from booktype.utils import config

try:
    BOOKTYPE_CONFIG = config.load_configuration()
except config.ConfigurationError:
    BOOKTYPE_CONFIG = {}
