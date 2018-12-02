from .views import UpdateBot
from django.urls import path


urlpatterns = [
    path('bot', UpdateBot.as_view())
]