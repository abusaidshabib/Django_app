from django.urls import path
from .views import learn_dj

urlpatterns = [
    path('', learn_dj),
]
