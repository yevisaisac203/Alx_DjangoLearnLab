from django.db import models

# Author model represents a book author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

# Book model represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book's title
    publication_year = models.IntegerField()  # Year published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
