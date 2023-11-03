from django.shortcuts import render

# Create your views here.
def homePage(request):
    courseName = {'cname':'React'}
    # return render(request, 'fees/home.html', courseName)
    return render(request, 'fees/home.html',  {'cname':'React'})

def aboutPage(request):
    django_details = {'cname':'Django', 'duration':'4 Months', 'seats':'10'}
    return render(request, 'fees/about.html', context=django_details)
