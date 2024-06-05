from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('disciplinas/', views.DisciplinaListView.as_view(), name='disciplinas_listado'),
    #path('disciplinas/crear', views.disciplina_crear, name='disciplina_crear'),
    path('disciplinas/crear', views.DisciplinaCreateView.as_view(), name='disciplina_crear'),
    path('disciplinas/modificar/<int:disciplina_id>', views.disciplina_modificar, name='disciplina_modificar'),
    path('disciplinas/eliminar/<int:disciplina_id>', views.disciplina_eliminar, name='disciplina_eliminar'),
    path('profesores/', views.ProfeListView.as_view(), name='profes_listado'),
    path('socios/', views.SocioListView.as_view(), name='socios_listado'),
    #path('inscripcion_socio/', views.inscripcion_socio, name='inscripcion_socio'),
    #path('estado_socios/', views.estado_socios, name='estado_socios'),
    #path('editar_socio/<int:socio_id>/', views.editar_socio, name='editar_socio'),
    #path('eliminar_socio/<int:socio_id>/', views.eliminar_socio, name='eliminar_socio'),
]
