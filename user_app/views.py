from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
# from sharad_app.models import Tasklist
# from sharad_app.form import TaskForm
from django.contrib import messages
# from django.core.paginator import Paginator
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save() 
            messages.success(request, ("New Account Created!"))
            return redirect('register')
    else:
        register_form = CustomUserCreationForm()
    return render (request, 'register.html', {'register_form' : register_form})
    