from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Disciplina(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    horarios = models.CharField(max_length=500)
    cuota = models.PositiveIntegerField(null=True, blank=True)
    #profe =
    #socios =

    def __str__(self):
        return self.nombre
    
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.PositiveIntegerField(verbose_name="DNI", unique=True)
    # No hacemos único el email pues un menor puede ingresar el correo de su padre o madre, o inclusive ser Nulo
    email = models.EmailField(null=True, blank=True)

#    class Meta:
#        # El echo de que la clase sea o no abstracta, siendo que dni es único, tiene implicancias en el caso de que un Profe pueda ser también Socio
#        # De momento optamos porque no sea abstracta pues la solución nos resulta más clara de esta forma
#        abstract = True
                    
'''
class Profe(Persona):
    cuit = models.CharField(max_length=100, verbose_name='CUIT')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email'],
                condition=Q(email__isnull=False),
                name='unique_email'
            )
        ]

    def clean(self):
        super().clean()
        if Profe.objects.filter(dni=self.dni).exclude(id=self.id).exists():
            raise ValidationError({'dni': 'Ya existe un Profe con este DNI.'})
        if self.email is not None:
            if Profe.objects.filter(email=self.email).exclude(id=self.id).exists():
                raise ValidationError({'email': 'Ya existe un Profe con este email.'})


class Socio(Persona):
    numero = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email'],
                condition=Q(email__isnull=False),
                name='unique_email'
            )
        ]

    def clean(self):
        super().clean()
        if Socio.objects.filter(dni=self.dni).exclude(id=self.id).exists():
            raise ValidationError({'dni': 'Ya existe un Socio con este DNI.'})
        if self.email is not None:
            if Profe.objects.filter(email=self.email).exclude(id=self.id).exists():
                raise ValidationError({'email': 'Ya existe un Socio con este email.'})

    def save(self, *args, **kwargs):
        if not self.persona_id:
            # Crear una nueva instancia de Persona si no existe
            self.persona = Persona.objects.create(
                nombre=self.persona.nombre, 
                apellido=self.persona.apellido, 
                dni=self.persona.dni
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
'''