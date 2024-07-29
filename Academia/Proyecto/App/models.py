from django.db import models

# Create your models here.

from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.EmailField()
    nivel = models.EmailField()
    
    

    def __str__(self):
        return self.nombre

