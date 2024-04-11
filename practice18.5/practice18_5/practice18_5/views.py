from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from first_app.forms import RegisterForm  # Assuming RegisterForm is defined in first_app.forms



def homemain(request):
    return render(request,'homemain.html')