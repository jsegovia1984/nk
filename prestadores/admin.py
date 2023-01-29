from django.contrib import admin

# Register your models here.
from .models import PrestadoresdePrimerNivel,Localidad,Municipio,PrestadoresdeSegundoNivel,Kinesiologia,Ecodoppler,Diagnostico_por_imagenes,Agencia
from .models import Tomografia_computada,Resonancia_magnetica
from .models import Procedimientos_neurologicos_pe,Procedimientos_neurologicos,Terapia_radiante,Terapia_radiante_IM,Artroscopia,Litotricia_extracorporea,Oftalmologia,Odontologia_primaria,Odontologia_alto_riesgo,Odontologia_servicios_complementarios,Neurocirugia,Cardiologia_alta_complejidad_y_hemodinamia,Electrofisiologia,Cirugia_cardiovascular,Colocacion_de_marcapaso,Diagnostico_por_imagenes
from .models import Direcciones,ComentariosSegundoNivel,ComentariosResonancia



@admin.register(PrestadoresdePrimerNivel)
class PrestadoresdePrimerNivelAdmin(admin.ModelAdmin):
    search_fields = ['nombre','apellido','direccion']
    list_display = ('activo','nombre', 'apellido','capita','municipio','localidad','agencia')
    list_filter = ('localidad', 'activo','municipio','agencia')
    change_list_template ="admin/prestadores/PrestadoresdePrimerNivel/change_list.html"

    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','nombre', 'apellido','capita','fecha_de_nacimiento','direccion','piso','oficina','telefono','municipio','localidad','agencia',),
        }), 
    )


class DireccionesInline(admin.TabularInline):
    model = Direcciones
    extra = 1

class ComentariosSegundoNivelInline(admin.TabularInline):
    model = ComentariosSegundoNivel
    extra = 1


@admin.register(PrestadoresdeSegundoNivel)
class PrestadoresdeSegundoNivelAdmin(admin.ModelAdmin):
    inlines = [DireccionesInline,ComentariosSegundoNivelInline,]
    search_fields = ['razon_social']
    list_display = ('activo','razon_social','capita',)
    fieldsets = (
        ('Prestadores de segundo nivel', {
            "fields": (
                'activo','razon_social','capita','telefono'),
        }), 
    )

@admin.register(Kinesiologia)
class KinesiologiaAdmin(admin.ModelAdmin):
    search_fields = ['razon_social']
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Diagnostico_por_imagenes)
class Diagnostico_por_imagenesAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Tomografia_computada)
class Tomografia_computadaAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )


class ComentariosResonanciaInline(admin.TabularInline):
    model = ComentariosResonancia
    extra = 1

@admin.register(Resonancia_magnetica)
class Resonancia_magneticaAdmin(admin.ModelAdmin):
    inlines = [ComentariosResonanciaInline,]
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )


@admin.register(Ecodoppler)
class EcodopplerAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    fieldsets = (
        ('Localidad', {
            "fields": (
                'municipio', 'nombre', 
            ),
        }),
    )

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    search_fields = ['nombre']
    fieldsets = (
        ('Municipio', {
            "fields": (
                'nombre',
            ),
        }),
    )

@admin.register(Agencia)
class AgenciaAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    search_fields = ['nombre']
    list_display = ('nombre', 'direccion',)
    fieldsets = (
        ('Municipio', {
            "fields": (
                'nombre','direccion','localidad',
            ),
        }),
    )


@admin.register(Procedimientos_neurologicos_pe)
class Procedimientos_neurologicos_peAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'
	    ),
        }), 
    )


@admin.register(Procedimientos_neurologicos)
class Procedimientos_neurologicosAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Terapia_radiante)
class Terapia_radianteAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Terapia_radiante_IM)
class Terapia_radiante_IMAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Artroscopia)
class ArtroscopiaAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Litotricia_extracorporea)
class Litotricia_extracorporeaAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Oftalmologia)
class OftalmologiaAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad','observaciones'),
        }), 
    )

@admin.register(Odontologia_primaria)
class Odontologia_primariaAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad','observaciones'),
        }), 
    )

@admin.register(Odontologia_alto_riesgo)
class Odontologia_alto_riesgoAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad','observaciones')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Odontologia_servicios_complementarios)
class Odontologia_servicios_complementariosAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad','observaciones')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad','observaciones'),
        }), 
    )

@admin.register(Neurocirugia)
class NeurocirugiaAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Cardiologia_alta_complejidad_y_hemodinamia)
class Cardiologia_alta_complejidad_y_hemodinamiaAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Electrofisiologia)
class ElectrofisiologiaAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Cirugia_cardiovascular)
class Cirugia_cardiovascularAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )

@admin.register(Colocacion_de_marcapaso)
class Colocacion_de_marcapasoAdmin(admin.ModelAdmin):
    list_display = ('activo','razon_social','capita','direccion','municipio','localidad')
    search_fields = ['razon_social']
    fieldsets = (
        ('Prestadores', {
            "fields": (
                'activo','razon_social','capita','telefono','direccion','municipio','localidad'),
        }), 
    )




admin.site.site_header = "Sistema de Gestion"
admin.site.site_title = " LA MATANZA"
admin.site.index_title = "Bienvenido al Sistema de Gestion "
