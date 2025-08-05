from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.urls import path
from django.http import JsonResponse

def placeholder_view(request):
    return JsonResponse({"message": "This works!"})

urlpatterns = [
    path('books/', placeholder_view),
]


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
