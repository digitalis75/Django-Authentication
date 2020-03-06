from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


# Log the user out
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully been logged out!')
    return redirect(reverse('index'))


# Return Login page
def login(request):
    login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
