from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100) 
    edad = models.TextField()