from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import DisciplinaForm, ProfeForm, SocioForm, InscripcionForm
from .models import Disciplina, Profe, Socio, Inscripcion


def home(request):
    context = {'test': 'Test'}
    return render(request, 'club/home.html', context)


'''#############'''
''' DISCIPLINAS '''

class DisciplinaListView(ListView):
    model = Disciplina
    template_name = 'club/disciplinas_listado.html'
    context_object_name = 'disciplinas'


class DisciplinaCreateView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'club/disciplina_crear.html'
    success_url = reverse_lazy('disciplinas_listado')
    success_message = 'Diciplina %(nombre)s creada!'
    permission_required = 'club.add_disciplina'


class DisciplinaUpdateView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'club/disciplina_modificar.html'
    success_url = reverse_lazy('disciplinas_listado')
    success_message = 'Diciplina %(nombre)s actualizada!'
    permission_required = 'club.change_disciplina'


class DisciplinaDeleteView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Disciplina
    success_url = reverse_lazy('disciplinas_listado')
    success_message = 'Diciplina eliminada!'
    permission_required = 'club.delete_disciplina'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = self.get_object()
        return context


'''########'''
''' PROFES '''

class ProfeListView(ListView):
    model = Profe
    template_name = 'club/profes_listado.html'
    context_object_name = 'profes'


class ProfeCreateView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    model = Profe
    form_class = ProfeForm
    template_name = 'club/profe_crear.html'
    success_url = reverse_lazy('profes_listado')
    success_message = 'Profe %(nombre)s %(apellido)s creado!'
    permission_required = 'club.add_profe'

class ProfeUpdateView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Profe
    form_class = ProfeForm
    template_name = 'club/profe_modificar.html'
    success_url = reverse_lazy('profes_listado')
    success_message = 'Profe %(nombre)s %(apellido)s actualizado!'
    permission_required = 'club.change_profe'

class ProfeDeleteView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Profe
    success_url = reverse_lazy('profes_listado')
    success_message = 'Profe eliminado!'
    permission_required = 'club.delete_profe'

'''########'''
''' SOCIOS '''

class SocioListView(LoginRequiredMixin, ListView):
    model = Socio
    template_name = 'club/socios_listado.html'
    context_object_name = 'socios'

class SocioCreateView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    model = Socio
    form_class = SocioForm
    template_name = 'club/socio_crear.html'
    success_url = reverse_lazy('socios_listado')
    success_message = 'Socio %(nombre)s %(apellido)s creado!'
    permission_required = 'club.add_socio'

class SocioUpdateView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'club/socio_modificar.html'
    success_url = reverse_lazy('socios_listado')
    success_message = 'Socio %(nombre)s %(apellido)s actualizado!'
    permission_required = 'club.change_socio'

class SocioDeleteView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Socio
    success_url = reverse_lazy('socios_listado')
    success_message = 'Socio eliminado!'
    permission_required = 'club.delete_socio'


# VISTA PARAMETRIZADA, RECIBE EN EL PARÁMETRO <int:pk> EL ID DEL SOCIO QUE SE QUIERE INSCRIBIR
class SocioInscripcionCreateView(PermissionRequiredMixin, CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'club/inscripcion_a_disciplina.html'
    success_url = reverse_lazy('socios_listado')
    permission_required = 'club.add_inscripcion'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['socio_id'] = self.kwargs.get('pk')
        return kwargs

    def get_initial(self):
        initial = super(SocioInscripcionCreateView, self).get_initial()
        socio_id = self.kwargs.get('pk')
        socio = get_object_or_404(Socio, id=socio_id)
        initial['socio'] = socio
        return initial

    def get_context_data(self, **kwargs):
        context = super(SocioInscripcionCreateView, self).get_context_data(**kwargs)
        socio_id = self.kwargs.get('pk')
        socio = get_object_or_404(Socio, id=socio_id)
        context['socio'] = socio
        return context


class SocioInscripcionDeleteView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Inscripcion
    success_url = reverse_lazy('socios_listado')
    success_message = 'inscripción eliminada!'
    permission_required = 'club.delete_inscripcion'
