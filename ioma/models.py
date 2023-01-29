from django.db import models
from django.db.models.signals import post_save
import googlemaps


# Create your models here.

    
class prestadores(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefonos = models.TextField(blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    subdirector = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("prestadores.Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)
    lat = models.FloatField(blank=True, null=True) 
    lon = models.FloatField(blank=True, null=True) 
    geo_parcial = models.BooleanField(blank=True, null=True, default=False,verbose_name ='Geolocalizado')

    def __str__(self):
        return "{} {}".format(self.lat,self.lon)

    class Meta:
        verbose_name = "Clinica"
        verbose_name_plural = "Clinicas"

def update_address_save(sender, instance, created, **kwargs):
    post_save.disconnect(update_address_save, sender=prestadores)
    
    if not instance.direccion:
        instance.direccion = ""
    if instance.direccion:
        address = '{}, {}, {}'.format(instance.direccion, instance.localidad, instance.municipio)
    else: 
        address = '{}, {}'.format(instance.direccion, instance.municipio)
    print(address)
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
    post_save.connect(update_address_save, sender=prestadores)
post_save.connect(update_address_save, sender=prestadores)
  
def get_georef(address):
    gmaps = googlemaps.Client(key='AIzaSyBJzks7JmRyirVz1nCHeYIVT05kpHmQ1qM')
    geocode_result = gmaps.geocode(address)
    return geocode_result


class postas_itinerantes(models.Model):

    TIPO = (
        ('FIJA', 'FIJA'),
        ('INTI', 'ITINERANTE'),
    )

    lugar = models.CharField(max_length=50)
    tipo = models.CharField(max_length=4, choices=TIPO,blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.CASCADE, blank=True, null=True)
    cantidad_de_vacunados = models.CharField(max_length=10,blank=True, null=True)
    fecha_inicio = models.DateField(blank=True)
    fecha_fin = models.DateField(blank=True)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.lugar)

    class Meta:
        verbose_name = "Opetativo"
        verbose_name_plural = "Operativos"



class afiliados(models.Model):
    nombre_y_apellido = models.CharField(max_length=50,blank=True, null=True)
    numero_de_afiliado = models.CharField(max_length=50,blank=True, null=True)
    fecha_de_nacimiento = models.CharField(max_length=50,blank=True, null=True)
    localidades = models.CharField(max_length=50,blank=True, null=True)
    mail = models.CharField(max_length=50,blank=True, null=True)
    tel_fijo= models.CharField(max_length=50,blank=True, null=True)
    celular = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombre_y_apellido)

    class Meta:
        verbose_name = "Afiliado"
        verbose_name_plural = "Afiliados"



