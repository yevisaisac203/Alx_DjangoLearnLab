from rest_framework import serializers
from .models import Book  # Make sure Book model exists

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
