"""
ASGI config for medicalApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import base.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicalApp.settings')

application = get_asgi_application()
    #'http' : ProtocolTypeRouter({,
    # 'websocket' : AuthMiddlewareStack(
    #     URLRouter(
    #         base.routing.websocket_rulpatterns
    #     )
    # )
#})
