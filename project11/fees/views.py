from django.shortcuts import render

# Create your views here.
def conditional(request):
    return render(request, 'fees/home.html', {'name':True, 'state':5})