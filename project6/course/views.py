from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def learn_mango(request):
    return HttpResponse('Hello mango')


def learn_django(request):
    return HttpResponse('Hello Python')
