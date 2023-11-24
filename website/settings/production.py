from .base import *

# Topical Index
# https://docs.djangoproject.com/en/4.2/ref/settings/#core-settings-topical-index

# Core Settings
# https://docs.djangoproject.com/en/4.2/ref/settings/#core-settings

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=[
        env.str("RAILWAY_PUBLIC_DOMAIN"),
    ],
)

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#database

DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:///railway.db"),
}

# Debugging
# https://docs.djangoproject.com/en/4.2/ref/settings/#debugging

DEBUG = env.bool("DEBUG", default=False)

# HTTP
# https://docs.djangoproject.com/en/4.2/ref/settings/#http

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=3600)

# Security
# https://docs.djangoproject.com/en/4.2/ref/settings/#security

CSRF_COOKIE_DOMAIN = env.str(
    "CSRF_COOKIE_DOMAIN", default=env.str("RAILWAY_PUBLIC_DOMAIN")
)

CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=True)

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=[
        f"https://{env.str('RAILWAY_PUBLIC_DOMAIN')}",
    ],
)

SECRET_KEY = env.str("SECRET_KEY")

# Sessions
# https://docs.djangoproject.com/en/4.2/ref/settings/#sessions

SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=True)
