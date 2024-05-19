from django.db import models
from django.utils import timezone


# Create your models here.
# club/models.py


class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_inscripcion = models.DateField(default=timezone.now)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"




class Pago(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.socio.nombre} - {self.monto} - {self.fecha_pago}"