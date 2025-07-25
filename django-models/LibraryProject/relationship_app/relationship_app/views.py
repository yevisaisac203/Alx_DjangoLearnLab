# relationship_app/views.py

from django.shortcuts import render
from django.views import DetailView
from .models import Book, Library

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-Based View to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'