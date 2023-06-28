from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

# Create your views here.

# Categoria Productos


def index(request: HttpResponse) -> HttpResponse:
    return render(request, "producto/index.html")  # type: ignore


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_list.html"
    context_object_name = "categorias"


class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_create.html"
    success_url = reverse_lazy("producto:index")


class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_delete.html"
    success_url = reverse_lazy("producto:index")


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_update.html"
    success_url = reverse_lazy("producto:index")


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_detail.html"


# Productos


class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:index")


class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Producto.objects.all()
        return object_list


class ProductoDetail(DetailView):
    model = models.Producto


class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")


class ProductoUpdate(UpdateView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
    form_class = forms.ProductoForm
