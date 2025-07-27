from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100)  # Name of the library
    location = models.CharField(max_length=255)  # Location of the library

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Link to the Author model
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)  # Link to the Library model
    publication_year = models.IntegerField()  # Year the book was published

    def __str__(self):
        return self.title