from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("personal_list/", views.PersonalList.as_view(), name="personal_list"),
    path("registrar_personal/", views.PersonalCreate.as_view(), name="personal_create"),
    path("personal_delete/<int:pk>/", views.PersonalDelete.as_view(), name="personal_delete"),
    path("personal_update/<int:pk>/", views.PersonalUpdate.as_view(), name="personal_update"),
]
