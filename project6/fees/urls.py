from django.urls import path
# from fees.views import learn_fees, learn_teas
from .views import learn_fees, learn_teas

urlpatterns = [
    path('fees', learn_fees),
    path('teas', learn_teas)
]
