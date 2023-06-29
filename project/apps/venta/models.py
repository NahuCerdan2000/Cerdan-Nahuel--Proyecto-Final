from django.contrib.auth.models import User
from django.db import models
from personal.models import Personal

# Create your models here.


class Venderdor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    celular = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)


class Meta:
    verbose_name = "vendedor"
    verbose_name_plural = "vendedores"


def __str__(self):
    return f"{self.usuario}"


# Create your models here.


class Venderdor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    celular = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)


class Meta:
    verbose_name = "vendedor"
    verbose_name_plural = "vendedores"


def __str__(self):
    return f"{self.user.username}"
