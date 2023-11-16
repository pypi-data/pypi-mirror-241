from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "fake-key"


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django_zupit_logging",
    "tests",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

ROOT_URLCONF = "tests.urls"

USE_TZ = True

TIME_ZONE = "Europe/Rome"

ZUPIT_LOGGING = {
    "BLACKLIST_URLS": ["/blacklisted/"],
    "SENSITIVE_FIELDS": ["password", "credit_card_number"],
    "REQUEST_ID_HEADER": "X-Request-ID",
    "APP_VERSION": "1.2.3",
}
