from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login as django_login,
                                 logout as django_logout)
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Snippet, Lang
from django.utils import timezone
from .pygmentsutils import formatCode

def index(request):
    return redirect("snippets:login")

def login(request):
    if (request.user.is_authenticated):
        return redirect("snippets:dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
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
        s = Snippet(title=request.POST["title"], data=request.POST["data"], 
                    lang=Lang.objects.get(name=request.POST["lang"]), pub_date=timezone.now(), owner=request.user)
        s.save()
    # fetch languages from database
    langs = Lang.objects.all()
    return render(request, "snippets/create_snippet.html", context={"langs":langs})

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

@login_required
def edit_snippet(request):
    if "title" in request.POST.keys():
        print(dict(request.POST))
        snip = Snippet.objects.get(pk=request.POST["id"])
        snip.title = request.POST["title"]
        snip.data = request.POST["data"]
        snip.save()
        return redirect("snippets:dashboard")
    id = list(request.POST.keys())[1]
    snip = Snippet.objects.get(pk=id)
    return render(request, "snippets/edit_snippet.html", context={"snip": snip})

@login_required
def view_snippet(request):
    id = list(request.POST.keys())[1]
    snip = Snippet.objects.get(pk=id)
    context ={ "snippet": snip, "code": formatCode(code=snip.data, lexerAlias=snip.lang.lexer_name)}
    return render(request, "snippets/view_snippet.html", context)