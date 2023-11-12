from django.urls import path
from .views import registration, thankyou

urlpatterns = [
    path('registration/', registration),
    path('success/', thankyou, name='registration_success')
]
