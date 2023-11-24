from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, EditProfile, EditAdminProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.
# Signup view
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})

# Login view
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data= request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form':fm})
    else:
         return HttpResponseRedirect('/profile/')


# Import necessary modules and your EditProfile form
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfile(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditProfile(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfile(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditProfile(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {'name': request.user, 'form': fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/')


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # help to update the session that's not logout
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def user_details(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfile(instance=pi)
        return render(request, 'enroll/userdetails.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')