"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from shortener.views import UrlMappingCreateView, resolve_url

from .currency import CurrencyView
from . import views

urlpatterns = [
    #path('', views.index),
    path('admin/', admin.site.urls),
    path('currency/', CurrencyView.as_view()),
    
    path('shortener', UrlMappingCreateView.as_view()),
    path('shortener/<int:pk>', UrlMappingCreateView.as_view(), name='create-view'),
    path('url/<str:url_hash>', resolve_url),
]
