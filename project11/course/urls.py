from django.urls import path
from .views import learn_django

urlpatterns = [
    path('home', learn_django),
]
