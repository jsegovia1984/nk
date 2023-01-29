from django.db import models



class Informes(models.Model):
    organismo = models.ForeignKey("casos_de_gestion.Organismo", on_delete=models.PROTECT, blank=True, null=True)
    fecha= models.DateField(blank=True, null=True)    
    archivo = models.FileField(blank=True, null=True) 
    usuario = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.organismo)

    class Meta:
        verbose_name = "Informes de gestion"
        verbose_name_plural = "Informes de gestion"
