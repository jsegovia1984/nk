from django.db import models


# Create your models here.


class lugar(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    sucursal = models.IntegerField(blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    barrio = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombre + " " + str(self.sucursal))


    
    
class postres(models.Model):
    lugar = models.ForeignKey("lugar", on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    porcion = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    descuento = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=50, blank=True, null=True)
    observacion = models.CharField(max_length=50, blank=True, null=True)
    disponible = models.BooleanField(blank=True, null=True)



