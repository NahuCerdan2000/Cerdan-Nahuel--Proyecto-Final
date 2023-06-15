from django.db import models


# Create your models here.
class Sector(models.Model):
    nombre_sector = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre_sector


class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nombre
