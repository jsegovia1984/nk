from django.contrib import admin
from .models import Centros, Subsidios

class SubsideiosInline(admin.TabularInline):
    model = Subsidios
    extra = 1

# Register your models here.
@admin.register(Centros)
class CentrosAdmin(admin.ModelAdmin):
    list_filter = ('localidad', 'incluido','agencia')
    inlines = [SubsideiosInline,]
    list_display = ('incluido','centro','presidente','direccion','agencia','localidad')
    search_fields = ['centro ','direccion']
    fieldsets = (
        ('Centros', {
            "fields": (
                'incluido', 'subsidio','centro','personeria_Juridica','sap','CUIT','presidente','agencia','localidad','municipio','direccion','telefono','relacion','observaciones'),
        }), 
    )


