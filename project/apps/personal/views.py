from . import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def index(request: HttpResponse) -> HttpResponse:
    return render(request, "personal/index.html")


def añadir_personal(request):
    if request.method == "POST":
        form = forms.PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home/index.html")
    else:
        form = forms.PersonalForm()
        context = {"form": form}
        return render(request, "personal/index.html", context)
