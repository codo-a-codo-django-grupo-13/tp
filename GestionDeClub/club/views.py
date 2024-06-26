from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse, reverse_lazy

from .forms import DisciplinaForm, ProfeForm, SocioForm, InscripcionForm
from .models import Disciplina, Profe, Socio, Inscripcion


def home(request):
    context = {'test': 'Test'}
    return render(request, 'club/home.html', context)


'''#############'''
''' DISCIPLINAS '''

'''
# Descartamos las Vistas basadas en Funciones
def disciplinas_listado(request):
    disciplinas = Disciplina.objects.all()
    print(disciplinas)
    context = {'disciplinas': disciplinas}

    return render(request, 'club/disciplinas_listado.html', context)
'''

class DisciplinaListView(ListView):
    model = Disciplina
    template_name = 'club/disciplinas_listado.html'
    context_object_name = 'disciplinas'

    # Descomentar si en el futuro queremos filtrar los objetos, por ejemplo por Disciplinas Activas
    #def get_queryset(self):
    #    return Disciplina.objects.filter(...)


'''
# Descartamos las Vistas basadas en Funciones
def disciplina_crear(request):
    if request.method == "GET":
        form = DisciplinaForm()

    elif request.method == "POST":
        form = DisciplinaForm(request.POST)

        if form.is_valid():
            disciplina = form.save()
            messages.success(request, f'La Disciplina {disciplina} fue creada con éxito')
            return redirect('disciplinas_listado')

        else:
            for complete_error in form.errors:
                for error in form.errors[complete_error]:
                    messages.error(request, error)

    context = {'form': form}
    return render(request, 'club/disciplina_crear.html', context)
'''

class DisciplinaCreateView(CreateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'club/disciplina_crear.html'
    success_url = reverse_lazy('disciplinas_listado')


    # Descomentar si hay lógica que agregar en el procesamiento del formulario
    #def form_valid(self, form):
    #    return super().form_valid(form)

    # Descomentar si hace falta especificar una redirección con parámetros
    #def get_success_url(self):
    #    return reverse_lazy('disciplinas_listado')


'''
# Descartamos las Vistas basadas en Funciones
def disciplina_modificar(request, disciplina_id):
    disciplina_activa = Disciplina.objects.get(id=disciplina_id)

    if request.method == "GET":
        form = DisciplinaForm(instance=disciplina_activa)

    elif request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina_activa)

        if form.is_valid():
            disciplina = form.save()
            messages.success(request, f'La Disciplina {disciplina} fue modificada con éxito')
            return redirect('disciplinas_listado')

        else:
            for complete_error in form.errors:
                for error in form.errors[complete_error]:
                    messages.error(request, error)

    context = {
        'form': form,
        'disciplina_activa': disciplina_activa}
    return render(request, 'club/disciplina_modificar.html', context)
'''

class DisciplinaUpdateView(UpdateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'club/disciplina_modificar.html'
    success_url = reverse_lazy('disciplinas_listado')

    #def form_valid(self, form):
    #    return super().form_valid(form)

    #def get_success_url(self):
    #    return reverse_lazy('disciplinas_listado')


'''
# Descartamos las Vistas basadas en Funciones
def disciplina_eliminar(request, disciplina_id):
    disciplina_activa = Disciplina.objects.get(id=disciplina_id)

    disciplina_activa.delete()

    messages.success(request, f'La Disciplina {disciplina_activa} fue eliminada con éxito')
    return redirect('disciplinas_listado')
'''

class DisciplinaDeleteView(DeleteView):
    model = Disciplina
    #template_name = 'club/disciplina_confirmacion_eliminar.html'
    success_url = reverse_lazy('disciplinas_listado')

    #def get_success_url(self):
    #    return reverse_lazy('disciplinas_listado')

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


class ProfeCreateView(SuccessMessageMixin, CreateView):
    model = Profe
    form_class = ProfeForm
    template_name = 'club/profe_crear.html'
    success_url = reverse_lazy('profes_listado')
    success_message = 'Profe %(nombre)s %(apellido)s creado!'

class ProfeUpdateView(SuccessMessageMixin, UpdateView):
    model = Profe
    form_class = ProfeForm
    template_name = 'club/profe_modificar.html'
    success_url = reverse_lazy('profes_listado')
    success_message = 'Profe %(nombre)s %(apellido)s actualizado!'

class ProfeDeleteView(SuccessMessageMixin, DeleteView):
    model = Profe
    #template_name = 'club/profe_confirmacion_eliminar.html'
    success_url = reverse_lazy('profes_listado')
    success_message = 'Profe %(nombre)s %(apellido)s eliminado!'

'''########'''
''' SOCIOS '''

class SocioListView(ListView):
    model = Socio
    template_name = 'club/socios_listado.html'
    context_object_name = 'socios'

class SocioCreateView(SuccessMessageMixin, CreateView):
    model = Socio
    form_class = SocioForm
    template_name = 'club/socio_crear.html'
    success_url = reverse_lazy('socios_listado')
    success_message = 'Socio %(nombre)s %(apellido)s creado!'

class SocioUpdateView(SuccessMessageMixin, UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'club/socio_modificar.html'
    success_url = reverse_lazy('socios_listado')
    success_message = 'Socio %(nombre)s %(apellido)s actualizado!'

class SocioDeleteView(SuccessMessageMixin, DeleteView):
    model = Socio
    #template_name = 'club/socio_confirmacion_eliminar.html'
    success_url = reverse_lazy('socios_listado')
    success_message = 'Socio %(nombre)s %(apellido)s eliminado!'


# VISTA PARAMETRIZADA, RECIBE EN EL PARÁMETRO <int:pk> EL ID DEL SOCIO QUE SE QUIERE INSCRIBIR
class SocioInscripcionCreateView(CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'club/inscripcion_a_disciplina.html'
    success_url = reverse_lazy('socios_listado')

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
