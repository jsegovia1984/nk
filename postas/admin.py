from django.contrib import admin
import datetime
from .models import becarios,postas,asistencia,conteo_de_vacunas,stock_de_vacunas
from datetime import datetime
from django.contrib.auth.models import User, Group

# exportar e importar
from import_export import resources
from import_export.admin import ImportExportModelAdmin


now = datetime.now()


def Presentes(self, request, queryset):
    beca = becarios.objects.all()
    beca = beca.filter(carga_horaria='LAV')
    for b in beca:
        asistencia.objects.create(nombre = b.nombre + " " + b.apellido, estado='P', certificado=False,organizacion=b.organizacion,posta=b.posta)
    self.message_user(request, "Se guardo en forma exitosa")


def Ausente(self, request, queryset):
    for b in queryset:
        reg = asistencia.objects.filter(nombre=b.nombre + " " + b.apellido, fecha=now)
        
        if reg.count()==0:
            asistencia.objects.create(nombre = b.nombre + " " + b.apellido, estado='A', certificado=False, fecha=request.POST['start'])
        else:
            reg.update(estado='A')
    self.message_user(request, "Se guardo en forma exitosa")




class becariosResource(resources.ModelResource):
    class Meta:
        model = becarios


@admin.register(becarios)
class becariosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','apellido','tarea','posta','turno','region')
  # change_list_template ="admin/postas/becarios/change_list.html"
    list_filter = ('posta',)
    resource_class = becariosResource

  #  actions = [Presentes,Ausente,Guardar]

    fieldsets = (
        ('becarios', {
            "fields": (
                'region','nombre','apellido','telefono','posta','turno','tarea','carga_horaria',),
        }), 
    )


    def save_model(self, request, obj, form, change):
        usuario = request.user.get_username()
        obj.usuario = usuario
        super().save_model(request, obj, form, change)
   

    def get_queryset(self, request): 
        user_current = request.user.get_username()	
        if User.objects.filter(username=user_current, groups__name='ATENEO').exists():
            return super(becariosAdmin, self).get_queryset(request)
        else:
            return super(becariosAdmin, self).get_queryset(request).filter(usuario=user_current)
  

@admin.register(postas)
class postasAdmin(admin.ModelAdmin):
    list_display = ('lugar','fecha_inicio','fecha_fin','direccion', 'localidad')
    fieldsets = (
        ('postas', {
            "fields": (
                'lugar','fecha_inicio','fecha_fin','direccion', 'localidad','comentarios'),
        }), 
    )


@admin.register(asistencia)
class asistenciaAdmin(admin.ModelAdmin):
    list_display = ('fecha','nombre','estado','certificado','comentario','organizacion')
    search_fields = ['nombre']
    date_hierarchy = 'fecha'
    list_filter = ('estado',)
    fieldsets = (
        ('asistencia', {
            "fields": (
                'fecha','nombre','estado','certificado','horario_ingreso','horario_salida','comentario'),
        }), 
    )

@admin.register(conteo_de_vacunas)
class conteo_de_vacunasAdmin(admin.ModelAdmin):
    list_display = ('posta','fecha','cantidad_turnera','turnera','cantidad_turnera','faltas','espontanea','primera_dosis','segunda_dosis')
    search_fields = ['posta']
    date_hierarchy = 'fecha'
    list_filter = ('posta',)
    fieldsets = (
        ('Conteo de vacunas', {
            "fields": (
                'posta','fecha','turnera','cantidad_turnera','faltas','espontanea','primera_dosis','segunda_dosis'),
        }), 
    )


@admin.register(stock_de_vacunas)
class stock_de_vacunasAdmin(admin.ModelAdmin):
    list_display = ('posta','fecha','laboratorio','tipo','formato','cantidad')
    search_fields = ['posta']
    date_hierarchy = 'fecha'
    list_filter = ('posta',)
    fieldsets = (
        ('Conteo de vacunas', {
            "fields": (
                'posta','fecha','laboratorio','tipo','formato','cantidad'),
        }), 
    )




