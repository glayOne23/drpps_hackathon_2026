"""Pengaturan purwarupa SIGAP (ARB-02): satu aplikasi Django + PostgreSQL.

Koneksi basis data diatur lewat variabel lingkungan SIGAP_DB_* (lihat README).
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SIGAP_SECRET_KEY", "purwarupa-sigap-bukan-untuk-produksi")
DEBUG = os.environ.get("SIGAP_DEBUG", "1") == "1"
ALLOWED_HOSTS = ["*"]  # purwarupa: boleh dibuka dari HP di jaringan Wi-Fi yang sama

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "penjualan",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sigap.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sigap.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("SIGAP_DB_NAME", "sigap"),
        "USER": os.environ.get("SIGAP_DB_USER", "sigap"),
        "PASSWORD": os.environ.get("SIGAP_DB_PASSWORD", "sigap"),
        "HOST": os.environ.get("SIGAP_DB_HOST", "127.0.0.1"),
        "PORT": os.environ.get("SIGAP_DB_PORT", "5432"),
    }
}

LANGUAGE_CODE = "id"
TIME_ZONE = "Asia/Jakarta"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
