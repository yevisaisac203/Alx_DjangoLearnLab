from django.contrib import admin
from .models import Library, Book, Author

class BookInline(admin.TabularInline):
    model = Book
    extra = 1  # Number of empty forms to display

class LibraryAdmin(admin.ModelAdmin):
    inlines = [BookInline]  # Show books associated with the library in the library admin page

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the author's name in the admin list view

# Register the models with the admin site
admin.site.register(Library, LibraryAdmin)
admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)