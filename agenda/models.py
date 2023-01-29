from django.db import models
from datetime import datetime, timedelta


# Create your models here.

class agenda(models.Model):

    ORG = (
        ('SUB', 'Subsecreatria de DDHH'),
        ('PAM', 'PAMI'),
        ('COE', 'Consejo Escolar'),
        ('ANS', 'ANSES'),
        ('ACU', 'ACUMAR'),
        ('REN', 'RENAPER'),
        ('MIG', 'Migraciones'),
        ('IOM', 'IOMA'),
        ('VAC', 'Vacunate'),
        ('MER', 'Mercado'),
        ('INT', 'Inter-Ministerial'),
    )

    vigente = models.BooleanField(default=True)
    lugar = models.CharField(max_length=50,blank=True, null=False,unique=True, db_column="lugar")
    organismo = models.CharField(max_length=3, choices=ORG)
    direccion = models.CharField(max_length=50,blank=True, null=True)
    responsable = models.ForeignKey("territorio.compañerxs", on_delete=models.PROTECT, blank=True, null=True)
    telefono = models.CharField(max_length=50,blank=True, null=True)
    organizacion = models.ForeignKey("territorio.organizacion", on_delete=models.PROTECT, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.PROTECT, blank=True,null=True)
    usuario = models.CharField(max_length=50,blank=True, null=True)
    fecha = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)
    horas = models.IntegerField(blank=True, null=True, default=1)
    dias = models.IntegerField(blank=True, null=True, default=1)
    descripcion = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
       #self.fecha_fin = self.fecha + timedelta(hours = self.horas)
        self.fecha_fin = self.fecha + timedelta(days = self.dias)
        super().save(*args, **kwargs)
	
    def __str__(self):
        return "{}".format(self.lugar)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agenda"

