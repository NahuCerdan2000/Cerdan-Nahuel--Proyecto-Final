from django.db import models

# Create your models here.


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  # el nombre de la categoria debe ser unico
    descripcion = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categoria de Productos"

    def __str__(self):
        return self.nombre
