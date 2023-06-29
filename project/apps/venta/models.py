from time import timezone

from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
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


class Venta(models.Model):
    vendedor = models.ForeignKey(Venderdor, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("producto.Producto", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveBigIntegerField()
    precio_total = models.DecimalField(decimal_places=2, max_digits=10, editable=False)
    fecha = models.DateTimeField(default=timezone.now, editable=False)

    def clean(self):
        if self.cantidad > self.producto.cantidad:
            raise ValidationError("No hay suficiente stock para ejecutar la venta")

    def save(self, *args, **kwargs):
        self.precio_total = self.cantidad * self.producto.precio
        super().save(*args, **kwargs)
