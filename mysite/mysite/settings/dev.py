# encoding: utf-8
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['194.87.93.29', '127.0.0.1', 'buzaza.ddns.net']

INTERNAL_IPS = ['127.0.0.1']


# Emails in file
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR + '/emails' # change this to a proper location