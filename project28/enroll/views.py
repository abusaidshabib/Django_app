from django.shortcuts import render

# Create your views here.
def registration(request):
    return render(request, 'enroll/Registration.html')