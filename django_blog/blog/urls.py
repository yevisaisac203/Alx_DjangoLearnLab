from django.urls import path
from . import views
from .views import UserLogoutView, UserLoginView, register, index, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns= [
    path('', views.index, name='bog-index'),
    path("", index, name="home"),
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path('posts/', views.Post, name='posts'),  
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]