from .base import * # noqa
from .base import env

DJANGO_SECRET_KEY = env(
    "DJANGO_SECRET_KEY"
)

DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000"
]