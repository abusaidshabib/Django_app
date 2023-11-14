from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        pi = User.objects.get(pk=1)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            # print(name, email, password)
            # -----------save
            # reg = User(name=name, email=email, password=password)
            # reg.save()
            # -----------update
            # reg = User(id=1, name=name, email=email, password=password)
            # reg.save()
            fm.save()
            # -----------delete
            # reg = User(id=2)
            # reg.delete()
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/userregistration.html', {'form':fm})