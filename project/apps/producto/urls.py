import stat

from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("producto_categoria_list/", views.ProductoCategoriaList.as_view(), name="producto_categoria_list"),
    path("producto_categoria_create/", views.ProductoCategoriaCreate.as_view(), name="producto_categoria_create"),
    path(
        "producto_categoria_delete/<int:pk>/",
        views.ProductoCategoriaDelete.as_view(),
        name="producto_categoria_delete",
    ),
    path(
        "producto_categoria_update/<int:pk>/",
        views.ProductoCategoriaUpdate.as_view(),
        name="producto_categoria_update",
    ),
    path(
        "producto_categoria_detail/<int:pk>/",
        views.ProductoCategoriaDetail.as_view(),
        name="producto_categoria_detail",
    ),
    path("producto/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("producto/list/", views.ProductoList.as_view(), name="producto_list"),
    path("producto/create/", staff_member_required(views.ProductoCreate.as_view()), name="producto_create"),
    path("producto/delete/<int:pk>", staff_member_required(views.ProductoDelete.as_view()), name="producto_delete"),
    path("producto/update/<int:pk>", staff_member_required(views.ProductoUpdate.as_view()), name="producto_update"),
]
