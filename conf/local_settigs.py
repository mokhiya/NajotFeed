from conf.settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG= True