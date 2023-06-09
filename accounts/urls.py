from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from accounts.views import SignupView, profile

app_name = "account"
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('signup/done/', auth_views.LoginView.as_view(template_name='account/signup_done.html'), name='signup_done'),
]