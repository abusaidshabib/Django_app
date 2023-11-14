from django.shortcuts import render

# Create your views here.
def home(request, year):
    print(year)

    return render(request, "enroll/home.html", {'year':year})

