from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# Create your models here.

class becarios(models.Model):
    TAREA = (
        ('PRE', 'PRE-VACUNACION'),
        ('TRI', 'TRIANGE'),
        ('LIM', 'LIMPIEZA'),
        ('ADM', 'ADMINISTRATIVO/A'),
        ('COR', 'COORDINADOR/A'),
        ('NOC', 'NOCHE'),
        ('VAC', 'VACUNADOR/A'),
        ('LOG', 'LOGISTICA'),

    )
    
    HORARIO = (
        ('LAV', 'LUNES A VIERNES'),
        ('FIN', 'FINES DE SEMANA'),
        ('LAL', 'LUNES A LUNES'),
        ('NOC', 'NOCHE'),
    )

    TURNO = (
        ('M', 'MAÑANA'),
        ('T', 'TARDE'),
        ('N', 'NOCHE'),
        ('MT', '12 HORAS'),
    )


    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    posta = models.ForeignKey("postas", on_delete=models.PROTECT, blank=True, null=True)
    tarea = models.CharField(max_length=5,choices=TAREA,blank=True, null=True)
    organizacion = models.ForeignKey("territorio.organizacion", on_delete=models.PROTECT, blank=True, null=True)
    turno = models.CharField(max_length=2,choices=TURNO,blank=True, null=True)
    carga_horaria = models.CharField(max_length=5,choices=HORARIO, blank=True, null=True)
    region= models.BooleanField(default=False)
    usuario = models.CharField(max_length=50,blank=True, null=True)

  
    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Becario"
        verbose_name_plural = "Becarios"

class postas(models.Model):

    lugar = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.PROTECT, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.lugar)

    class Meta:
        verbose_name = "posta"
        verbose_name_plural = "postas"



class asistencia(models.Model):

    ASISTENCIA = (
        ('P', 'PRESENTE'),
        ('A', 'AUSENTE'),
    )

    fecha= models.DateField(blank=True, null=True,default=timezone.now)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=1,choices=ASISTENCIA ,blank=True, null=True)
    certificado = models.BooleanField(default=False)
    horario_ingreso= models.TimeField(blank=True, null=True)
    horario_salida= models.TimeField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    posta = models.CharField(max_length=50,blank=True, null=True)
    organizacion = models.CharField(max_length=50,blank=True, null=True)
    usuario = models.CharField(max_length=50,blank=True, null=True)


    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"


my_store = FileSystemStorage(location='/var/www/sgpami.ar/sgpami/media/turnera')

class conteo_de_vacunas(models.Model):
    posta = models.ForeignKey("postas", on_delete=models.PROTECT)
    fecha= models.DateField(blank=True, null=True,default=timezone.now)
    turnera = models.FileField(blank=True, null=True,storage=my_store) 
    cantidad_turnera = models.IntegerField(blank=True, null=True)
    faltas = models.IntegerField(blank=True, null=True)
    espontanea = models.IntegerField(blank=True, null=True)
    primera_dosis = models.IntegerField(blank=True, null=True)
    segunda_dosis = models.IntegerField(blank=True, null=True)
    total_vacunados = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=50,blank=True, null=True)



    def __str__(self):
        return "{}".format(self.posta)

    class Meta:
        verbose_name = "Conteo de Turnos diarios"
        verbose_name_plural = "Conteo"




class stock_de_vacunas(models.Model):
    LAB = (
        ('A', 'ASTRASENECA'),
        ('S', 'SPUNK V'),
    )

    FORMATO = (
        ('M', 'MODOSIS'),
        ('D', '10'),
    )

    TIPO = (
        ('1', 'PRIMERA DOSIS'),
        ('2', 'SEGUNDA DOSIS'),
        ('3', 'NO APLICA'),
    )


    posta = models.ForeignKey("postas", on_delete=models.PROTECT)
    fecha= models.DateField(blank=True, null=True,default=timezone.now)
    laboratorio = models.CharField(max_length=2,choices=LAB,blank=True, null=True) 
    tipo = models.CharField(max_length=2,choices=TIPO,blank=True, null=True)
    formato = models.CharField(max_length=2,choices=FORMATO,blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=50,blank=True, null=True)

   
    def __str__(self):
        return "{}".format(self.posta)

    class Meta:
        verbose_name = "Vacuna"
        verbose_name_plural = "Stock de Vacunas"


