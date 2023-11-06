from django.shortcuts import render


# Create your views here.
def learn_dj(request):
    return render(request, 'course/courseInfo.html')