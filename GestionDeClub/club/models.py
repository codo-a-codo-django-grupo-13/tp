from django.db import models

# Create your models here.
# club/models.py


class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
