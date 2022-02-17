from django.shortcuts import render, HttpResponse, redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import *
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from .models import UserProfile


#registration view
class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "user/register.html"
    success_url = reverse_lazy('login')

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url

#login page...
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect_url    =   request.GET.get('next', 'homepage')
            messages.success(request, "You`re logged in as "+ username)
            return redirect(redirect_url)

        else:
            messages.info(request, "Incorrect username or password")

        def get_success_url(self):
            if "next" in self.request.GET:
                next_url = self.request.GET.get("next")
                return next_url
            else:
                return self.success_url
    context = {}
    return render(request, 'user/login.html', context)


#create profile page
class CreateProfile(generic.CreateView):
    midel = UserProfile
    form_class = CreateProfileForm
    template_name = "user/create_profile.html"

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if request.user.is_authenticated:
            pass
        else:
            return redirect("/signin/?next=/create_profile/")
        return super().dispatch(request, *args, **kwargs)

    success_url = reverse_lazy('profile')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#display a profile page dynamic
class ProfileView(generic.ListView):
    model = UserProfile
    template_name = "user/profile.html"

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if request.user.is_authenticated:
            pass
        else:
            return redirect("/signin/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)


#edit profile page
class EditProfile(generic.UpdateView):
    model = UserProfile
    template_name = "user/edit_profile.html"
    fields = (
            "profile_picture", "date_of_birth", "phone_number"
            )
    success_url = reverse_lazy('profile')

#edit user profile
class EditSettings(generic.UpdateView):
    form_class = ProfileChangeForm
    template_name = "user/edit_settings.html"
    success_url = reverse_lazy('profile')
    
    
    def get_object(self):
        return self.request.user


#change password 
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "user/pwd_change.html"
    success_url = reverse_lazy("password_changed_successful")


def password_changed_successful(request):
    return render(request, "user/password_changed_successful.html", {})


#log out function...
# this terminate user authentication
def logoutV(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect("homepage")



