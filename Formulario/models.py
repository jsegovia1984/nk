from django.db import models
# Create your models here.

from django.contrib.auth.models import User


class Post(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    texto = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creado']

class Persona(models.Model):
    PLENARIOS = (
        ('LAF', 'G. de Laferrere'),
        ('MAD', 'V. Madero'),
        ('CAS', 'I. Casanova'),
        ('CAT', 'G. Catan'),
    )
    plenario = models.CharField(max_length=3, choices=PLENARIOS)
    nombre = models.CharField(max_length = 50) 
    apellido = models.CharField(max_length = 50)    
    telefono = models.CharField(max_length = 12)
    Direccion = models.CharField(max_length = 50)
    localidad = models.ForeignKey("Localidad", on_delete=models.PROTECT,help_text=" (¿Donde vivis?)")
    barrio = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.nombre

class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

    def __str__(self):
        return self.nombre

