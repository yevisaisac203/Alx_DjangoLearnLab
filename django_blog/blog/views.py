from django.shortcuts import render,redirect
from .models import Post
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import PostForm

from .forms import RegisterForm, ProfileForm

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        return self.get_object().author == self.request.user

def index(request):
    """
    Home page (example): list posts or show a welcome.
    """
    posts = Post.objects.order_by("-published_date")[:10]
    return render(request, "blog/index.html", {"posts": posts})


def register(request):
    """
    Handles GET (empty form) and POST (create user).
    - On success: log the user in and send them to the profile page.
    - On failure: re-render form with errors.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()         # creates the User securely (password hashed)
            login(request, user)       # logs them in immediately
            messages.success(request, "Your account was created. Welcome!")
            return redirect("profile")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})


class UserLoginView(LoginView):
    """
    Uses Django's built-in LoginView.
    We only say which template to render; the view handles validation.
    """
    template_name = "blog/login.html"


class UserLogoutView(LogoutView):
    """
    Built-in logout. If you set LOGOUT_REDIRECT_URL in settings,
    Django will send the user there after logging out.
    """
    template_name = "blog/logout.html"


@login_required
def profile(request):
    """
    Allows logged-in users to view/edit their basic profile fields.
    - GET: show the form with current values.
    - POST: validate and save changes.
    """
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})

def index(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def index(request):
    return HttpResponse("Hello, this is my blog!")


