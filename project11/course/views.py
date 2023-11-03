from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_django(request):
    django_details= {'name':'Django', 'duration':'4 months', 'seats':'10', 'details': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Unde rem at sed! Id impedit illo nobis nulla dignissimos dicta? Quasi adipisci saepe delectus non iure id dignissimos cum debitis necessitatibus.', 'date':datetime.now(), 'float':56.045454}
    return render(request, 'course/home.html', context=django_details)