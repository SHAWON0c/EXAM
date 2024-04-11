from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']