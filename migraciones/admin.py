from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import casos, nacionalidad

def eliminar_todo(modeladmin, request, queryset):
    casos.objects.all().delete()





@admin.register(nacionalidad)
class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ('id','nacionalidad',)
    fieldsets = (
        ('NACIONALIDADES', {
            "fields": (
                'nacionalidad',),
        }), 
    )


class CasosResource(resources.ModelResource):
    class Meta:
        model = casos


@admin.register(casos)
class casosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','apellido','localidad','expediente',)
    search_fields = ['nombre','apellido','expediente',]
    resource_class = CasosResource
    actions = [eliminar_todo]
    date_hierarchy = 'fecha_de_toma'
    list_filter = ('interministerial','localidad','nacionalidad')
    change_list_template ="admin/migraciones/casos/change_list.html"
    fieldsets = (
        ('CASOS DE MIGRACIONES', {
            "fields": (
                'interministerial',('nombre','apellido'),'dni_cedula','fecha_de_nacimiento','nacionalidad','direccion','localidad','fecha_de_toma',('modo_de_toma','lugar_de_toma'),'expediente','estado_del_tramite','mail','telefono','observaciones','agente')
        }), 
    )



    
