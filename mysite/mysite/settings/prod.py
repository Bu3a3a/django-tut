# encoding: utf-8
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['buzaza.pythonanywhere.com']

INTERNAL_IPS = ['127.0.0.1']


# HTTP -> HTTPS
SECURE_SSL_REDIRECT = True


# If a browser connects initially via HTTP, which is the default for most browsers, it is possible for existing cookies
# to be leaked. For this reason, you should set your SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE settings to True.
# This instructs the browser to only send these cookies over HTTPS connections. Note that this will mean that sessions
# will not work over HTTP, and the CSRF protection will prevent any POST data being accepted over HTTP (which will be
# fine if you are redirecting all HTTP traffic to HTTPS).
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# https://docs.djangoproject.com/en/1.11/ref/middleware/#http-strict-transport-security
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True