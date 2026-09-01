from django.urls import path
from django.shortcuts import render,redirect
from . import views

urlpatterns = [
    path('',views.index,name='index' ),
    path("contact/", views.contact, name="contact"),
]
