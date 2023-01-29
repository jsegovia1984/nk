from django.db import models

# Create your models here.



class Poligonos(models.Model):
    nombre = models.CharField(max_length=50,blank=True, null=True)
    lat = models.FloatField(blank=True, null=True) 
    lon = models.FloatField(blank=True, null=True) 

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Poligonos"
        verbose_name_plural = "Poligonos"
