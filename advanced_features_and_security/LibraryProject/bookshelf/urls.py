from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('form/', views.example_form, name='example_form'),
    path('', include('bookshelf.urls')),
]
