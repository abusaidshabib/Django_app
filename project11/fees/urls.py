from django.urls import path
from .views import conditional

urlpatterns = [
    path('home/', conditional),
]
