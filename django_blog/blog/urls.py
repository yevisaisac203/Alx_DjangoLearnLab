from django.urls import path
from . import views
from .views import UserLogoutView, UserLoginView, register, index, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import PostDetailView,comment_create,CommentUpdateView,CommentDeleteView


urlpatterns= [
    path("", index, name="home"),
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    #posts URLS
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # Comment routes:
    path('post/new/', PostCreateView.as_view(), name='post'),
    path("posts/<int:pk>/comments/new/", comment_create, name="comment-create"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-edit"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

]