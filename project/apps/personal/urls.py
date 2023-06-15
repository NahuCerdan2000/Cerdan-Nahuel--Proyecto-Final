from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("añadir_personal/", views.añadir_personal, name="añadir_personal"),
]
