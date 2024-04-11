from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.views.generic import FormView
from .forms import UserSignupForm 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from car.models import Car
from django.contrib.auth import logout as django_logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .import forms, models


class signup(FormView):
    template_name='register.html'
    form_class= UserSignupForm
    success_url=reverse_lazy('profile')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

# # @login_required    
# def profile(request):
#     purchased_car_id = request.session.get('purchased_car')
#     purchased_car = None
#     if purchased_car_id:
#         purchased_car = get_object_or_404(Car, id=purchased_car_id)
#     return render(request, 'profile.html', {'car': purchased_car})


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def profile(request):
    purchased_car_id = request.session.get('purchased_car')
    purchased_car = None
    user_details = None
    
    if purchased_car_id:
        purchased_car = get_object_or_404(Car, id=purchased_car_id)
        
    if request.user.is_authenticated:
        user_details = request.user
        print("User is authenticated:", user_details.username)  # Debug statement
    
    print("User details:", user_details)  # Debug statement

    return render(request, 'profile.html', {'car': purchased_car, 'user': user_details})



# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     success_url = reverse_lazy('profile')
#     redirect_authenticated_user = True

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')  

    def form_valid(self, form):
        # Call the parent class's form_valid method
        super().form_valid(form)
        # Redirect to the success URL
        return redirect(self.get_success_url())
    
# @login_required
def logout_view(request):
    """
    Logout view.
    """
    django_logout(request)
    return redirect('homepage') 



class EditUserView(LoginRequiredMixin, UpdateView):
    template_name = 'register.html'  # Template for the edit form
    form_class = forms.UserEditForm  # Form class for editing user details
    success_url = reverse_lazy('profile')  # Redirect URL after successful form submission

    def get_object(self, queryset=None):
        return self.request.user  # Fetch the current logged-in user as the object to be edited

    def form_valid(self, form):
        form.save()  # Save the form data
        return super().form_valid(form)
