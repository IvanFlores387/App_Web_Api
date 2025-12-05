import os
from pathlib import Path
import dj_database_url   # <-- importante para Render

# ==========================
# RUTAS
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# CONFIGURACIÓN BÁSICA
# ==========================

# En Render pon SECRET_KEY como variable de entorno; aquí dejamos un fallback
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "-_&+lsebec(whhw!%n@ww&1j=4-^j_if9x8$q778+99oz&!ms2"
)

# En Render debes poner DEBUG=False en las env vars
DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",                 # cualquier dominio de Render
    "ivanflores387.pythonanywhere.com",  # por si sigues usando PA para algo
]

# ==========================
# APPS
# ==========================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "app_escolar_api",
]

# ==========================
# MIDDLEWARE
# ==========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise para servir estáticos en Render
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==========================
# CORS
# ==========================

CORS_ALLOWED_ORIGINS = [
    "https://sistema-web-app.vercel.app",
    "http://localhost:4200",
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = "app_escolar_api.urls"

# ==========================
# TEMPLATES / STATIC / MEDIA
# ==========================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = "/static/"
# Carpeta donde collectstatic va a guardar los archivos para producción
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "app_escolar_api.wsgi.application"

# ==========================
# BASE DE DATOS (Render: DATABASE_URL -> Postgres)
# ==========================
# En Render vas a definir la variable de entorno DATABASE_URL
# (te la da el servicio de PostgreSQL).
# En local, si no existe DATABASE_URL, usa SQLite en db.sqlite3.

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=not DEBUG,  # en Render (DEBUG False) fuerza SSL a Postgres
    )
}

# ==========================
# AUTH / I18N / DRF
# ==========================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "app_escolar_api.models.BearerTokenAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
}
