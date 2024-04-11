# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm , LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Manually set password
            user.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'type': 'Signup'})


def login_view(request):
    form = LoginForm()  # Initialize the form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')  # Redirect to home page after successful login
            else:
                return redirect('signup')  # Redirect to signup page if authentication fails
    return render(request, 'register.html', {'form': form, 'type': 'Login'})




def logout_view(request):
    logout(request)
    return redirect('login')
