from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_fees(request):
    return HttpResponse('Hello Fees')

def learn_teas (request):
    return HttpResponse('Hello Teas')