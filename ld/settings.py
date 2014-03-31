"""
Django settings for ld project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$d!vwst%d)qq&re3d5(35z9x)d9p9xu2^8xccjn_d%!@_h^&se'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ld.urls'

WSGI_APPLICATION = 'ld.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_URL = '/static/'
MEDIA_URL = '/upload/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/"),
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'lushizhao'
EMAIL_HOST_PASSWORD = 'lushizhao1129'
DEFAULT_FROM_EMAIL = 'i@lushizhao.me'
SERVER_EMAIL = 'i@lushizhao.me'

QINIU_ACCESS_KEY='8UYiGo3ZTdwkSD6QWXsvysWy79OmtbJ2-I2AuAa_'
QINIU_SECRET_KEY='f8xbN8LewTLJx1ZMfC0n5uLa_6zuD-OXoDhwv_Vg'
QINIU_BUCKET_NAME='longda'
QINIU_BUCKET_DOMAIN='longda.qiniudn.com'
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
STATICFILES_STORAGE  = 'qiniustorage.backends.QiniuStaticStorage'