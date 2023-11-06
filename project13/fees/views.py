from django.shortcuts import render

# Create your views here.
def fees_home(request):
    return render(request, 'fees/home.html', {'name':'Fees Page'})