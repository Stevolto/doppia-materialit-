import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')
    BABEL_DEFAULT_LOCALE = 'it'
    LANGUAGES = ['it', 'en', 'de']
