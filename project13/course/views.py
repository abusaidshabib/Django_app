from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'course/home.html', {'name':'Course Page'})