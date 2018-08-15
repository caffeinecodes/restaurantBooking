"""
Django settings for TextNook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fuk+aeooc4!ea62^0gaeu$zrxb9r&sgr5hf3+p^(q-s$w@1o3s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djrill',
    'rest_framework',
    'app.accounts',
    'app.dishes',
    # 'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT':
    'json',
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer', ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )
}

JWT_AUTH = {'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14)}
JWT_ALLOW_REFRESH = True
# Social Auth

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',
    # 'social.apps.django_app.context_processors.backends',
    # 'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    # 'social.backends.facebook.FacebookOAuth2',
    # 'social.backends.google.GooglePlusAuth',
    # 'social.backends.google.GoogleOAuth2',
    # 'social.backends.google.GoogleOAuth',
    'django.contrib.auth.backends.ModelBackend', )

SOCIAL_AUTH_PIPELINE = (
    # 'social.pipeline.social_auth.social_details',
    # 'social.pipeline.social_auth.social_uid',
    # 'social.pipeline.social_auth.auth_allowed',
    # 'social.pipeline.social_auth.social_user',
    # 'social.pipeline.user.get_username',
    # 'social.pipeline.mail.mail_validation',
    # 'social.pipeline.user.create_user',
    # 'social.pipeline.social_auth.associate_user',
    # 'social.pipeline.social_auth.load_extra_data',
    # 'social.pipeline.user.user_details',
    # 'app.accounts.pipeline.get_avatar',
)

LOGIN_URL = '/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
#  672667412754-c1t89acf0k86lrbb50u3hmlkagbtbf7s.apps.googleusercontent.com
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '672667412754-c1t89acf0k86lrbb50u3hmlkagbtbf7s.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'dnzUBCq_qXEHXORoPNWcvqm7'

SOCIAL_AUTH_FACEBOOK_KEY = '511214295706675'
SOCIAL_AUTH_FACEBOOK_SECRET = 'acbc2f64d1cc7ab6c28510cd36025b7e'

SOCIAL_AUTH_USER_MODEL = 'accounts.Account'

AUTH_USER_MODEL = 'accounts.Account'

ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'

MANDRILL_API_KEY = 'rPlJL4lSZFNqDk9RgeZqQA'

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'commonproj',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'yourdatabasename.db'),
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    # How to format the output
    'formatters': {
        'standard': {
            'format':
            "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt':
            "%d/%b/%Y %H:%M:%S"
        },
    },

    # Log handlers (where to go)
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_ROOT + "/log/debug.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },

    # Loggers (where does the log come from)
    'loggers': {
        'debug': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console', 'logfile'],
            'level': 'WARN',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'gunicorn.error': {
            'level': 'INFO',
            'handlers': ['logfile'],
            'propagate': True,
        },
        'gunicorn.access': {
            'level': 'INFO',
            'handlers': ['logfile'],
            'propagate': False,
        },
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'), )
print(STATIC_ROOT)