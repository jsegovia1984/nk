from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.
from .models import Informes

# Register your models here.
@admin.register(Informes)
class InformesAdmin(admin.ModelAdmin):
    list_filter = ('organismo',)
    list_display = ( 'organismo', 'fecha','observaciones','usuario','archivo')
    fieldsets = (
        ('Informes de Gestion', {
            "fields": (
                'organismo', 'archivo','fecha','observaciones'),
        }), 
    )

    def get_queryset(self, request): 
        user_current = request.user.get_username()

        if User.objects.filter(username=user_current, groups__name='ATENEO').exists():
            return super(InformesAdmin, self).get_queryset(request)
        else:
            return super(InformesAdmin, self).get_queryset(request).filter(usuario=user_current)
    
    def save_model(self, request, obj, form, change):
        obj.usuario =  request.user.get_username()
        super().save_model(request, obj, form, change)
   




