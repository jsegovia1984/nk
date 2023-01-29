from django.contrib import admin
from django.contrib.auth.models import User, Group

# exportar e importar
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME


# Modelos:
from casos_de_gestion.models import Casos
from .models import agenda

from django.http import FileResponse,HttpResponse
from pathlib import Path
import os
from fpdf import FPDF
import calendar


from datetime import datetime
import datetime


def format_fecha(fecha):
    """
	Formatear fecha actual de modo que su formato quede como:
	"19 de Diciembre del 2018"
"""
#Diccionarios de días y meses
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    mes = meses.get(fecha.month)
    fecha = "{} de {} del {}".format(fecha.day, mes, fecha.year)
    return str(fecha)

# Register your models here.
def Informe(self, request, queryset):
    hoy = format_fecha(datetime.datetime.now())
    BASE_DIR = Path(__file__).resolve().parent.parent
    target = os.path.join(BASE_DIR, 'media', 'pdfs') + '/example.pdf'
    hearder = os.path.join(BASE_DIR, 'media') + '/cabecera.jpeg'

    Casosdegestion=Casos.objects.filter(interministerial=True)
    informe=FPDF()
    informe.add_page()
    informe.set_xy(0, 0)
    informe.image(hearder, 0, 0,)
    informe.set_font("Arial","", size=10)

    for i in range(5):
        informe.cell(40, 10," ",0,1,'C')

    informe.image(hearder, 0, 0,)
    informe.cell(185, 10,hoy,0,0,'R')


    for inter in queryset.filter(organismo='INT'):
        fecha_i=inter.fecha
        fecha_f=inter.fecha_fin 
        localidadinter= str(inter.localidad)
        lugar = inter.lugar
        #fecha_de_entrada__range=[fecha_i, fecha_f]
        renaper_count = Casosdegestion.filter(lugar_operativo__lugar=lugar, organismo__nombre='RENAPER').count()
        pami_count = Casosdegestion.filter(lugar_operativo__lugar=lugar,organismo__nombre='PAMI').count()
        anses_count = Casosdegestion.filter(lugar_operativo__lugar=lugar,organismo__nombre='ANSES').count()
        ioma_count = Casosdegestion.filter(lugar_operativo__lugar=lugar,organismo__nombre='IOMA').count()
        migra_count = Casosdegestion.filter(lugar_operativo__lugar=lugar,organismo__nombre='MIGRACIONES').count()
        desfensoria_count = Casosdegestion.filter(lugar_operativo__lugar=lugar,organismo__nombre='DEFENSORIA').count()
        total_count = Casosdegestion.filter(lugar_operativo__lugar=lugar).count()
        
        if int(total_count) != 0:
            informe.cell(40, 10," ",0,1,'C')
        
            informe.cell(40, 10,"   LUGAR: " + lugar + ' (' + localidadinter + ')',0,1,'L') #primer digito, 0 sin recuadro, 1 con recuadro. Segundo paramentro 1 salto de linea, 0 desplazamiento en horizontal
            informe.cell(40, 10,"   FECHA: " + format_fecha(fecha_i) + ' - ' + format_fecha(fecha_f),0,1,'L') #primer digito, 0 sin recuadro, 1 con recuadro. Segundo paramentro 1 salto de linea, 0 desplazamiento en horizontal
         
            informe.cell(40, 10,"RENAPER: " + str(renaper_count),1,0,'C')
            informe.cell(40, 10,"PAMI: " + str(pami_count),1,0,'C')
            informe.cell(40, 10,"ANSES: " + str(anses_count),1,1,'C')
            informe.cell(40, 10,"IOMA: " + str(ioma_count),1,0,'C')
            informe.cell(40, 10,"MIGRACIONES: " + str(migra_count),1,0,'C')
            informe.cell(40, 10,"DEFENSORIA: " + str(desfensoria_count),1,0,'C')
            informe.cell(40, 10,"TOTAL: " + str(total_count),1,1,'C')
            informe.cell(40, 10,"",0,1,'C')
            
        
            if total_count!=0:
                pp=round(100 * pami_count / total_count,2)
                rp=round(100 * renaper_count / total_count ,2)
                ip=round(100 * ioma_count / total_count,2)
                dp=round(100 * desfensoria_count / total_count,2)
                ap=round(100 * anses_count / total_count,2)
                mp=round(100 * migra_count / total_count,2)
                rotulos='PAMI(' + str(pp) +'%)' + '|RENAPER(' + str(rp) +'%)' +'|IOMA(' + str(ip) +'%)' + '|DEFENSORIA(' + str(dp) +'%)' + '|ANSES(' + str(ap) +'%)' + '|MIGRACIONES(' + str(mp) +'%)'
                informe.image('https://chart.googleapis.com/chart?cht=p&chd=t:' + str(pp) +',' + str(rp) + ',' + str(ip) +',' + str(dp) + ',' + str(ap) +',' + str(mp) + '&chs=500x150&chl=' + rotulos,)
        
      
    informe.output(target)
        
    file = open(target, 'rb')
      
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename=Informe_Interministerial.pdf'  
    return response



def imprimir_listado(self, request, queryset):
    '''
    imprime el listado de interminiteriales en cero 
    '''

   # agenda_inter = agenda.objects.all().filter(organismo='INT') 

    hoy = format_fecha(datetime.datetime.now())
    BASE_DIR = Path(__file__).resolve().parent.parent

    target = os.path.join(BASE_DIR, 'media', 'pdfs') + '/example.pdf'
    hearder = os.path.join(BASE_DIR, 'media') + '/cabecera.jpeg'

    Casosdegestion=Casos.objects.filter(interministerial=True)
    informe=FPDF()
    informe.add_page()
    informe.set_xy(0, 0)
    informe.image(hearder, 0, 0,)
    informe.set_font("Arial","", size=10)


    for i in range(5):
        informe.cell(40, 10," ",0,1,'C')

    informe.image(hearder, 0, 0,)

    informe.cell(185, 10,hoy,0,1,'R')

    informe.set_font("Arial","B", size=15)

    informe.cell(40, 10,"  LISTADO DE INTERMINISTERIALES SIN CARGA: ",0,1,'L') #primer digito, 0 sin recuadro, 1 con recuadro. Segundo paramentro 1 salto de linea, 0 desplazamiento en horizontal

    informe.set_font("Arial","", size=10)

   # for inter in queryset.filter(organismo='INT'):

    for inter in queryset:

        
        lugar = inter.lugar
        total_count = Casosdegestion.filter(lugar_operativo__lugar=lugar).count()

        if total_count==0:
            informe.cell(40, 10,"   LUGAR: " + lugar  + ", TOTAL: " + str(total_count),0,1,'L') #primer digito, 0 sin recuadro, 1 con recuadro. Segundo paramentro 1 salto de linea, 0 desplazamiento en horizontal


    informe.output(target)
        
    file = open(target, 'rb')
      
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename=listado_interministeriales.pdf'  
    return response



class AgendaResource(resources.ModelResource):
    class Meta:
        model = agenda


@admin.register(agenda)
class agendaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('id','organismo', 'lugar','vigente','fecha','organizacion','responsable')
    autocomplete_fields = ('responsable',)
    search_fields = ['descripcion','lugar']
    resource_class = AgendaResource
    actions = [Informe,imprimir_listado]
    change_list_template ="admin/agenda/agenda/change_list.html"
    fieldsets = (
        ('Agenda de Organismos', {
            "fields": (
                'organismo', 'lugar','direccion','localidad','fecha','dias', 'descripcion','vigente','organizacion','responsable','telefono'),
        }), 
    )

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'imprimir_listado':
            if not request.POST.getlist(ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in agenda.objects.all().filter(organismo='INT'):
                    post.update({ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(agendaAdmin, self).changelist_view(request, extra_context)
    
    
    def save_model(self, request, obj, form, change):
        obj.usuario =  request.user.get_username()
        super().save_model(request, obj, form, change)
   



