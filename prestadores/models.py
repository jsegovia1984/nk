from django.db import models
      
class PrestadoresdePrimerNivel(models.Model):
    apellido = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    piso = models.CharField(max_length=5, blank=True, null=True)
    oficina = models.CharField(max_length=5, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    agencia = models.ForeignKey("Agencia", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

    class Meta:
        verbose_name = "Prestador de Primer Nivel"
        verbose_name_plural = "Prestadores de Primer Nivel"


class Direcciones(models.Model):
    razon_social = models.ForeignKey("PrestadoresdeSegundoNivel", on_delete=models.CASCADE, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.direccion)

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"


class PrestadoresdeSegundoNivel(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Prestador de Segundo Nivel"
        verbose_name_plural = "Prestadores de segundo Nivel"


class ComentariosSegundoNivel(models.Model):
    prestadores= models.ForeignKey("PrestadoresdeSegundoNivel", on_delete=models.CASCADE, blank=True, null=True)
    descripcion = models.TextField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
  
    def __str__(self):
        return "{}".format(self.prestadores)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"


class Procedimientos_neurologicos_pe(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Procedimientos neurologico PE"
        verbose_name_plural = "Procedimientos neurologicos PE"


class Procedimientos_neurologicos(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Procedimientos neurologico"
        verbose_name_plural = "Procedimientos neurologicos"


class Terapia_radiante(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Terapia radiante"
        verbose_name_plural = "Terapia radiante"



class Terapia_radiante_IM(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Terapia radiante IM"
        verbose_name_plural = "Terapia radiante IM"



class Artroscopia(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Artroscopia"
        verbose_name_plural = "Artroscopia"


class Litotricia_extracorporea(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Litotricia extracorporea"
        verbose_name_plural = "Litotricia extracorporeas"


class Oftalmologia(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Oftalmologia"
        verbose_name_plural = "Oftalmologia"


class Odontologia_primaria(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.PROTECT, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.PROTECT, blank=True, null=True)
    activo = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)


    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Odontologia primaria"
        verbose_name_plural = "Odontologia primaria"

class Odontologia_alto_riesgo(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)


    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Odontologia alto riesgo"
        verbose_name_plural = "Odontologia alto riesgo"




class Odontologia_servicios_complementarios(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)


    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Odontologia servicios complementarios "
        verbose_name_plural = "Odontologia servicios complementarios "



class Neurocirugia(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Neurocirugia"
        verbose_name_plural = "Neurocirugia"






class Cardiologia_alta_complejidad_y_hemodinamia(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Cardiologia alta complejidad y hemodinamia"
        verbose_name_plural = "Cardiologia alta complejidad y hemodinamia"


class Electrofisiologia(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Electrofisiologia"
        verbose_name_plural = "Electrofisiologia"



class Cirugia_cardiovascular(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Cirugia cardiovascular"
        verbose_name_plural = "Cirugia cardiovascular"


class Colocacion_de_marcapaso(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Colocacion de marcapaso"
        verbose_name_plural = "Colocacion de marcapaso"


class Ecodoppler(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Ecodoppler"
        verbose_name_plural = "Ecodoppler"


class Kinesiologia(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Kinesiologia"
        verbose_name_plural = "Kinesiologia"


class Diagnostico_por_imagenes(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Diagnostico por imagenes"
        verbose_name_plural = "Diagnostico por imagenes"



class Resonancia_magnetica(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Resonancia Magnetica"
        verbose_name_plural = "Resonancia Magneticas"

class ComentariosResonancia(models.Model):
    prestadores= models.ForeignKey("Resonancia_magnetica", on_delete=models.CASCADE, blank=True, null=True)
    descripcion = models.TextField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
  
    def __str__(self):
        return "{}".format(self.prestadores)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"


class Tomografia_computada(models.Model):
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    capita = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        verbose_name = "Tomografia computada"
        verbose_name_plural = "Tomografia computada"

class Municipio(models.Model):
    nombre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    municipio = models.ForeignKey("Municipio", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

    def __str__(self):
        return self.nombre


class Agencia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    localidad = models.ForeignKey("Localidad", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Agencia"
        verbose_name_plural = "Agencias"

    def __str__(self):
        return self.nombre



