from django.urls import path

from ollama_api.views import select_model

urlpatterns = [
    path('model/select/', select_model, name='check-model-select'),
]
