from django.contrib import admin

# Register your models here.


from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Poligonos

class PoligonosResource(resources.ModelResource):
    class Meta:
        model = Poligonos

@admin.register(Poligonos)
class PoligonosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','lat','lon')
    resource_class = PoligonosResource
    fieldsets = (
        ('Poligonos', {
            "fields": ('nombre','lat','lon'),
        }), 
    )


