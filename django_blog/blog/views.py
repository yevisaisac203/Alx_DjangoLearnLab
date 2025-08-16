from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def index(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def index(request):
    return HttpResponse("Hello, this is my blog!")


