# relationship_app/query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    return Librarian.objects.get(library__name=library_name)

if __name__ == "__main__":
    # Example usage
    print(books_by_author("George Orwell"))
    print(books_in_library("Main Library"))
    print(librarian_for_library("Main Library"))