import os
from pathlib import Path
import dj_database_url

# ==========================
# RUTAS
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# CONFIGURACIÓN BÁSICA
# ==========================

# Usa la de entorno en Render; este valor solo es fallback local
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "-_&+lsebec(whhw!%n@ww&1j=4-^j_if9x8$q778+99oz&!ms2"
)

# En Render pon DEBUG=False en las env vars; aquí solo leemos el valor
DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",                # cualquier dominio de Render
    "app-web-api.onrender.com",     # tu servicio concreto
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
    # WhiteNoise si luego quieres servir estáticos desde Render
    # "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    # CORS SIEMPRE ANTES DE CommonMiddleware
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

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    # URL pública de tu front (ajusta a la actual si cambió)
    "https://sistema-web-app.vercel.app",
    # Previews de Vercel, cualquier subdominio
    # (si quieres ser más estricto, quita este regex)
]

CORS_ORIGIN_WHITELIST = CORS_ALLOWED_ORIGINS

CORS_ORIGIN_REGEX_WHITELIST = [
    r"^http://localhost:4200$",
    r"^https://sistema-web-.*\.vercel\.app$",
]

# ==========================
# URLS / TEMPLATES / WSGI
# ==========================

ROOT_URLCONF = "app_escolar_api.urls"

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
# Render te da la variable DATABASE_URL. Si no está, usamos SQLite local.

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=not DEBUG,
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

# ==========================
# ESTÁTICOS
# ==========================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ==========================
# DRF
# ==========================

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
