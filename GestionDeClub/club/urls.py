from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('disciplinas/', views.disciplinas_listado, name='disciplinas_listado'),
    path('profesores/', views.profesores, name='profesores'),
    path('socios/', views.socios, name='socios'),
    #path('inscripcion_socio/', views.inscripcion_socio, name='inscripcion_socio'),
    #path('estado_socios/', views.estado_socios, name='estado_socios'),
    #path('editar_socio/<int:socio_id>/', views.editar_socio, name='editar_socio'),
    #path('eliminar_socio/<int:socio_id>/', views.eliminar_socio, name='eliminar_socio'),
    path('disciplinas/crear', views.disciplina_crear, name='disciplina_crear'),
    path('disciplinas/modificar/<int:disciplina_id>', views.disciplina_modificar, name='disciplina_modificar'),
]
