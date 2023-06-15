from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


# Create your views here.
def index(request: HttpResponse) -> HttpResponse:
    return render(request, "personal/index.html")


class PersonalList(ListView):
    model = models.Personal
    template_name = "personal/personal_list.html"
    context_object_name = "empleados"


class PersonalCreate(CreateView):
    model = models.Personal
    form_class = forms.PersonalForm
    template_name = "personal/personal_create.html"
    success_url = reverse_lazy("personal:index")


class PersonalDelete(DeleteView):
    model = models.Personal
    template_name = "personal/personal_delete.html"
    success_url = reverse_lazy("personal:index")


class PersonalUpdate(UpdateView):
    model = models.Personal
    form_class = forms.PersonalForm
    template_name = "personal/personal_update.html"
    success_url = reverse_lazy("personal:index")
