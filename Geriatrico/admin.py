from django.contrib import admin
from .models import Geriatrico,Facturacion
from django.utils.html import format_html


# Register your models here.

@admin.register(Geriatrico)
class GeriatricoAdmin(admin.ModelAdmin):
    list_filter = ('localidad', 'conveniado','tipo',)
    list_display = ('razon_social','conveniado','tipo','cantidad_de_afiliados','direccion','localidad')
    search_fields = ['razon_social','direccion']
    fieldsets = (
        ('Geriatricos', {
            "fields": (
                'conveniado','razon_social','CUIT','sap','tipo','cantidad_de_afiliados','telefono','direccion','municipio','localidad'),
        }), 
    )


@admin.register(Facturacion)

class FacturacionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['Lugar']
    list_filter = ('Lugar', 'tipo',)
    date_hierarchy = 'Fecha_de_facturacion'
    list_display = ('Lugar','Fecha_de_facturacion','Monto','tipo',)
    search_fields = ['Lugar']
    fieldsets = (
        ('Facturacion', {
            "fields": (
                'Lugar', 'Fecha_de_facturacion','tipo','Monto'),
        }), 
    )

    def monto(self, obj):
        return format_html(
            '<span>$ {}</span>',
                obj.Monto,
        )
