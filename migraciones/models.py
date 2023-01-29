from django.db import models
from django.db.models.signals import post_save
import googlemaps

# Create your models here.
class nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nacionalidad,)

    class Meta:
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidades"



class casos(models.Model):
    interministerial = models.BooleanField(default=False)
    fecha_de_toma = models.DateField(blank=False, null=False) 
    modo_de_toma = models.CharField(max_length=50, blank=False, null=False)
    lugar_de_toma = models.CharField(max_length=50, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    fecha_de_nacimiento = models.DateField(blank=False, null=False) 
    nacionalidad = models.ForeignKey("nacionalidad", on_delete=models.PROTECT, blank=False, null=False,)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.PROTECT, blank=False, null=False,related_name="CasosMigraciones",)
    telefono= models.CharField(max_length=30, blank=False, null=False)
    mail = models.EmailField(max_length = 254, blank=True, null=True)
    dni_cedula = models.CharField(max_length=15, blank=False, null=False)
    expediente = models.CharField(max_length=25, blank=False, null=False)
    estado_del_tramite = models.CharField(max_length=50,blank=False, null=False)
    usuario = models.CharField(max_length=50,blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True) 
    agente =  models.CharField(max_length=25, blank=False, null=False)
    lat = models.FloatField(blank=True, null=True) 
    lon = models.FloatField(blank=True, null=True) 
    geo_parcial = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        verbose_name = "Caso"
        verbose_name_plural = "Casos"




def update_address_save(sender, instance, created, **kwargs):
    post_save.disconnect(update_address_save, sender=casos)
    if not instance.direccion:
        instance.direccion = ""
    if instance.direccion:
        address = '{}, {}, {}'.format(instance.direccion, instance.localidad, 'la matanza')
    else: 
        address = '{}, {}'.format(instance.direccion, 'la matanza')
    geo = get_georef(address)

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
        post_save.connect(update_address_save, sender=casos)
post_save.connect(update_address_save, sender=casos)
  
def get_georef(address):
    gmaps = googlemaps.Client(key='AIzaSyBJzks7JmRyirVz1nCHeYIVT05kpHmQ1qM')
    geocode_result = gmaps.geocode(address)
    return geocode_result
