from django.urls import path
from .views import showformdata

urlpatterns = [
    path('registration/', showformdata),
]