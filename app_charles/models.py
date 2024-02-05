from django.db import models

# Create your models here.
class Libros(models.Model):
    nombre = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    editorial = models.CharField(max_length=60)
    resenia = models.TextField(blank=True)
    detalle = models.CharField(max_length=200)
    comentarios = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.nombre}, {self.autor}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    dni = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"