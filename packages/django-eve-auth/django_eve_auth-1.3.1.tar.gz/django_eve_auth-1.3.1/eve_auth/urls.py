"""Routes for Eve Auth."""

from django.urls import path

from . import views

app_name = "eve_auth"

urlpatterns = [
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
