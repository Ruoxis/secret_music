from django.urls import path
from .views import message,Templates
urlpatterns = [
    path('',message),
    path('a',Templates.as_view())
]