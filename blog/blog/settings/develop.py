from .base import *       # NOQA   告诉PEP 8规范检测工具，这个地方不需要检查

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG=True