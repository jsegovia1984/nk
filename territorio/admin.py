from django.contrib import admin
from django.contrib.auth.models import User, Group
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Unidades_Basicas,organizacion,Instituciones,Cuadricula,beneficios_anses,compañerxs


@admin.register(compañerxs)
class compañerxsAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','organizacion','trabaja_en_el_estado')
    search_fields = ('nombre','apellido','organizacion')
    fieldsets = (
        ('Compañerxs', {
            "fields": ('nombre','apellido','dni','direccion','barrio','telefono','mail','localidad','organizacion','afiliado_al_pj','trabaja_en_el_estado'),
        }), 
    )


@admin.register(organizacion)
class organizacionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)
    fieldsets = (
        ('Organizaciones', {
            "fields": ('nombre',),
        }), 
    )


@admin.register(beneficios_anses)
class beneficios_ansesAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    fieldsets = (
        ('Beneficios', {
            "fields": ('nombre',),
        }), 
    )


class Unidades_BasicasResource(resources.ModelResource):
    class Meta:
        model = Unidades_Basicas


def GeolocalizarUB(self, request, queryset):
    UBS=Unidades_Basicas.objects.all()
    for ub in UBS:
        ub.save()


@admin.register(Unidades_Basicas)
class Unidades_BasicasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('direccion','barrio','localidad','organizacion','casa_operativa')
    list_filter = ('localidad','organizacion')
    change_list_template ="admin/territorio/Unidades_Basicas/change_list.html"
    actions = [GeolocalizarUB,]
    resource_class = Unidades_BasicasResource
    fieldsets = (
        ('Listado de Unidades Basicas', {
            "fields": (
                'nombre','direccion','barrio','localidad','organizacion','casa_operativa',
    	),
        }), 

    )


def Geolocalizar(self, request, queryset):
    Institucion=Instituciones.objects.all()
    for inst in Institucion:
        inst.save()

class InstitucionesResource(resources.ModelResource):
    class Meta:
        model = Instituciones


@admin.register(Instituciones)
class InstitucionesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('organismo','sede','jefe','direccion','localidad','mail' )
    change_list_template ="admin/territorio/Instituciones/change_list.html"
    list_filter = ('localidad','organismo')
    resource_class = InstitucionesResource
    actions = [Geolocalizar,]

    fieldsets = (
        ('Listado de Instituciones', {
            "fields": (
                'organismo','sede','jefe','direccion' ,'localidad','municipio','telefono','mail','lat','lon'
	),
        }), 

    )

    def no_geo_parcial(self, obj):
        return not obj.geo_parcial



class CuadriculaResource(resources.ModelResource):
    class Meta:
        model = Cuadricula

@admin.register(Cuadricula)
class CuadriculaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','direccion','barrio','nombre','apellido','usuario')
    resource_class = CuadriculaResource
    list_filter = ('usuario','caso_de_gestion')
    fieldsets = (
        ('Datos Personales', {
            "fields": (
                'direccion','barrio','nombre','apellido','nacionalidad','edad' ,'telefono','trabajo_registrado'
	),
        }), 

       ('Numero de personas convivientes:', {
            "fields": (
                'menores','mayores','discapacitados'
	),
        }),

       ('VACUNATE:', {
            "fields": (
                'inscriptx_vacuna','desea_inscribirse','vacunacion'
	),
        }),

        ('ANSES:', {
            "fields": (
                'cobran_correctamente','beneficios'
	),
        }),

        ('SALUD:', {
            "fields": (
                'cobertura_de_salud','prestador','inconveniente'
	),
        }),

        ('RENAPER:', {
            "fields": (
                'DNI','tuvo_DNI_alguna_vez','turno'
	),
        }),

        ('ALIMENTOS:', {
            "fields": (
                'prestacion_alinentaria',
	),
        }),

        ('CASO DE GESTION (ESTE CAMPO LO COMPLETA LE COMPAÑERX):', {
            "fields": (
                'caso_de_gestion',
	),
        }),

        ('GENERO:', {
            "fields": (
                'conoces_la_linea_144',
	),
        }),

       ('BARRIO:', {
            "fields": (
                'mejoras',
	),
        }),

       ('POLITICA:', {
            "fields": (
                'politica1','politica2','preferencia'
	),
        }),

       ('OBSERVACIONES:', {
            "fields": (
                'observaciones',
	),
        }),


    )

    def save_model(self, request, obj, form, change):
        usuario = request.user.get_username()
        obj.usuario = usuario
        if usuario == 'janton84':
            obj.usuario = "folpevaperon"

        super().save_model(request, obj, form, change)
   

    def get_queryset(self, request): 
        user_current = request.user.get_username()

        if User.objects.filter(username=user_current, groups__name='ATENEO').exists():
            return super(CuadriculaAdmin, self).get_queryset(request)
        elif User.objects.filter(username=user_current, groups__name='nuevoencuentro').exists():			
            return super(CuadriculaAdmin, self).get_queryset(request).filter(usuario='nuevoencuentro')
        elif User.objects.filter(username=user_current, groups__name='peronismomilitante').exists():			
            return super(CuadriculaAdmin, self).get_queryset(request).filter(usuario='peronismomilitante')
        elif User.objects.filter(username=user_current, groups__name='folp').exists():			
            return super(CuadriculaAdmin, self).get_queryset(request).filter(usuario__contains='folp')
