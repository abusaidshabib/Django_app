from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def initial_page(request):
    return HttpResponse("Initial page")


def learn_python(request):
    return HttpResponse("<h1>Hello Python</h1>")
