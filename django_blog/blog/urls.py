from django.urls import path
from . import views
from .views import UserLogoutView, UserLoginView, register, index

urlpatterns= [
    path('', views.index, name='bog-index'),
    path("", index, name="home"),
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path('posts/', views.Post, name='posts'),  
]