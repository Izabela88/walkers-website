"""
Django settings for walkers project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("ENV") == "PRODUCTION":
    DEBUG = False
    X_FRAME_OPTIONS = "SAMEORIGIN"
    X_FRAME_OPTIONS = "ALLOW-FROM http://ami.responsivedesign.is"
else:
    DEBUG = True

ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = "walkers.urls"


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    # "allauth.socialaccount",
    # "allauth.socialaccount.providers.facebook",
    # "allauth.socialaccount.providers.google",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "phonenumber_field",
    "rest_framework",
    "home",
    "about",
    "walker_profile",
    "search",
    "reviews",
    "contact",
    "newsletter",
    "django_cleanup.apps.CleanupConfig",
]


SITE_ID = 2


# PHONE_NUBER FIELD
PHONENUMBER_DEFAULT_REGION = "GB"
PHONENUMBER_DEFAULT_FORMAT = "NATIONAL"


LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# ALLAUTH
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USER_MODEL_USERNAME_FIELD = None


# Forms
ACCOUNT_FORMS = {"signup": "walker_profile.forms.ExtendedSignupForm"}
# SOCIALACCOUNT_ADAPTER = "walkers.adapter.SocialAccountAdapter"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


# SOCIALACCOUNT_PROVIDERS = {
#     "facebook": {
#         "METHOD": "js_sdk",
#         "SCOPE": ["email", "public_profile"],
#         "AUTH_PARAMS": {"auth_type": "reauthenticate"},
#         "INIT_PARAMS": {"cookie": True},
#         "FIELDS": [
#             "id",
#             "first_name",
#             "last_name",
#             "middle_name",
#             "name",
#             "name_format",
#             "email",
#         ],
#         "EXCHANGE_TOKEN": True,
#         "LOCALE_FUNC": lambda request: "en_US",
#         "VERIFIED_EMAIL": False,
#         "VERSION": "v13.0",
#     },
#     "google": {
#         "SCOPE": [
#             "profile",
#             "email",
#             "openid",
#         ],
#         "AUTH_PARAMS": {
#             "access_type": "online",
#             "response_type": "code",
#         },
#     },
# }


# MAILCHIMP CREDENTIALS
MAILCHIMP_API_KEY = os.environ.get("MAILCHIMP_API_KEY")
MAILCHIMP_DATA_CENTER = os.environ.get("MAILCHIMP_DATA_CENTER")
MAILCHIMP_EMAIL_LIST_ID = os.environ.get("MAILCHIMP_EMAIL_LIST_ID")


# EMAIL
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = os.environ.get("EMAIL")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "walkers.context_processors.global_variables",
            ],
        },
    },
]


WSGI_APPLICATION = "walkers.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# if os.getenv("ENV") == "PRODUCTION":
DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
# else:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": BASE_DIR / "db.sqlite3",
#         }
#     }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation." "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


STATIC_URL = "/static/"
STATICFILES_STORAGE = (
    "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "walker_profile.WalkerUser"

SILENCED_SYSTEM_CHECKS = ["auth.W004"]

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

BASE_COUNTRY = "UK"
