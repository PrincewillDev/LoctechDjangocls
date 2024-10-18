from django.shortcuts import render, redirect
from .models import Book
from .form import BookForm
# from django.http import HttpResponse

# Create your views here.

def get_books(request):
    book = Book.objects.all()
    return render(request, '/home/princewill-elebhose/Documents/Loctech_Work_Resources/test_django/templates/book_list.html', {'books':book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            print('Data has been sent')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, '/home/princewill-elebhose/Documents/Loctech_Work_Resources/test_django/templates/add_book.html', {'form': form})