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

# LOGGING = {
#     # バージョンは「1」固定
#     'version': 1,
#     # 既存のログ設定を無効化しない
#     'disable_existing_loggers': False,
#     # ログフォーマット
#     'formatters': {
#         # 本番用
#         'production': {
#             'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
#                       '%(pathname)s:%(lineno)d %(message)s'
#         },
#     },
#     # ハンドラ
#     'handlers': {
#         # ファイル出力用ハンドラ
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': '/var/log/{}/app.log'.format(PROJECT_NAME),
#             'formatter': 'production',
#         },
#     },
#     # ロガー
#     'loggers': {
#         # 自作アプリケーション全般のログを拾うロガー
#         '': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         # Django本体が出すログ全般を拾うロガー
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#     },
# }
