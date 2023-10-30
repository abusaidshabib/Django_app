from django.urls import path
# from fees.views import learn_fees, learn_teas
from .views import learn_django, learn_mango

urlpatterns = [
    path('mango', learn_mango),
    path('django', learn_django),
]
