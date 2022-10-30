from django.urls import path

from chat_app.consumers.message import MessageConsumer
from chat_app.consumers.notification import NewUserConsumer

websocket_urlpatterns = [
    path('ws/notification/<str:username>/', NewUserConsumer.as_asgi()),
    path('ws/message/<str:username>/', MessageConsumer.as_asgi()),
]
