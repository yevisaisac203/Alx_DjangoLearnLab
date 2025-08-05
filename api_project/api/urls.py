from .views import BookList  # This should match the name of your view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet 
from rest_framework.authtoken.views import obtain_auth_token# import both views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Optional: keep old list view
    path('token/', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),  # Routes all CRUD endpoints
]



