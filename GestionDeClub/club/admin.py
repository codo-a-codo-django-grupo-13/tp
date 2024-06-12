from django.contrib import admin
from .models import Disciplina, Profe, Socio, Inscripcion


class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [InscripcionInline]

admin.site.register(Disciplina, DisciplinaAdmin)


admin.site.register(Profe)

    
class SocioAdmin(admin.ModelAdmin):
    inlines = [InscripcionInline]

admin.site.register(Socio, SocioAdmin)