from territorio.models import Instituciones,Unidades_Basicas
from asociaciones_civiles.models import asociaciones_civiles
from ioma.models import prestadores
from casos_de_gestion.models import Casos
from .models import Poligonos
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.shortcuts import render, loader
from django.http import HttpResponse, JsonResponse
import json
import os
from django.contrib.gis.geos import Polygon, Point, MultiPoint, GeometryCollection, MultiPolygon
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import ListView


class ACivilesdetalle(ListView):
    model = asociaciones_civiles
    template_name = 'asociaciones_civiles_detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        iddetail = self.request.GET.get('id') 
        context['institucion'] =  asociaciones_civiles.objects.get(pk=iddetail)
        return context


class MapaDetailViewACiviles(ListView):
    model = asociaciones_civiles
    template_name = 'asociaciones_civiles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asociaciones_civiles'] =  asociaciones_civiles.objects.all()
        return context



class MapaDetailView(ListView):
    model = Instituciones
    template_name = 'mapa-instituciones.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Instituciones'] =  Instituciones.objects.exclude(organismo=28)
        context['poli'] =  Poligonos.objects.all()
        return context


class MapaDetailViewIOMA(ListView):
    model = prestadores
    template_name = 'mapa-ioma-prestadores.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['prestadores'] = prestadores.objects.all()
        return context

class MapaDetailViewBasicas(ListView):
    model = Unidades_Basicas
    template_name = 'mapa-basicas.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['basicas'] = Unidades_Basicas.objects.all()
        return context

class MapaDetailViewCasos(ListView):
    model = Casos
    template_name = 'mapa-casos.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['Casos'] = Casos.objects.all().order_by('organismo')
        return context





def map_json(request):    
    lote_mapas = []
    lote_mapas.append((1,'aldo_bonzi.geojson'),)
    lote_mapas.append((2,'ciudad_evita.geojson'),)
    lote_mapas.append((3,'gonzalez_catan.geojson'),)
    lote_mapas.append((4,'gregorio_de_laferrere.geojson'),)
    lote_mapas.append((5,'isidro_casanova.geojson'),)
    lote_mapas.append((6,'la_tablada.geojson'),)
    lote_mapas.append((7,'lomas_del_mirador.geojson'),)
    lote_mapas.append((8,'rafael_castillo.geojson'),)
    lote_mapas.append((9,'ramos_mejia.geojson'),)
    lote_mapas.append((10,'san_justo.geojson'),)
    lote_mapas.append((11,'tapiales.geojson'),)
    lote_mapas.append((12,'veinte_de_junio.geojson'),)
    lote_mapas.append((13,'villa_celina.geojson'),)
    lote_mapas.append((14,'villa_luzuriaga.geojson'),)
    lote_mapas.append((15,'villa_madero.geojson'),)
    lote_mapas.append((16,'virrey_del_pino.geojson'),)

    json_data = '{ "type": "FeatureCollection", "features": [' 
    for map in lote_mapas:
        loc = Localidad.objects.get(pk=map[0])
        # Ordernar por "pk" es mucho muy importante, porque sino crashea ya que toma coordenadas azarozas
        poly = Polygon([ (c.latitud, c.longitud) for c in loc.poligono.all().order_by('pk')])
        multipoly = MultiPolygon(poly)
        gc = GeometryCollection(multipoly)

        # Propiedad a graficar
        personas = loc.persona_set.all()
        personas |= loc.localidadsecuestro_set.all()
        personas |= loc.localidadasesinato_set.all()
        personas |= loc.localidadrestos_set.all()
        personas = personas.distinct()

        cant_mujeres = personas.filter(genero=Genero.objects.filter(nombre="Femenino").first()).count()
        cant_varones = personas.filter(genero=Genero.objects.filter(nombre="Masculino").first()).count()

        propiedades = ''
        propiedades = propiedades + '"desaparecidos": ' + str(personas.count())
        propiedades = propiedades + ', "localidad": "' + str(loc.nombre) + '"'
        propiedades = propiedades + ', "vivia_en": "' + str(loc.persona_set.count()) + '"'
        propiedades = propiedades + ', "secuestrado_en": "' + str(loc.localidadsecuestro_set.count())  + '"'
        propiedades = propiedades + ', "asesinado_en": "' + str(loc.localidadasesinato_set.count())  + '"'
        propiedades = propiedades + ', "restos_en": "' + str(loc.localidadrestos_set.count())  + '"'
        propiedades = propiedades + ', "cant_mujeres": "' + str(cant_mujeres)  + '"'
        propiedades = propiedades + ', "cant_varones": "' + str(cant_varones)  + '"'

        json_data = json_data + '{"type": "GeometryCollection", "properties": {  '+ propiedades+  '},"geometries": ['
        # Agrego las geometrias al geojson, si es el ultimo no le pongo coma
        if not map[0] == 16:
            json_data = json_data + str(multipoly.geojson) + "]},"  
        else:
            json_data = json_data + str(multipoly.geojson) + "]}"

    json_data = json_data + ' ]}'
    data = str(json_data)
    data_posta = data.replace('\"','"')
    data_json = json.loads(data_posta)

    # return JsonResponse(data_posta, safe=False)
    return JsonResponse(data_json)
