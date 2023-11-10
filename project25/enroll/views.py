from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    fm = StudentRegistration()
    # fm = StudentRegistration(auto_id='some_%s')
    # fm = StudentRegistration(auto_id=False)
    # fm = StudentRegistration(auto_id=True)
    # fm = StudentRegistration(auto_id=True, label_suffix='-', initial={'name':'User Name Initial Value', 'email':'test@initail@gmail.com'})
    # fm.order_fields(field_order=['email', 'name', 'first_name']) #help to order the form
    return render(request, 'enroll/userregistration.html', {'form':fm})

