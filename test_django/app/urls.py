from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_books, name='get_books'),
    path('addbook/', views.add_book, name='add_book'),
]