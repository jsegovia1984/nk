from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Organismo,Casos,Region,Casos_interminitserial
from agenda.models import agenda
from django.contrib.auth.models import User, Group
from django.http import FileResponse,HttpResponse
from pathlib import Path
import os
from fpdf import FPDF




@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion',)
    fieldsets = (
        ('Listado de Regiones', {
            "fields": (
                'nombre','descripcion'),
        }), 
    )

@admin.register(Organismo)
class OrganismoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)
    fieldsets = (
        ('Listado de Organismos', {
            "fields": (
                'nombre',),
        }), 
    )


class CasosResource(resources.ModelResource):
    class Meta:
        model = Casos

class CasosinterResource(resources.ModelResource):
    class Meta:
        model = Casos_interminitserial


def Marcar_Interministerial(self, request, queryset):
    for caso in queryset:
        caso.interministerial=True
        caso.caso_resuelto=True
        caso.usuario="opinter"
        caso.save()

def Agregar_fecha_a_vacios(self, request, queryset):
    fullcasos = Casos.objects.all()
    for caso in fullcasos:
        if caso.fecha_de_entrada:
            print("OK " + caso.nombre)
        else:
            print(caso.nombre)
            caso.fecha_de_entrada='2021-01-01'
            caso.save()


@admin.register(Casos_interminitserial)
class CasosinterAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','nombre','apellido','organismo','caso_resuelto','fecha_de_entrada','region','organizacion','usuario')
    search_fields = ['nombre','apellido','domicilio']
    list_filter = ('organismo','localidad','lugar_operativo')
    actions = [Marcar_Interministerial,Agregar_fecha_a_vacios]
    change_list_template ="admin/casos_de_gestion/Casos_interminitserial/change_list.html"
#    autocomplete_fields = ('lugar_operativo','localidad','organismo')
    date_hierarchy = 'fecha_de_entrada'

    resource_class = CasosinterResource
    fieldsets = (
        ('Listado de Organismos', {
            "fields": (
                'caso_resuelto','lugar_operativo','apellido','nombre','dni','domicilio','localidad','contacto','organismo','tipo_de_Tramite','observaciones', 'fecha_de_entrada',
        ),
        }), 

    )

    def save_model(self, request, obj, form, change):

        user_current = request.user.get_username()
        obj.fecha_de_resolucion = obj.fecha_de_entrada
        obj.usuario =  'opinter'
        obj.metodo_de_entrada = 'InterMinisterial'
        obj.interministerial = True
        obj.caso_resuelto = True


        if User.objects.filter(username=user_current, groups__name='nuevoencuentro').exists():  
                obj.organizacion = "nuevoencuentro"     
        elif User.objects.filter(username=user_current, groups__name='peronismomilitante').exists():    
                obj.organizacion = "peronismomilitante"
        elif User.objects.filter(username=user_current, groups__name='folp').exists():
                obj.organizacion = "folp"       
        elif User.objects.filter(username=user_current, groups__name='lacampora').exists():
                obj.organizacion = "lacampora"  
        elif User.objects.filter(username=user_current, groups__name='ATENEO').exists():
                obj.organizacion = "ateneo"     

 
        else:
            obj.organizacion = user_current

        super().save_model(request, obj, form, change)


    def get_queryset(self, request): 
        user_current = request.user.get_username()
        return super(CasosinterAdmin, self).get_queryset(request).filter(usuario='opinter')



@admin.register(Casos)
class CasosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','nombre','apellido','organismo','caso_resuelto','fecha_de_entrada','region','organizacion','usuario')
    search_fields = ['nombre','apellido','domicilio','dni','contacto']
    list_filter = ('caso_resuelto','usuario','region','organismo','localidad')
    actions = [Marcar_Interministerial,Agregar_fecha_a_vacios]
    change_list_template ="admin/casos_de_gestion/casos_de_gestion/change_list.html"
#    autocomplete_fields = ('lugar_operativo','localidad','organismo')
    date_hierarchy = 'fecha_de_entrada'

    resource_class = CasosResource
    fieldsets = (
        ('Listado de Organismos', {
            "fields": (
                'caso_resuelto','apellido','nombre','dni','domicilio','localidad','contacto','metodo_de_entrada','organismo','tipo_de_Tramite','observaciones', 'fecha_de_entrada','fecha_de_resolucion','persona_de_Seguimiento','region', 
	),
        }), 
 

    )
    
    def save_model(self, request, obj, form, change):
        user_current = request.user.get_username()
        obj.usuario =  user_current
        obj.lugar_operativo = agenda.objects.get(id='85')


        if User.objects.filter(username=user_current, groups__name='nuevoencuentro').exists():	
	        obj.organizacion = "nuevoencuentro"	
        elif User.objects.filter(username=user_current, groups__name='peronismomilitante').exists():	
	        obj.organizacion = "peronismomilitante"			
        elif User.objects.filter(username=user_current, groups__name='folp').exists():			
	        obj.organizacion = "folp"	
        elif User.objects.filter(username=user_current, groups__name='lacampora').exists():			
	        obj.organizacion = "lacampora"	
        elif User.objects.filter(username=user_current, groups__name='ATENEO').exists():			
            	obj.organizacion = "ateneo"	

        else:
            obj.organizacion = user_current
           
        super().save_model(request, obj, form, change)


    def get_queryset(self, request): 
        user_current = request.user.get_username()
        if User.objects.filter(username=user_current, groups__name='ATENEO').exists():
            return super(CasosAdmin, self).get_queryset(request).exclude(usuario='opinter')
        elif User.objects.filter(username=user_current, groups__name='nuevoencuentro').exists():			
            return super(CasosAdmin, self).get_queryset(request).exclude(organizacion=['lacampora', 'folp','peronismomilitante']).exclude(usuario='opinter')
        elif User.objects.filter(username=user_current, groups__name='peronismomilitante').exists():			
            return super(CasosAdmin, self).get_queryset(request).exclude(organizacion=['lacampora', 'nuevoencuentro','folp']).exclude(usuario='opinter')
        elif User.objects.filter(username=user_current, groups__name='folp').exists():			
            return super(CasosAdmin, self).get_queryset(request).filter(organizacion='folp')
        elif User.objects.filter(username=user_current, groups__name='lacampora').exists():	
            return super(CasosAdmin, self).get_queryset(request).filter(organizacion='lacampora').exclude(usuario='opinter')
        else:
            return super(CasosAdmin, self).get_queryset(request).filter(usuario = user_current)
