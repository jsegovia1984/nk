from django.contrib import admin
# Register your models here.

from .models import lugar, postres

@admin.register(lugar)
class lugarAdmin(admin.ModelAdmin):
    list_display = ('nombre','sucursal','direccion','ciudad','barrio',)
    fieldsets = (
        ('LUGARES', {
            "fields": (
                'nombre','sucursal','direccion','ciudad','barrio',),
        }),

    )



@admin.register(postres)
class postresAdmin(admin.ModelAdmin):
    list_display = ('lugar','nombre','descripcion','porcion','precio','descuento','foto','observacion','disponible',)
    fieldsets = (
        ('Postres', {
            "fields": (
                'lugar','nombre','descripcion','porcion','precio','descuento','foto','observacion','disponible',),
        }),

    )






