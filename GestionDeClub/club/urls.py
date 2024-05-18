from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('disciplinas/', views.disciplinas, name='disciplinas'),
    path('socios/', views.socios, name='socios'),
    path('inscripcion/', views.inscripcion_socio, name='inscripcion_socio'),
    path('estado_socios/', views.estado_socios, name='estado_socios'),
]