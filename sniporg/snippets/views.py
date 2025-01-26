from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login as django_login,
                                 logout as django_logout)
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Snippet, Lang
from django.utils import timezone
from .pygmentsutils import formatCode
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from . import forms as myForms

def index(request):
    return redirect("snippets:login")

def register(request):
    if (request.user.is_authenticated):
        return redirect("snippets:dashboard")
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            u = User.objects.create_user(username=username, password=password)
            context = {"message":"User created successfully"}
            u.save()
        else:
            context = {"message":"Username taken"}
    return render(request, "snippets/register.html", context)

class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = "snippets/dashboard.html"
    login_url = reverse_lazy('snippets:login')

    def get_queryset(self):
        return Snippet.objects.filter(owner=self.request.user)

@login_required
def delete_snippet(request):
    if request.method == "POST":
        print(request.user.username)
        #if request.user.username == 'john':
        #    return redirect("snippets:dashboard")
        delete_id = list(request.POST.keys())[1]
        snip = Snippet.objects.get(pk=delete_id) 
        if (request.user == snip.owner):
            snip.delete()
    return redirect("snippets:dashboard")

class SnippetUpdateView(generic.edit.UpdateView):
    model = Snippet
    form_class = myForms.SnippetUpdateForm

    def get_success_url(self):
        return reverse("snippets:dashboard")

class SnippetCreateView(generic.edit.CreateView):
    model = Snippet
    form_class = myForms.SnippetUpdateForm

    def get_success_url(self):
        return reverse("snippets:dashboard")

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        super().form_valid(form)
        return redirect("snippets:dashboard")

class ViewSnippetView(generic.DetailView):
    template_name = "snippets/view_snippet.html"
    model = Snippet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formattedCode"] = formatCode(context["snippet"].data, context["snippet"].lang.lexer_name)
        return context