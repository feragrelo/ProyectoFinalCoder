
from django.db import models
from django.forms import CharField, DateField, EmailField

class Pilotos(models.Model):
    nombre=models.CharField(max_length=50, null=True)
    nacionalidad=models.CharField(max_length=50, null=True)
    fecha_nacimiento=models.DateField(blank=True, null=True)
    
class Constructores(models.Model):
    nombre=models.CharField(max_length=30, null=True)
    nacionalidad=models.CharField(max_length=30,  null=True)
    email=models.EmailField( null=True)
    
class Circuitos(models.Model):
    nombre=models.CharField(max_length=30, null=True)
    país=models.CharField(max_length=30, null=True)
    año_primer_carrera=models.DateField(blank=True, null=True)
    
