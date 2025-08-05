from django.urls import path
from .views import BookList  # This should match the name of your view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
