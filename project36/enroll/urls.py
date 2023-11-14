from django.urls import path, include
from .views import home, show_details, show_subdetails

urlpatterns = [
    # kwargs is {'check':'OK'}
    path('home/', home, {'check':'OK'}, name="home"),
    # path('student/<my_id>/', show_details, name="detail"),
    # <int:my_id> will only return the int value
    path('student/<int:my_id>/', show_details, name="detail"),
    path('student2/<int:my_id>/<int:my_class>', show_subdetails, name="class"),
]