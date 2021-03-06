"""
Django settings for project project.

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
SECRET_KEY = 'u-ftea0f8cn2jmroyaw7kx$*3u+aum$=4i7zbr!(kjra_y)o&='

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
	'project.apps.homepage',
	'project.apps.data',
	'project.uauth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT=""
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT=SITE_ROOT
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)
TEMPLATE_CONTEXT_PROCESSOR = (
	'django.contrib.auth.context_processor.auth',
	'django.core.context_processor.media',
	'django.core.context_processors.csrf',
)
'''TEMPLATE_LOADERS = (
	'django.template.loaders.app_directories.loader',
	)'''
TEMPLATE_DIRS=(
	os.path.join(os.path.dirname(__file__),'templates'),
	os.path.join(os.path.dirname(__file__),'templates/auth'),
	)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tysemminiproject@gmail.com'
EMAIL_HOST_PASSWORD = 'jp5project'
EMAIL_PORT = 587


AUTH_PROFILE_MODULE='project.data.MyUser'

LOGIN_URL='/login/'

LOGIN_REDIRECT_PROFILE='/home'


SESSION_EXPIRE_AT_BROWSER_CLOSE=True