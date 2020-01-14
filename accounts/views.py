from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm


def __init__(request):
    if request.user.is_authenticated:
        return redirect('/app/dashboard')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})
