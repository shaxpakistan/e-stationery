
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse
from .models import UserProfile

class SignUpForm(UserCreationForm):
    first_name      = forms.CharField(max_length=255)
    last_name       = forms.CharField(max_length=255)

    class Meta:
        model = User

        fields = ("username", "first_name", "last_name", "password1", "password2")



class ProfileChangeForm(UserChangeForm):
    first_name  = forms.CharField(max_length=255)
    last_name   = forms.CharField(max_length=255)
    username    = forms.CharField(max_length=255)
    email       = forms.EmailField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

        # model = UserProfile
        # fields = ('profile_picture', 'date_of_birth', 'phone_number')

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "profile_picture", "date_of_birth", "phone_number"
            )