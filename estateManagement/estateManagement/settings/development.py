from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@estatemanagement.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Estate Management"

DATABASES = {   
       'default': {
        'ENGINE': 'django.db.backends.sqlite3',   # Database engine
        'NAME': BASE_DIR / 'db.sqlite3',          # Path to the SQLite database file
    }
    # "default" : {
    #     "ENGINE" : env("POSTGRES_ENGINE"),
    #     "NAME": env("POSTGRES_DB"),
    #     "USER": env("POSTGRES_USER"),
    #     "PASSWORD": env("POSTGRES_PASSWORD"),
    #     "HOST": env("PG_HOST"),
    #     "PORT": env("PG_PORT"),
    # }

}

