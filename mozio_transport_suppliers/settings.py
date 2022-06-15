import os
import environ
from datetime import timedelta
from pathlib import Path
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Environment variables
env = environ.Env(
    ON_SERVER=(bool, True), LOGGING_LEVEL=(str, "INFO"), DEBUG=(bool, False)
)
IGNORE_DOT_ENV_FILE = env.bool("IGNORE_DOT_ENV_FILE", default=False)
if not IGNORE_DOT_ENV_FILE:
    # reading .env file
    environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
ON_SERVER = env("ON_SERVER", default=True)

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_CREDENTIALS = True
if ON_SERVER:
    CORS_ORIGIN_REGEX_WHITELIST = env.list("CORS_ORIGIN_REGEX_WHITELIST", default=[])
else:
    CORS_ORIGIN_ALLOW_ALL = True


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    
    ##### Third party apps
    "axes",  # Keep track of login attempts
    "rest_framework",  # RESTful APIs
    "rest_framework.authtoken",
    "corsheaders",  # Allow cross-origin requests
    "drf_yasg",  # Api documentation
    "phone_field", # Handle phone numbers password_validation
    
    ### - Authentication
    # All-in-one authentication
    "dj_rest_auth",  # API endpoints for RESTful authentication
    "allauth",  # Social authentication
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    "dj_rest_auth.registration",  # API endpoints for RESTful registration
    "guardian",  # Permissions
    
    ### Local apps
    "mozio_transport_suppliers.users" # User management
    
]


AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesBackend",
    # Django ModelBackend is the default authentication backend.
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
]


SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}


# we are turning off email verification for now
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False

SITE_ID = 1  # https://stackoverflow.com/questions/25468676/django-sites-model-what-is-and-why-is-site-id-1
REST_USE_JWT = True  # Use JWT for authentication

JWT_AUTH_COOKIE = "auth-access-token"
JWT_AUTH_REFRESH_COOKIE = "auth-refresh-token"
# JWT_AUTH_SAMESITE = "none"


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # For loading static files in production
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.
    "axes.middleware.AxesMiddleware",
]

ROOT_URLCONF = "mozio_transport_suppliers.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mozio_transport_suppliers.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# https://github.com/kennethreitz/dj-database-url
DATABASES = {
    "default": dj_database_url.config(default=env("DATABASE_URL"), conn_max_age=600)
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = "Africa/Dar_es_Salaam"


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "mozio_transport_suppliers/static"),
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# TODO: Change accesstokentime this when we are ready to deploy
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "USER_ID_FIELD": "id",  # for the custom user model
    "USER_ID_CLAIM": "user_id",
    "SIGNING_KEY": env("JWT_SECRET_KEY"),
}


# custom user model which the official Django documentation “highly recommends.”
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
AUTH_USER_MODEL = "users.CustomUser"


REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "mozio_transport_suppliers.users.serializers.CustomUserSerializer",
    "PASSWORD_RESET_SERIALIZER": "mozio_transport_suppliers.users.serializers.CustomPasswordResetSerializer",
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "mozio_transport_suppliers.users.serializers.UserRegisterSerializer"
}

# Set up the rest framework authentication middleware classes
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        # 'rest_framework.authentication.SessionAuthentication',
        "rest_framework.authentication.TokenAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 10,
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/hour", "user": "1000/hour"},
}

# EMAIL CONFIGURATIONS SENDGRID
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")  # Exactly that.
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")  # 25 or 587 (for unencrypted/TLS connections).
EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-user-models
# https://oluchiorji.com/django-rest-framework-tutorial-user-authentication/
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
OLD_PASSWORD_FIELD_ENABLED = True


FRONTEND_URL = env("FRONTEND_URL")
LOGIN_URL = env("FRONTEND_URL") + "/login/"
REGISTER_URL = env("FRONTEND_URL") + "/register/"
ACCOUNT_EMAIL_CONFIRMATION_URL = env("FRONTEND_URL") + "/verify-email/{}"
ACCOUNT_PASSWORD_RESET_CONFIRM = env("FRONTEND_URL") + "/password-reset/confirm/"


AXES_FAILURE_LIMIT = 4
AXES_COOLOFF_TIME = timedelta(minutes=5)
