from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Article

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
