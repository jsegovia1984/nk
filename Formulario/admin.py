from django.contrib import admin

# Register your models here.
from Formulario.models import Persona,Localidad

class PersonaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'apellido', 'telefono','Direccion', 'barrio')
    list_filter = ('plenario',)

admin.site.register(Persona,PersonaAdmin)
admin.site.register(Localidad)
