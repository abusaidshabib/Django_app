from django.urls import path
from .views import conditional, loop, large,single

urlpatterns = [
    path('home/', conditional),
    path('loop/', loop),
    path('large/', large),
    path('single/', single),
]
