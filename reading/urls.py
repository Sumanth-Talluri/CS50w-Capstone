from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("user", views.user_view, name="user"),
    path("search", views.search, name="search"),
    path("book/<str:gid>", views.book, name="book"),
    path("add_book/<str:gid>", views.add_book, name="add_book"),
    path("topbooks", views.topbooks, name="topbooks"),
    path("topreaders", views.topreaders, name="topreaders")
]
