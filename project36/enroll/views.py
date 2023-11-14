from django.shortcuts import render

# Create your views here.
def home(request, check):
    print(check)
    return render(request, "enroll/home.html")

def show_details(request, my_id):
    print(my_id)
    if my_id == 1:
        student = {'id':my_id, 'name':'Rohan'}
    if my_id ==2:
        student = {'id':my_id, 'name':'Tohan'}
    if my_id ==3:
        student = {'id':my_id, 'name':'Cohan'}
    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id, my_class):
    print(my_id, my_class)
    if my_id == 1 and my_class == 1:
        student = {'id':my_id, 'name':'Rohan', 'info':my_class}
    if my_id ==2 and my_class == 2:
        student = {'id':my_id, 'name':'Tohan', 'info':my_class}
    if my_id ==3 and my_class == 3:
        student = {'id':my_id, 'name':'Cohan', 'info':my_class}
    return render(request, 'enroll/show.html', student)