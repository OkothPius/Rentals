import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

 # reading .env file
env = environ.Env()
environ.Env.read_env()


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = 'SECRET_KEY'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrap_datepicker_plus",
    "backend.apps.accounts",
    "backend.apps.core",
    "backend.apps.invoice",
    "crispy_forms",
    "social_django",
    "bulma",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "backend.urls"

INTERNAL_IPS = ["127.0.0.1"]

# ==============================================================================
# AUTHENTICATION_BACKENDS
# ==============================================================================
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)


WSGI_APPLICATION = "backend.wsgi.application"


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <-
            ],
        },
    },
]


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

# LANGUAGE_CODE = env("LANGUAGE_CODE", default="en-us")
LANGUAGE_CODE = "en-us"


# TIME_ZONE = env("TIME_ZONE", default="UTC")
TIME_ZONE = "UTC"


USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

THOUSAND_SEPARATOR=','

DECIMAL_SEPARATOR='.'

NUMBER_GROUPING=3

LOCALE_PATHS = [BASE_DIR / "locale"]


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = "/static/"

# STATIC_ROOT = BASE_DIR.parent.parent / "static"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [BASE_DIR / "static"]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = "/media/"

# MEDIA_ROOT = BASE_DIR.parent.parent / "media"


# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================
# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'

SOCIAL_AUTH_GITHUB_KEY = '3021786cc75de7b2eb75'
SOCIAL_AUTH_GITHUB_SECRET = '36390c9b438fd5d7134c4bd8b0593035a68455f7'
AUTH_USER_MODEL = 'accounts.User'

# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

BACKEND_ENVIRONMENT = env("BACKEND_ENVIRONMENT", default="local")
