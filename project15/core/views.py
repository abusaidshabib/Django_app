from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def test(request):
    return render(request, 'course/info.html')