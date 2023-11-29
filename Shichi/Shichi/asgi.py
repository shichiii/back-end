import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Chat.routing  # Import your routing module
from Chat.consumers import TokenAuthMiddleware # Import your routing module
import Chat.urls  # Import your routing module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(URLRouter(
        Chat.routing.websocket_urlpatterns
    )),
})