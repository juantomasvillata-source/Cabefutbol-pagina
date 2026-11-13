from django.db import models

#Datos del signup/login que se registrarán en una base de datos

class Datos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=100)


# Create your models here.
