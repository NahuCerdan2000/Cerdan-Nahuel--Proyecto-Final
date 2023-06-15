from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from . import forms


# Create your views here.
def index(request: HttpResponse) -> HttpResponse:
    return render(request, "home/index.html")  # type: ignore


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {"mensaje": f"¡Bienvenido {usuario}!"})
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = forms.CustomerCreationsForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje": "¡Usuario Creado Correctamente!"})
    else:
        form = forms.CustomerCreationsForm()
    return render(request, "home/register.html", {"form": form})
