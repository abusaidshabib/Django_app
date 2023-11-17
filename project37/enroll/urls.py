from django.urls import path, register_converter
from . import converters
from .views import home

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('home/<yyyy:year>', home,  name="home"),
]