from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'USER': env('USER'),
        'USER': 'postgres',
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),  
        'PORT': env('PORT'),
    }
}


