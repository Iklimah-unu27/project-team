from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoe),
    path('about', views.about, name='about'),
    path('guru', views.guru, name='guru'),
    
]