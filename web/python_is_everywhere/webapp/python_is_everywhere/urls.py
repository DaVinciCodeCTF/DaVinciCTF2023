"""python_is_everywhere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from interpretor import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='interpretor'),
    path('0d98dd7fa52c1cac27b7605b848c6756/', views.admin, name='admin'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('report/', views.report, name='report'),
    path('e93717a75fefedbb76ecadf91a73b95e/', views.bot, name='bot')
]
