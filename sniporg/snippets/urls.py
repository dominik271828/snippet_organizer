from django.urls import path, reverse_lazy

from . import views
from django.contrib.auth import views as auth_views

app_name = "snippets"

urlpatterns = [
    path("", views.index, name="index"), 
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"), 
    path("logout/", auth_views.LogoutView.as_view(template_name="snippets/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("delete_snippet/", views.delete_snippet, name="delete_snippet"),
    path("view/<int:pk>", views.ViewSnippetView.as_view(), name="view"),
    path("login/", auth_views.LoginView.as_view(template_name="snippets/login.html", next_page=reverse_lazy("snippets:dashboard")), name="login"), 
    path("edit/<int:pk>", views.SnippetUpdateView.as_view(), name="edit"),
    path("create/", views.SnippetCreateView.as_view(), name="create"),
]