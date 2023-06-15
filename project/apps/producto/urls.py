from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("producto_categoria_list", views.producto_categoria_list, name="producto_categoria_list"),
    path("producto_categoria_create", views.producto_categoria_create, name="producto_categoria_create"),
]
