from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Article
from .models import Book
from django.views.decorators.csrf import csrf_protect
from .forms import ExampleForm

@csrf_protect
def example_form(request):
    message = ''
    form = ExampleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        message = f"Thank you, {name}!"
    return render(request, 'bookshelf/form_example.html', {'form': form, 'message': message})

# Example form view (CSRF protected)
@csrf_protect
def example_form(request):
    message = ''
    if request.method == "POST":
        # Safely handle form input (no DB for this task)
        name = request.POST.get('name', '').strip()
        message = f"Thank you, {name}!" if name else "Please enter a valid name."
    return render(request, 'bookshelf/form_example.html', {'message': message})

# View to list all books, protected by can_view permission
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    # Code for creating article (form logic here)
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, article_id):
    # Code for editing article
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, article_id):
    # Code for deleting article
    pass
