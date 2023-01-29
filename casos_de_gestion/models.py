
from django.db import models
from django.db.models.signals import post_save
import googlemaps

# Create your models here.


class Region(models.Model):
    nombre = models.CharField(max_length=20,primary_key=True)
    descripcion = models.TextField()

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Region"


class Organismo(models.Model):
    nombre = models.CharField(max_length=50)
 
    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Organismo"
        verbose_name_plural = "Organismos"


class Casos(models.Model):
    caso_resuelto = models.BooleanField(default=True)
    interministerial = models.BooleanField(default=False)
    lugar_operativo = models.ForeignKey("agenda.agenda", to_field="lugar",  db_column="lugar", on_delete=models.PROTECT, blank=True, null=True,limit_choices_to={'vigente': True},)
    apellido = models.CharField(max_length=50,)
    nombre = models.CharField(max_length=50,)
    dni = models.IntegerField(blank=True, null=True)
    domicilio = models.CharField(max_length=120, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.PROTECT, blank=True, null=True)
    contacto = models.CharField(max_length=30, blank=True, null=True)
    metodo_de_entrada = models.CharField(max_length=30, blank=True, null=True)
    organismo =  models.ForeignKey("Organismo", on_delete=models.PROTECT,blank=True, null=True)
    tipo_de_Tramite= models.CharField(max_length=40, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_de_entrada = models.DateField(blank=True, null=True)    
    fecha_de_resolucion = models.DateField(blank=True, null=True)
    persona_de_Seguimiento=  models.CharField(max_length=25, blank=True, null=True)
    region = models.ForeignKey("Region", on_delete=models.PROTECT, blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    organizacion = models.CharField(max_length=50,blank=True, null=True)
    lat = models.FloatField(blank=True, null=True) 
    lon = models.FloatField(blank=True, null=True) 
    geo_parcial = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Casos de gestion"
        verbose_name_plural = "Casos de gestion"

def update_address_save(sender, instance, created, **kwargs):
    if instance.geo_parcial != False:
        post_save.disconnect(update_address_save, sender=Casos)
        if not instance.domicilio:
            instance.domicilio = ""

        if instance.localidad:
            address = '{}, {}, {}'.format(instance.domicilio, instance.localidad, 'la matanza')
        else: 
            address = '{}, {}'.format(instance.domicilio, 'la matanza')
        print (address)
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
        post_save.connect(update_address_save, sender=Casos)
    post_save.connect(update_address_save, sender=Casos)

def get_georef(address):
    gmaps = googlemaps.Client(key='AIzaSyBJzks7JmRyirVz1nCHeYIVT05kpHmQ1qM')
    geocode_result = gmaps.geocode(address)
    return geocode_result


class Casos_interminitserial(Casos):
    class Meta:
        proxy = True
        verbose_name = "Casos de Interministeriles"
        verbose_name_plural = "Casos de Interministeriales"


    def __str__(self):
        return "{}".format(self.id)

 
