from django.urls import path
from .views import fees_home

urlpatterns = [
    path('home/', fees_home),
]