from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment,Tag
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import PostForm
from django.db.models import Q
from django.views.generic import ListView

from .forms import RegisterForm, ProfileForm,CommentForm

class PostsByTagListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # reuse your list template
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        tag_name = self.kwargs["tag_name"]
        return (Post.objects.filter(tags__name__iexact=tag_name)
                .select_related("author")
                .prefetch_related("tags")
                .distinct()
                .order_by("-id"))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["active_tag"] = self.kwargs["tag_name"]
        ctx["tag_filter"] = True
        return ctx

class PostSearchListView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get("q", "").strip()
        if not q:
            return Post.objects.none()
        return (Post.objects.filter(
                    Q(title__icontains=q) |
                    Q(content__icontains=q) |
                    Q(tags__name__icontains=q)
                )
                .select_related("author")
                .prefetch_related("tags")
                .distinct()
                .order_by("-id"))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["q"] = self.request.GET.get("q", "").strip()
        return ctx

@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.post = post
            c.author = request.user
            c.save()
    return redirect(post.get_absolute_url())

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.select_related('author').all()
        context['comment_form'] = CommentForm()
        return context


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

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']   # adjust based on your Comment model fields
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        # Attach the comment to the right post
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user   # assuming comment has author
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the post detail after creating comment
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})    


