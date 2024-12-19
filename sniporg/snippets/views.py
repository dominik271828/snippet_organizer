from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login as django_login,
                                 logout as django_logout)
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Snippet, Lang
from django.utils import timezone
from .pygmentsutils import formatC

def index(request):
    return redirect("snippets:login")

def login(request):
    if (request.user.is_authenticated):
        return redirect("snippets:dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            django_login(request, user)
            return redirect("snippets:dashboard")
        else:
            return render(request, "snippets/login.html", {
                "message":"Login error, try again",
            })
    return render(request, "snippets/login.html", {})

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

def logout(request):
    django_logout(request)
    return render(request, "snippets/logout.html")

@login_required
def dashboard(request):
    snippets = request.user.snippet_set.all()
    context = {"snippets":snippets}
    return render(request, "snippets/dashboard.html", context)

@login_required
def create_snippet(request):
    if request.method == "POST":
        print(request.POST)
        s = Snippet(title=request.POST["title"], data=request.POST["data"], 
                    lang=Lang.objects.get(name=request.POST["lang"]), pub_date=timezone.now(), owner=request.user)
        s.save()
    return render(request, "snippets/create_snippet.html")

@login_required
def delete_snippet(request):
    if request.method == "POST":
        delete_id = list(request.POST.keys())[1]
        # TODO: Verify the snippet actually belongs to the user
        Snippet.objects.get(pk=delete_id).delete()
    return redirect("snippets:dashboard")

@login_required
def edit_snippet(request):
    return render(request, "snippets/edit_snippet.html")

@login_required
def view_snippet(request):
    id = list(request.POST.keys())[1]
    snip = Snippet.objects.get(pk=id)
    context ={ "snippet": snip, "code": formatC(snip.data)}
    return render(request, "snippets/view_snippet.html", context)