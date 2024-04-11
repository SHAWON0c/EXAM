from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from first_app.forms import RegisterForm  # Assuming RegisterForm is defined in first_app.forms
from django.contrib.auth.decorators import login_required



def Signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')  # Redirect to home or any appropriate URL after successful registration
    else:
        form = RegisterForm() 
    return render(request, 'home.html', {'form': form, 'type': 'Signup'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('profile')  # Redirect to profile page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'home.html', {'form': form, 'type': 'Login'})



@login_required
def profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'profile.html', {'username': username})



@login_required
def logout_view(request):
    
    logout(request)
    # Add a logout message if desired
    messages.success(request, 'You have been logged out successfully!')
    
    return redirect('login') 

 # Redirect to the login page after logout
@login_required
def changepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'passchange.html', {'form': form})


@login_required
def changepass2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)

    return render(request, 'passchange.html', {'form': form})