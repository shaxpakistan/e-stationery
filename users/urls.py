from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name = "register"),
    path('<int:pk>/password/', PasswordsChangeView.as_view(), name = "password"),
    path('profile/', ProfileView.as_view(), name = "profile"),
    
    path('<int:pk>/edit_profile/', EditProfile.as_view(), name = "edit_profile"),    
    path('<str:pk>/edit_settings/', EditSettings.as_view(), name = "edit_settings"),
    path('create_profile/', CreateProfile.as_view(), name = "create_profile"),
    path('password_changed_successful/', password_changed_successful, name = "password_changed_successful"),

    path('signin/', signin, name = 'login'),
    path('logoutV/', logoutV, name = 'logout'),
] 