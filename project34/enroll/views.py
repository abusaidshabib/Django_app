from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            # reg = User(name=name, email=email, password= password)
            # reg.save()

            # for delete
            reg = User(id=1)
            reg.delete()

    else:
        fm = StudentRegistration        
    return render(request, 'enroll/userregistration.html', {'form':fm})