from django.urls import path
from .views import homePage, aboutPage

urlpatterns = [
    path('', homePage),
    path('about', aboutPage)
]
