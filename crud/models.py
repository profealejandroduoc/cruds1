from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .enumeraciones import *



# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10, primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    fnacto=models.DateField(verbose_name="Fecha de Nacimiento", null=False)
    correo=models.EmailField(verbose_name='E-mail')
    sexo=models.CharField(max_length=1,choices=TIPO_SEXO)
    foto=models.ImageField(upload_to='personas',null=True)

    def __str__ (self):
        return f"{self.rut} -  {self.nombre} {self.apellido}"
    

class Mascota(models.Model):
    nombre=models.CharField(max_length=50,null=False)
    tipo=models.CharField(max_length=15, null=False, choices=TIPO_MASCOTA)
    subtipo=models.CharField(max_length=20,choices=SUBTIPOS_MASCOTA,default='Otro')
    edad=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(300)])
    propietario=models.ForeignKey(Persona,on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre + "-" + self.tipo