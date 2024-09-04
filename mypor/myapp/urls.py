"""
URL configuration for mypor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('', views.login_user, name='login'),
    path("signup/", views.signup_user, name='signup'),
    path('admin_panel/', views.user_list, name='admin_panel'),
    path('logout/', views.logout_user, name='logout'),
    path('activate/<str:encoded_id>/', views.activate, name='activate'),
    path("home/", views.homepage, name='home'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('add_user/', views.adds, name='add_user'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('update/<str:id>/', views.update, name='update'),
    path('blog/', views.blogs,name='blog'),
    path('contact/', views.contact, name='contact'),
    path('port/', views.portfolio, name='port'),
    path('password_reset/', PasswordResetView.as_view(template_name='pass_reset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset_confirm.html'), name='password_reset_confirm'),
    path('password_complete/',PasswordResetCompleteView.as_view(template_name='reset_complete.html'), name='password_reset_complete'),
]
