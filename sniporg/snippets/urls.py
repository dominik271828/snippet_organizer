from django.urls import path

from . import views

app_name = "snippets"

urlpatterns = [
    path("", views.index, name="index"), 
    path("login/", views.login, name="login"), 
    path("dashboard/", views.dashboard, name="dashboard"), 
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("create_snippet/", views.create_snippet, name="create_snippet"),
    path("delete_snippet/", views.delete_snippet, name="delete_snippet"),
    path("edit_snippet/", views.edit_snippet, name="edit_snippet"),
    path("view_snippet/", views.view_snippet, name="view_snippet"),

]