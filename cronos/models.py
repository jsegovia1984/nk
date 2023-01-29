from django.db import models

# Create your models here.

class cliente(models.Model):
    socio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    dni = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    peso_inicial = models.FloatField(blank=True, null=True)
    altura = models.FloatField(blank=True, null=True)
    nombre_aviso = models.CharField(max_length=50, blank=True, null=True)
    telefono_aviso = models.CharField(max_length=50, blank=True, null=True)
    fecha_alta = models.DateField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True, default=False)


    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class pago(models.Model):
    socio = models.ForeignKey("cliente", on_delete=models.PROTECT)
    modalidad = models.ForeignKey("modalidad", on_delete=models.PROTECT)
    fecha_de_inicio = models.DateField(blank=True, null=True)
    fecha_de_fin = models.DateField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    medio_de_pago = models.ForeignKey("mediodepago", on_delete=models.PROTECT)


    def __str__(self):
        return "{}".format(self.socio)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"


class modalidad(models.Model):
    nombre = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"

class mediodepago(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Medio de Pago"
        verbose_name_plural = "Medios de pago"




class aranceles(models.Model):
    nombre = models.ForeignKey("modalidad", on_delete=models.PROTECT)
    precio = models.FloatField()


    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Arancel"
        verbose_name_plural = "Aranceles"




class stock(models.Model):
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.descripcion)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stock"




class gastos(models.Model):

    descripcion = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    unidades = models.IntegerField(blank=True, null=True)
    precio_unitario = models.FloatField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha= models.DateField(blank=True, null=True)
  

    def __str__(self):
        return "{}".format(self.descripcion)

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"



