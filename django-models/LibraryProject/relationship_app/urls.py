from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # FBV
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV
     path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
     path('add_book/', views.add_book, name='add_book'),   # Add Book View
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit Book View
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]