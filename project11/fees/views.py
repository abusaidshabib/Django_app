from django.shortcuts import render

# Create your views here.
def conditional(request):
    return render(request, 'fees/home.html', {'name':True, 'state':5})

def loop(request):
    student = {'names':['Rahul', 'Sonam', 'Raj', 'Anu']}
    return render(request, 'fees/loop.html', student)

def large(request):
    student = {
        'stu1':{'name':'Rahul', 'roll':101},
        'stu2':{'name': 'Sonam', 'roll':102},
        'stu3':{'name':'Raj', 'roll':103},
        'stu4':{'name':'Anu', 'roll':104}
    }
    students = {'student':student}
    return render(request, 'fees/largeLoop.html', students)

def single(request):
    data = {'name':'Rahul', 'roll': 101}
    return render(request, 'fees/single.html', {'data':data})