from django.db import models

# Create your models here.


class Centros(models.Model):
    PERSONERIA = (
        ('R', 'Regularizar/Normalizar'),
        ('C', 'Construir'),
        ('T', 'En Tramite'),
        ('N', 'No Tiene'),
        ('B', 'En Regla'),

    )
    incluido = models.BooleanField(default=True)
    subsidio = models.BooleanField(default=True)
    sap = models.CharField(max_length=20, blank=True, null=True)
    personeria_Juridica = models.CharField(max_length=1, choices=PERSONERIA, blank=True, null=True)
    centro = models.CharField(max_length=50, blank=True, null=True)
    CUIT = models.CharField(max_length=20, blank=True, null=True)
    presidente = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    agencia = models.ForeignKey("prestadores.Agencia", on_delete=models.CASCADE, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("prestadores.Municipio", on_delete=models.CASCADE, blank=True, null=True)
    relacion = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.centro)

    class Meta:
        verbose_name = "Centro de Jubilado"
        verbose_name_plural = "Centros de Jubilados"

class Subsidios(models.Model):
    centro = models.ForeignKey("Centros", on_delete=models.CASCADE, blank=True, null=True)
    monto = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.TextField(max_length=50, blank=True, null=True)
  
    def __str__(self):
        return "{}".format(self.centro)

    class Meta:
        verbose_name = "subsidio"
        verbose_name_plural = "subsidios"
