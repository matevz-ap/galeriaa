from .base import *

# Topical Index
# https://docs.djangoproject.com/en/4.2/ref/settings/#core-settings-topical-index

# Core Settings
# https://docs.djangoproject.com/en/4.2/ref/settings/#core-settings

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=[
        ".localhost",
        "127.0.0",
        "::1",
    ],
)

INSTALLED_APPS += [
    # django-extensions
    # https://django-extensions.readthedocs.io/en/latest/
    "django_extensions",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#database

DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:///local.db"),
}

# Debugging
# https://docs.djangoproject.com/en/4.2/ref/settings/#debugging

DEBUG = env.bool("DEBUG", default=True)

# Security
# https://docs.djangoproject.com/en/4.2/ref/settings/#security

SECRET_KEY = env.str("SECRET_KEY", default="krnv9x3xcr3e573cp1gr3437w6")
