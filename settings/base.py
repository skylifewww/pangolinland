import sys
from pathlib import Path

BASE_DIR = Path()


def rel(*x):
    return str(BASE_DIR.joinpath(*x).absolute())

DEBUG = False
DOMAIN = 'localhost:8000'

APPEND_SLASH = True
ALLOWED_HOSTS = ["pangolinlanding.herokuapp.com", DOMAIN]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_AGE = 1209600  # (2 weeks)
SESSION_COOKIE_NAME = 'sessionid'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

SECRET_KEY = '6qf20&*1&@bjyx8wobz*&+&36!0=ng(m^eyuyw$!j9%5+&u_n2'

ROOT_URLCONF = 'pangolinland.urls'

WSGI_APPLICATION = 'wsgi.application'

TESTING = 'test' in sys.argv[0]
DEVELOPMENT = 'run.py' in sys.argv or 'runserver' in sys.argv or 'collectstatic' in sys.argv

if 'test' in sys.argv:
    print('\033[1;91mNo django tests.\033[0m')
    print('Try: \033[1;33mpy.test\033[0m')
    sys.exit(0)
