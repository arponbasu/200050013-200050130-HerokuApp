"""
ASGI config for cs251lab4_200050013_200050130 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs251lab4_200050013_200050130.settings')

application = get_asgi_application()
