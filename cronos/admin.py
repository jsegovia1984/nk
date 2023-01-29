from django.contrib import admin

# Register your models here.
from .models import cliente,modalidad,stock,pago,aranceles,mediodepago,gastos
from datetime import datetime



@admin.register(cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('socio','nombre','apellido','telefono','activo')
    list_filter = ('activo','apellido','telefono')
    search_fields = ['nombre','apellido']
    fieldsets = (
        ('Listado de Clientes', {
            "fields": (
	        'nombre','apellido','dni','fecha_nacimiento','peso_inicial','altura','telefono','mail','nombre_aviso','telefono_aviso'),
        }), 
    )


@admin.register(modalidad)
class modalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    fieldsets = (
        ('Listado de Medios de pago', {
            "fields": (
		'nombre',),
        }), 

    )


@admin.register(mediodepago)
class modalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    fieldsets = (
        ('Listado de medios de pago', {
            "fields": (
		'nombre',),
        }), 

    )

@admin.register(stock)
class stockAdmin(admin.ModelAdmin):
    list_display = ('descripcion','cantidad')
    fieldsets = (
        ('Stock de equipos', {
            "fields": (
		'descripcion','cantidad'),
        }), 

    )


@admin.register(pago)
class pagoAdmin(admin.ModelAdmin):
    list_display = ('socio','modalidad','fecha_de_inicio','fecha_de_fin','monto','saldo')
    autocomplete_fields = ('socio', )

    fieldsets = (
        ('Listado de Pagos', {
            "fields": (
		'socio','modalidad','fecha_de_inicio','monto','medio_de_pago'),
        }), 

    )



@admin.register(aranceles)
class arancelesAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio')
    fieldsets = (
        ('aranceles', {
            "fields": (
		'nombre','precio'),
        }), 

    )


@admin.register(gastos)
class gastosAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','fecha','precio','cantidad','unidades','precio_unitario',)
    fieldsets = (
        ('Gastos', {
            "fields": (
		'nombre','descripcion','fecha','precio','cantidad','unidades','precio_unitario',),
        }), 

    )

  

 
