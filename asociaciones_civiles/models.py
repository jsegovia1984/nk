from django.db import models
from django.db.models.signals import post_save
import googlemaps

# Create your models here.

class tipo_ac(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Tipo de Asociacion civil"
        verbose_name_plural = "Tipos de Asociaciones civiles"



class situacion_documental(models.Model):
    nombre = models.CharField(max_length=50)
  
    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Situacion Documental"
        verbose_name_plural = "Situaciones Documentales"

class proceso(models.Model):
    nombre = models.CharField(max_length=50)
   
    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Proceso"
        verbose_name_plural = "Procesos"


   



class asociaciones_civiles(models.Model):
    GRADO = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    nombre = models.CharField(max_length=100,)
    foto = models.ImageField(blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.PROTECT, blank=True, null=True)
    tipo = models.ForeignKey("tipo_ac", on_delete=models.PROTECT, blank=True, null=True)
    grado_de_relacion = models.CharField(max_length=2,choices=GRADO, blank=True, null=True)
    Inscripta = models.BooleanField(default=True)
    numero =  models.CharField(max_length=25, blank=True, null=True)
    situacion_documental = models.ForeignKey("situacion_documental", on_delete=models.PROTECT, blank=True, null=True)
    proceso = models.ForeignKey("proceso", on_delete=models.PROTECT, blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)
    recursos_y_actividades = models.TextField(blank=True, null=True)
    organizacion = models.ForeignKey("territorio.organizacion", on_delete=models.PROTECT, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True) 
    lon = models.FloatField(blank=True, null=True) 
    geo_parcial = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Asociacion civil"
        verbose_name_plural = "Asociciones civiles"

def update_address_asociviles_save(sender, instance, created, **kwargs):
    post_save.disconnect(update_address_asociviles_save, sender=asociaciones_civiles)
    if not instance.direccion:
        instance.direccion = ""
    if instance.direccion:
        address = '{}, {}, {}'.format(instance.direccion, instance.localidad, 'la matanza')
    else: 
        address = '{}, {}'.format(instance.direccion, 'la matanza')
    geo = get_georef(address)
    print(geo)
    if len(geo)!=0:
        if 'geometry' in geo[0]:
            instance.lat = geo[0]['geometry']['location']['lat']
            instance.lon = geo[0]['geometry']['location']['lng']
        if 'partial_match' in geo[0]:
            instance.lat = 0.0
            instance.lon = 0.0
            instance.geo_parcial= True
        else:
            instance.geo_parcial= False
            instance.save()
    post_save.connect(update_address_asociviles_save, sender=asociaciones_civiles)
post_save.connect(update_address_asociviles_save, sender=asociaciones_civiles)


def get_georef(address):
    gmaps = googlemaps.Client(key='AIzaSyBJzks7JmRyirVz1nCHeYIVT05kpHmQ1qM')
    geocode_result = gmaps.geocode(address)
    return geocode_result
