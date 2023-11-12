from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.

def thankyou(request):
    return render(request, 'enroll/RedirectSuccess.html' )

def registration(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # print(fm)
        if fm.is_valid():
            print(fm.cleaned_data)
            print('Form Validated')
            # print('Name:', fm.cleaned_data['name'])
            # print('Email:', fm.cleaned_data['email'])
            # print('Password:', fm.cleaned_data['password'])
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print(name, email, password)
            # not recommendend 
            # fm = StudentRegistration()
            
            return HttpResponseRedirect('/api/v4.2/enroll/success/')
            # return render(request, 'enroll/RedirectSuccess.html', {'name':name})

        else:
            print('It is not valid')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/Registration.html', {'form':fm})