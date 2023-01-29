from django.db import models

# Create your models here.

class Geriatrico(models.Model):

    TIPO = (
        ('E', 'RAM'),
        ('N', 'RAMP'),
        ('C', 'CENTRO DE DIA'),


    )
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    sap = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=True, null=True)
    CUIT = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    cantidad_de_afiliados = models.CharField(max_length=20, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("prestadores.Municipio", on_delete=models.CASCADE, blank=True, null=True)
    conveniado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Geriatrico"
        verbose_name_plural = "Geriatricos"


class Facturacion(models.Model):
    TIPO = (
        ('E', 'RAM'),
        ('N', 'RAMP'),
        ('C', 'CENTRO DE DIA'),
    )

    Fecha_de_facturacion = models.DateField()
    Lugar = models.ForeignKey("Geriatrico", on_delete=models.CASCADE, blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO)
    Monto = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.Lugar)

    class Meta:
        verbose_name = "Facturacion"
        verbose_name_plural = "Facturacion"
