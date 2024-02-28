from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('schedule/', views.profile, name="profile"),
    path('contact/', views.contact, name="contact"), 
    path('services/', views.services, name="services"),
    path('privacy/', views.privacy, name="privacy"),
    path('terms/', views.terms, name="terms")
]
