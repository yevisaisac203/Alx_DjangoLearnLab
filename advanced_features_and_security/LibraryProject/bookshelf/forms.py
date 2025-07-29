from django import forms
from .models import Book

# Example form for adding/editing a Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
