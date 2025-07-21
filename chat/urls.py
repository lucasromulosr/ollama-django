from django.urls import path

from chat.views import chat_view, clear_chat_context

urlpatterns = [
    path('', chat_view, name='chat'),
    path('context/clear/', clear_chat_context, name='context-clear'),
]
