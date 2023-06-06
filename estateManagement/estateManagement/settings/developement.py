from .base import *

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
