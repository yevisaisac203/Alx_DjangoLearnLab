from django.urls import path
from .views import add_book 
from .views import edit_book
from .views import delete_book


urlpatterns = [
    path('books/add/', add_book, name='add_book'),  # URL for adding a book
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),  # URL for editing a book
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),  # URL for deleting a book
]