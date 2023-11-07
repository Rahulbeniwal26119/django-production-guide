import environ

env = environ.Env()

LOCAL = env.bool("DJANGO_LOCAL", default=True)
PRODUCTION = env.bool("DJANGO_PRODUCTION", default=False)

if PRODUCTION:
    from .production import *  # noqa
else:
    from .local import *
