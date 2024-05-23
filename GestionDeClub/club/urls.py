from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('disciplinas/', views.disciplinas, name='disciplinas'),
    path('profesores/', views.profesores, name='profesores'),
    path('socios/', views.socios, name='socios'),
    path('inscripcion_socio/', views.inscripcion_socio, name='inscripcion_socio'),
    path('estado_socios/', views.estado_socios, name='estado_socios'),
    path('editar_socio/<int:socio_id>/', views.editar_socio, name='editar_socio'),
    path('agregar_pago/', views.agregar_pago, name='agregar_pago'),
    path('listar_pagos/', views.listar_pagos, name='listar_pagos'),
    path('eliminar_socio/<int:socio_id>/', views.eliminar_socio, name='eliminar_socio'),
    path('reporte_pagos/', views.reporte_pagos, name='reporte_pagos'),
]
