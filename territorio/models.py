from django.db import models
from django.db.models.signals import post_save
import googlemaps
# Create your models here.

class organizacion(models.Model):
    nombre = models.CharField(max_length=50,)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Organizacion"
        verbose_name_plural = "Organizaciones"


class compañerxs(models.Model):
    nombre = models.CharField(max_length=50,blank=True, null=True)
    apellido = models.CharField(max_length=50,blank=True, null=True)
    dni = models.CharField(max_length=50,blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    barrio = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.PROTECT, blank=True, null=True)
    organizacion = models.ForeignKey("organizacion", on_delete=models.PROTECT, blank=True, null=True)
    afiliado_al_pj = models.BooleanField(blank=True, null=True,default=False) 
    trabaja_en_el_estado = models.BooleanField(blank=True, null=True,default=False) 
    lat = models.FloatField(blank=True, null=True) 
    lon = models.FloatField(blank=True, null=True) 
    geo_parcial = models.BooleanField(blank=True, null=True, default=False,verbose_name ='Geolocalizado')


    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

    class Meta:
        verbose_name = "compañerx"
        verbose_name_plural = "Compañerxs"


class Unidades_Basicas(models.Model):
    nombre = models.CharField(max_length=50,blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    barrio = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.PROTECT, blank=True, null=True)
    organizacion = models.ForeignKey("organizacion", on_delete=models.PROTECT, blank=True, null=True)
    casa_operativa = models.BooleanField(blank=True, null=True,default=False) 
    lat = models.FloatField(blank=True, null=True) 
    lon = models.FloatField(blank=True, null=True) 
    geo_parcial = models.BooleanField(blank=True, null=True, default=False,verbose_name ='Geolocalizado')

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Unidad Basica"
        verbose_name_plural = "Unidad Basica"

def update_address_ub_save(sender, instance, created, **kwargs):
    post_save.disconnect(update_address_ub_save, sender=Unidades_Basicas)
    if not instance.direccion:
        instance.direccion = ""
    if instance.direccion:
        address = '{}, {}, {}'.format(instance.direccion, instance.localidad, 'la matanza')
    else: 
        address = '{}, {}'.format(instance.direccion, 'la matanza')
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
    post_save.connect(update_address_ub_save, sender=Unidades_Basicas)
post_save.connect(update_address_ub_save, sender=Unidades_Basicas)



class Instituciones(models.Model):
    organismo = models.ForeignKey("casos_de_gestion.Organismo",on_delete=models.PROTECT,)
    jefe = models.CharField(max_length=50, blank=True, null=True)
    sede = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("prestadores.Localidad", on_delete=models.PROTECT, blank=True, null=True)
    municipio = models.ForeignKey("prestadores.Municipio", on_delete=models.PROTECT, blank=True, null=True)
    telefono= models.CharField(max_length=50, blank=True, null=True)
    mail = models.EmailField(max_length=50, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True) 
    lon = models.FloatField(blank=True, null=True) 
    geo_parcial = models.BooleanField(blank=True, null=True, default=False,verbose_name ='Geolocalizado')

    def __str__(self):
        return "{}".format(self.organismo)
   
    class Meta:
        verbose_name = "Institucion"
        verbose_name_plural = "Instituciones"

def update_address_save(sender, instance, created, **kwargs):
    post_save.disconnect(update_address_save, sender=Instituciones)
    if not instance.direccion:
        instance.direccion = ""
    if instance.direccion:
        address = '{}, {}, {}'.format(instance.direccion, instance.localidad, 'la matanza')
    else: 
        address = '{}, {}'.format(instance.direccion, 'la matanza')
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
    post_save.connect(update_address_save, sender=Instituciones)
post_save.connect(update_address_save, sender=Instituciones)
  
def get_georef(address):
    gmaps = googlemaps.Client(key='AIzaSyBJzks7JmRyirVz1nCHeYIVT05kpHmQ1qM')
    geocode_result = gmaps.geocode(address)
    return geocode_result

class beneficios_anses(models.Model):
    nombre = models.CharField(max_length=20,blank=True, null=True)
   
    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Beneficio"
        verbose_name_plural = "Beneficios de Anses"

class Cuadricula(models.Model):

    VACUNA = (
        ('0', 'NO'),
        ('1', 'Si, con la Primera dosis'),
        ('2', 'Si, con la Segunda dosis'),
    )									
    PARTIDOS = (
        ('FT', 'Frente de Todxs'),
        ('JXC', 'Juntos por el Cambio'),
        ('AL', 'Avanza Libertad'),
        ('CF', 'Consenso Federal'),
        ('FIT', 'Frente de Izquierda'),
        ('NOS', 'Nos'),
        ('OTR', 'Otro'),
        ('NIN', 'Ninguno'),

    )
    NACIONALIDAD = (
        ('ARG', 'ARGENTINO/A'),
        ('BOL', 'BOLIVINO/A'),
        ('URU', 'URUGUAYO/A'),
        ('PAR', 'PARAGUAYO/A'),
        ('BRA', 'BRASILERO/A'),
        ('CHI', 'CHILENO/A'),
        ('OTRO', 'OTRX'),
    )

    PRESTADOR = (
        ('SPRI', 'Salud Privada'),
        ('PAMI', 'PAMI'),
        ('IOMA', 'IOMA'),
        ('INCL', 'INCLUIR'),
        ('OTRA', 'OTRA'),
    )

    fecha = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    usuario = models.CharField(max_length=50,blank=True, null=True)
    barrio = models.CharField(max_length=50,blank=True, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    trabajo_registrado = models.BooleanField(blank=True, null=True,verbose_name = "¿Tiene trabajo registrado?")
    nacionalidad = models.CharField(max_length=4, choices=NACIONALIDAD,blank=True, null=True)
    edad = models.CharField(max_length=5,blank=True, null=True)
    telefono = models.CharField(max_length=50,blank=True, null=True)
    menores = models.CharField(max_length=5,blank=True, null=True,verbose_name = "¿Cuantos menores viven en el hogar?")
    mayores = models.CharField(max_length=5,blank=True, null=True,verbose_name = "¿Cuantos mayores viven en el hogar?")
    discapacitados = models.BooleanField(blank=True, null=True,verbose_name = "¿Hay alguna persona discapacitada?")
    vacunacion = models.CharField(max_length=1, choices=VACUNA,blank=True, null=True)
    inscriptx_vacuna = models.BooleanField(blank=True, null=True,verbose_name = "¿Esta Incriptx a la vacuna contra el COVID-19?")
    desea_inscribirse = models.BooleanField(blank=True, null=True,help_text="Comentar sobre la mesa de Vacunate",verbose_name = "¿Desea Inscribirse?")
    cobran_correctamente = models.BooleanField(blank=True, null=True,help_text="¿Cobran las prestaciones de ANSES correctamente?")
    beneficios = models.ManyToManyField("beneficios_anses",help_text="Recordar que mayores de 60 (mujeres) y 65 (hombres) con algunos años de aportes se pueden jubilar, Si tiene hijxs puede cobrar AUH (Si no estan registradxs lxs progenitorxs) y Suaf (Si estan registradxs)")
    otros = models.CharField(max_length=50,blank=True, null=True)
    cobertura_de_salud = models.BooleanField(blank=True, null=True, verbose_name = "¿Tiene Cobertura de salud?")
    prestador = models.CharField(max_length=4, choices=PRESTADOR,blank=True, null=True)
    inconveniente = models.TextField(blank=True, null=True,verbose_name = "¿Que inconveniente Tiene?")
    DNI = models.BooleanField(blank=True, null=True,verbose_name = "¿Tiene actualmente DNI?")
    tuvo_DNI_alguna_vez = models.BooleanField(blank=True, null=True,verbose_name = "¿Tuvo alguna vez DNI?")
    turno = models.BooleanField(blank=True, null=True,verbose_name = "¿Necesita un turno por renovacion o por emision de un nuevo ejemplar?")
    prestacion_alinentaria = models.BooleanField(blank=True, null=True,help_text="¿Reciben prestacion alimentaria o asisten a algun comedor o merendero?")
    caso_de_gestion = models.BooleanField(blank=True, null=True,verbose_name = "¿hay un caso de gestion a resolver?",default=False)
    conoces_la_linea_144 = models.BooleanField(blank=True, null=True, help_text="Existe el programa ACOMPAÑAR, el cual buscar fortalecer economicamente a las victimas que sufren violencia de genero",verbose_name = "¿Sabias que en caso de visualizar un caso de violencia de genero podes llamar al 144?")
    mejoras = models.TextField(blank=True, null=True,verbose_name = "¿Qué crees que se puede mejorar del barrio?")
    politica1 = models.TextField(blank=True, null=True,verbose_name = "¿Alguna medida del gobierno le parecio buena? ¿Cuál/es?")
    politica2 = models.TextField(blank=True, null=True,verbose_name = "¿Alguna medida del gobierno le parecio mala? ¿Cuál/es?")
    preferencia = models.CharField(max_length=3, choices=PARTIDOS,blank=True, null=True,verbose_name="¿Se refencia con algún partido político?¿Cuál?")
    observaciones = models.TextField(blank=True, null=True)
					

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Encuestado"
        verbose_name_plural = "Cuadriculas"

