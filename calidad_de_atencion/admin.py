from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import Atencion_de_primer_nivel

@admin.register(Atencion_de_primer_nivel)
class Atencion_de_primer_nivelAdmin(admin.ModelAdmin):
    list_filter = ('agencia',)
    autocomplete_fields = ['medico']
    list_display = ('agencia','atencion','afiliado','fecha_del_reclamo')
    search_fields = ['medico','afiliado','descripcion']
    fieldsets = (
        ('CALIDAD DE ATENCION DE PRIMER NIVEL', {
            "fields": (
                'medico','agencia','atencion','afiliado','descripcion',)
        }), 
    )

    def get_queryset(self, request):
        qs = super(Atencion_de_primer_nivelAdmin, self).get_queryset(request)
        usuarios = User.objects.filter(groups__name='LAFERRERE')
        return qs
