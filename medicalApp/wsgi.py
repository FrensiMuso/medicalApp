"""
WSGI config for medicalApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from base.mqtt import thread1

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicalApp.settings')

application = get_wsgi_application()
thread1.start()