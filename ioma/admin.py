from django.contrib import admin
from django.http import FileResponse
from import_export import resources
from import_export.admin import ImportExportModelAdmin


import os

# Register your models here.

from .models import prestadores, postas_itinerantes,afiliados
from django.http import HttpResponse
from pathlib import Path

from fpdf import FPDF

@admin.register(prestadores)
class prestadoresAdmin(admin.ModelAdmin):
    search_fields = ['nombre','direccion']
    list_display = ('activo','nombre', 'no_geo_parcial' ,'direccion','localidad','telefonos')
    list_filter = ('localidad',)
    change_list_template ="admin/ioma/prestadores/change_list.html"

    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','nombre', 'direccion','telefonos','mail','municipio','localidad','director','subdirector','lat','lon',),
        }), 
    )

    def no_geo_parcial(self, obj):
        return not obj.geo_parcial
    no_geo_parcial.boolean = True 



def Informe(self, request, queryset):

    BASE_DIR = Path(__file__).resolve().parent.parent
    informe=FPDF()
    informe.add_page()
    informe.set_xy(0, 0)

    informe.set_font("Arial","B", size=10)
    vertical = 5
    for linea in queryset:
        lugar=linea.lugar
        cantidad=linea.cantidad_de_vacunados
        inicio=str(linea.fecha_inicio)
        fin=str(linea.fecha_fin)
        informe.cell(60,vertical,txt=lugar + " " + cantidad + " " + inicio + " " + fin , ln=1, align='C')
        vertical = vertical + 5
    target = os.path.join(BASE_DIR, 'media', 'pdfs') + '/example.pdf'
    informe.output(target)
    
    file = open(target, 'rb')

    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename=example.pdf' 
    return response

   

@admin.register(postas_itinerantes)
class postas_itinerantesAdmin(admin.ModelAdmin):
    list_display = ('lugar','fecha_inicio','fecha_fin','direccion', 'localidad','cantidad_de_vacunados')
    actions = [Informe]
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'lugar','tipo','fecha_inicio','fecha_fin','direccion', 'localidad','cantidad_de_vacunados','comentarios'),
        }), 
    )


class afiliadosResource(resources.ModelResource):
    class Meta:
        model = afiliados


@admin.register(afiliados)
class afiliadosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_y_apellido','numero_de_afiliado','fecha_de_nacimiento','localidades','mail', 'tel_fijo','celular',)
    resource_class = afiliadosResource
    list_filter = ('localidades',)
    search_fields = ['nombre_y_apellido',]

    fieldsets = (
        ('Afiliados', {
            "fields": (
                'nombre_y_apellido','numero_de_afiliado','fecha_de_nacimiento','localidades','mail', 'tel_fijo','celular',),
        }), 
    )




