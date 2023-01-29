from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import tipo_ac,situacion_documental,proceso,asociaciones_civiles


def Geolocalizar(self, request, queryset):
    UBS=asociaciones_civiles.objects.all()
    for ub in UBS:
        ub.save()


@admin.register(tipo_ac)
class tipoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)
    fieldsets = (
        ('Tipo de Asociacion Civil', {
            "fields": (
                'nombre',),
        }), 
    )

@admin.register(situacion_documental)
class situacion_documentalAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)
    fieldsets = (
        ('Situacion Documental', {
            "fields": (
                'nombre',),
        }), 
    )


@admin.register(proceso)
class procesoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)
    fieldsets = (
        ('Proceso', {
            "fields": (
                'nombre',),
        }), 
    )



class ACResource(resources.ModelResource):
    class Meta:
        model = asociaciones_civiles


@admin.register(asociaciones_civiles)
class asociaciones_civilesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','direccion','localidad','Inscripta','organizacion')
    search_fields = ['nombre',]
    actions = [Geolocalizar,]
    list_filter = ('localidad','organizacion','tipo')
    resource_class = ACResource
    change_list_template ="admin/asociaciones_civiles/asociaciones_civiles/change_list.html"

    fieldsets = (
        ('Asociaciones Civiles', {
            "fields": (
                'nombre','foto','direccion','localidad','tipo','grado_de_relacion','Inscripta','numero','situacion_documental','proceso','detalle','recursos_y_actividades','organizacion'),
        }), 
    )

