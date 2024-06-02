from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DisciplinaForm
from .models import Disciplina


def home(request):
    context = {'test': 'Test'}
    return render(request, 'club/home.html', context)


def disciplinas_listado(request):
    disciplinas = Disciplina.objects.all()
    print(disciplinas)
    context = {'disciplinas': disciplinas}
    return render(request, 'club/disciplinas_listado.html', context)

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

def disciplina_eliminar(request, disciplina_id):
    disciplina_activa = Disciplina.objects.get(id=disciplina_id)

    disciplina_activa.delete()

    messages.success(request, f'La Disciplina {disciplina_activa} fue eliminada con éxito')
    return redirect('disciplinas_listado')

def profesores(request):
    context = {'test': 'Test'}
    return render(request, 'club/profesores.html', context)


def socios(request):
    context = {'test': 'Test'}
    return render(request, 'club/socios.html', context)