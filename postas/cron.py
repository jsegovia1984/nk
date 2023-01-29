from .models import becarios,asistencia


def my_scheduled_job():
    beca = becarios.objects.all()
    beca = beca.filter(carga_horaria='LAV')
    for b in beca:
        asistencia.objects.create(nombre = b.nombre + " " + b.apellido, estado='P', certificado=False,organizacion=b.organizacion,posta=b.posta)
 

def fines_scheduled_job():
    beca = becarios.objects.all()
    beca = beca.filter(carga_horaria='FIN')
    for b in beca:
        asistencia.objects.create(nombre = b.nombre + " " + b.apellido, estado='P', certificado=False,organizacion=b.organizacion,posta=b.posta)
 



