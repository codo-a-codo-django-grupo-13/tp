from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('disciplinas/', views.DisciplinaListView.as_view(), name='disciplinas_listado'),
    path('disciplinas/crear', views.DisciplinaCreateView.as_view(), name='disciplina_crear'),
    path('disciplinas/modificar/<int:pk>', views.DisciplinaUpdateView.as_view(), name='disciplina_modificar'),
    path('disciplinas/eliminar/<int:pk>', views.DisciplinaDeleteView.as_view(), name='disciplina_eliminar'),
    path('profes/', views.ProfeListView.as_view(), name='profes_listado'),
    path('profes/crear', views.ProfeCreateView.as_view(), name='profe_crear'),
    path('profes/modificar/<int:pk>', views.ProfeUpdateView.as_view(), name='profe_modificar'),
    path('profes/eliminar/<int:pk>', views.ProfeDeleteView.as_view(), name='profe_eliminar'),
    path('socios/', views.SocioListView.as_view(), name='socios_listado'),
    path('socios/crear', views.SocioCreateView.as_view(), name='socio_crear'),
    path('socios/modificar/<int:pk>', views.SocioUpdateView.as_view(), name='socio_modificar'),
    path('socios/eliminar/<int:pk>', views.SocioDeleteView.as_view(), name='socio_eliminar'),

    #path('disciplinas/inscripción/<int:pk>', views.DisciplinaCreateView.as_view(), name='disciplina_inscripcion'),
    path('socios/inscripcion/<int:pk>', views.SocioInscripcionCreateView.as_view(), name='socio_inscripcion'),
    path('socios/inscripcion/eliminar/<int:pk>', views.SocioInscripcionDeleteView.as_view(), name='socio_inscripcion_eliminar'),

    #path('inscripcion_socio/', views.inscripcion_socio, name='inscripcion_socio'),
    #path('estado_socios/', views.estado_socios, name='estado_socios'),
    #path('editar_socio/<int:socio_id>/', views.editar_socio, name='editar_socio'),
    #path('eliminar_socio/<int:socio_id>/', views.eliminar_socio, name='eliminar_socio'),


    #############
    #   Auth    #
    #############
    path ('accounts/login/', auth_views.LoginView.as_view(template_name='club/registration/login.html'), name='login'),
    path ('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path ('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='club/registration/password_reset.html'), name='password_reset'),
]
