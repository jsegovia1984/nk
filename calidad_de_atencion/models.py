from django.db import models

# Create your models here.



class Atencion_de_primer_nivel(models.Model):
    CALIDAD = (
        ('MM', 'MUY MALA'),
        ('M', 'MALA'),
        ('B', 'BUENA'),
        ('MB', 'MUY BUENA'),
    )

    medico = models.ForeignKey("prestadores.PrestadoresdePrimerNivel", on_delete=models.CASCADE)
    agencia = models.ForeignKey("prestadores.Agencia", on_delete=models.CASCADE)
    atencion = models.CharField(max_length=2, choices=CALIDAD)
    afiliado = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField()
    fecha_del_reclamo = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Atencion de primer Nivel"
        verbose_name_plural = "Atencion de primer Nivel"

    def __str__(self):
        return "{}".format(self.medico)


 