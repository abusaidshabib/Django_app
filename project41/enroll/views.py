from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def regi(request):
    messages.info(request, 'Now you can login')
    messages.success(request, 'Updated things')
    messages.warning(request, 'Something warning')
    messages.error(request, 'Something error')
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})