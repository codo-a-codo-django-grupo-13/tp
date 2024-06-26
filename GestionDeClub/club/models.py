from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Disciplina(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    horarios = models.CharField(max_length=500)
    cuota = models.PositiveIntegerField(null=True, blank=True)
    profe = models.ForeignKey('Profe', related_name='disciplinas', on_delete=models.SET_NULL, null=True, blank=True) # classe Profe entre comillas porque aún no está definida (más abajo recién)
    socios = models.ManyToManyField('Socio', related_name='disciplinas', through='Inscripcion') # classe Socio entre comillas porque aún no está definida (más abajo recién)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class Inscripcion(models.Model):
    socio = models.ForeignKey('Socio', on_delete=models.CASCADE) # classe Socio entre comillas porque aún no está definida (más abajo recién)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        # En realidad un socio podría desinscribirse y volverse a inscribir en el futuro, pero es un caso que no analizaremos en esta versión
        unique_together = ('socio', 'disciplina')

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.PositiveIntegerField(verbose_name="DNI", unique=True)
    # No hacemos único el email en esta Clase pues en el caso de Socio un/a menor puede ingresar el correo de su padre o madre, o inclusive ser Nulo
    email = models.EmailField(null=True, blank=True)

    class Meta:
        # El echo de que la clase Persona sea o no abstracta, tiene implicancias en el caso de que un Profe pueda ser también Socio
        # Por simplicidad optamos por hacer asbtracta la clase Persona y tomar Profe y Socio como dos Tipos completamente independientes
        abstract = True
                    

class Profe(Persona):
    cuit = models.CharField(max_length=100, verbose_name='CUIT', unique=True)

    class Meta:
        # No permitimos dos profes con el mismo email salvo que sea Null
        constraints = [
            models.UniqueConstraint(
                fields=['email'],
                condition=Q(email__isnull=False),
                name='unique_email')
        ]

    def clean(self):
        super().clean()
        if Profe.objects.filter(dni=self.dni).exclude(id=self.id).exists():
            raise ValidationError({'dni': 'Ya existe un Profe con este DNI.'})
        # No permitimos dos profes con el mismo email salvo que sea Null
        if self.email is not None:
            if Profe.objects.filter(email=self.email).exclude(id=self.id).exists():
                raise ValidationError({'email': 'Ya existe un Profe con este email.'})

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.cuit})"


class Socio(Persona):
    numero = models.PositiveIntegerField(unique=True)
    fecha_alta = models.DateField(verbose_name="Fecha de alta", auto_now_add=True)

    def clean(self):
        super().clean()
        if Socio.objects.filter(dni=self.dni).exclude(id=self.id).exists():
            raise ValidationError({'dni': 'Ya existe un Socio con este DNI.'})

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.numero})"