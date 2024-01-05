"""
URL configuration for jarvisSetup project.

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
from webserver import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home-assistant/', views.home_assistant, name='home_assistant'),
    path('tools/', views.tools, name='tools'),
    path('configuration-settings/', views.configuration_settings, name='configuration_settings'),
    path('general-customization/', views.general_customization, name='general_customization'),
]
