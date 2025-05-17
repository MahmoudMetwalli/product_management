import os

from django.core.asgi import get_asgi_application

# Install uvloop as the default event loop

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "code_quest_django.settings")

application = get_asgi_application()
