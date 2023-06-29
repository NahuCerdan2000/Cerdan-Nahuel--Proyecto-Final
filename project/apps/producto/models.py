from django.db import models
from django.utils import timezone

# Create your models here.


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  # el nombre de la categoria debe ser unico
    descripcion = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categoria de Productos"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, null=True, blank=True, verbose_name="descripción")
    categoria = models.ForeignKey(
        ProductoCategoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="categoria"
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.FloatField()
    fecha_actualizacion = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="fecha de actualización"
    )

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return f"{self.nombre}  ${self.precio} "
