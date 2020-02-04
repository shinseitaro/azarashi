from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']

# Application definition

INSTALLED_APPS += [
]

MIDDLEWARE += [
]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
        }
}

EMAIL_USE_SSL = True
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = os.environ['EMAIL_PORT']
DEFAULT_FROM_EMAIL = os.environ['FROM_EMAIL']

LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'filters': {
       'require_debug_false': {
           '()': 'django.utils.log.RequireDebugFalse',
       },
       'require_debug_true': {
           '()': 'django.utils.log.RequireDebugTrue',
       },
   },
   'formatters': {
       'django.server': {
           '()': 'django.utils.log.ServerFormatter',
           'format': '[%(server_time)s] %(message)s a',
       },
       'verbose': {
           'format': '%(levelname)s %(asctime)s %(module)s '
                     '%(process)d %(thread)d %(message)s'
       },
   },
   'handlers': {
       'file': {  # どこに出すかの設定に名前をつける `file`という名前をつけている
           'level': 'DEBUG',  # DEBUG以上のログを取り扱うという意味
           'class': 'logging.FileHandler',  # ログを出力するためのクラスを指定
           'filename': os.path.join(BASE_DIR, 'django.log'),  # どこに出すか
           'formatter': 'verbose',  # どの出力フォーマットで出すかを名前で指定
       },
       'console': {
           'level': 'INFO',
           'filters': ['require_debug_true'],
           'class': 'logging.StreamHandler',
           'formatter': 'verbose',
       },
       'django.server': {
           'level': 'INFO',
           'class': 'logging.StreamHandler',
           'formatter': 'django.server',
       },
       'mail_admins': {
           'level': 'ERROR',
           'filters': ['require_debug_false'],
           'class': 'django.utils.log.AdminEmailHandler'
       }
   },
   'loggers': {
       'django': {
           'handlers': ['console', 'file', 'mail_admins'],
           'level': 'INFO',
       },
       'django.server': {
           'handlers': ['django.server'],
           'level': 'INFO',
           'propagate': False,
       },
       #追加
       'azarashi': {
           'handlers': ['console', 'file'],
           'level': 'INFO',
           'propagate': False,
       },
   }
}
