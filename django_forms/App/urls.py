from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.createStudent, name='createStudent'),
    path('success/', views.success, name='success'),
]
