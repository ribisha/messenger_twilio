
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('need_help', views.need_help, name='need_help'),
   
]