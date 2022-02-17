from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

class NewAccount(UserCreationForm):
    first_name =  forms.CharField(max_length=100)
    last_name   =  forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

# User = get_user_model()

# class UserAdminCreationForm(forms.ModelForm):
#     """a form for creating new users. including all the required fields, and repeated passwords """
#     password1 = forms.CharField(label = "Password", widget = forms.PasswordInput)
#     password2 = forms.CharField(label = "Password confirmation", widget = forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username','first_name', 'last_name')

#     def clean_password2(self):
#         #check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")

#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Password doesn`t match")
#         return password2

#     def save(self, commit=True):
#         #save the provoded password in hashed format
#         user = super(UserAdminCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.seve()
#         return user

# class UserAdminChangeForm(forms.ModelForm):
#     """a form for updating users,including all the fields on users but 
#     replaces the password field with admin`s pwd hash display """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'password', 'active', 'admin')


#     def clean_password(self):
#         #regadless of ehat user provide it return the initial value only
#         #this is done here rather than in the field because the field 
#         #does not have the access to the initial value
#         return self.initial["password"]

class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2',)
    

    def clean_username(self):
        username = self.cleaned_data.get('username')
        us = User.objects.filter(username = username)
        if us.exist():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords must match.")
        return data