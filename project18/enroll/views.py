from django.shortcuts import render
from .models import Student
# Create your views here.
def student(request):
    student = Student.objects.all()
    # need to print without for loop for specific data
    # student = Student.objects.get(pk=2)
    print('My output', student)
    return render(request, 'enroll/student.html', {'student':student})