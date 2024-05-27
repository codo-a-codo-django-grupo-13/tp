from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DisciplinaForm


def home(request):
    context = {'test': 'Test'}
    return render(request, 'club/home.html', context)


def disciplinas_listado(request):
    disciplinas = {
        1: {'id': 1, 'nombre': 'Fútbol', 'cuota': 8000},
        2: {'id': 2, 'nombre': 'Baloncesto', 'cuota': 6000},
        3: {'id': 3, 'nombre': 'Natación', 'cuota': 13000},
        4: {'id': 4, 'nombre': 'Tenis', 'cuota': 12000},
        5: {'id': 5, 'nombre': 'Atletismo', 'cuota': 8000},
        6: {'id': 6, 'nombre': 'Artes Marciales', 'cuota': 7000},
        7: {'id': 7, 'nombre': 'Ciclismo', 'cuota': 6000},
        8: {'id': 8, 'nombre': 'Gimnasio', 'cuota': 6000},
        9: {'id': 9, 'nombre': 'Boxeo', 'cuota': 9000}}

    context = {'disciplinas': disciplinas}
    return render(request, 'club/disciplinas_listado.html', context)

def disciplina_crear(request):
    disciplinas = {
        1: {'id': 1, 'nombre': 'Fútbol', 'cuota': 8000},
        2: {'id': 2, 'nombre': 'Baloncesto', 'cuota': 6000},
        3: {'id': 3, 'nombre': 'Natación', 'cuota': 13000},
        4: {'id': 4, 'nombre': 'Tenis', 'cuota': 12000},
        5: {'id': 5, 'nombre': 'Atletismo', 'cuota': 8000},
        6: {'id': 6, 'nombre': 'Artes Marciales', 'cuota': 7000},
        7: {'id': 7, 'nombre': 'Ciclismo', 'cuota': 6000},
        8: {'id': 8, 'nombre': 'Gimnasio', 'cuota': 6000},
        9: {'id': 9, 'nombre': 'Boxeo', 'cuota': 9000}}
    
    if request.method == "GET":
        form = DisciplinaForm()
    
    elif request.method == "POST":
        form = DisciplinaForm(request.POST)
        
        if form.is_valid():
            messages.success(request, 'La Disciplina fue hipotéticamente creada con éxito')
            return redirect('disciplinas_listado')

        else:
            for complete_error in form.errors:
                for error in form.errors[complete_error]:
                    messages.error(request, error)

    context = {'form': form}
    return render(request, 'club/disciplina_crear.html', context)

def disciplina_modificar(request, disciplina_id):
    disciplinas = {
        1: {'id': 1, 'nombre': 'Fútbol', 'cuota': 8000},
        2: {'id': 2, 'nombre': 'Baloncesto', 'cuota': 6000},
        3: {'id': 3, 'nombre': 'Natación', 'cuota': 13000},
        4: {'id': 4, 'nombre': 'Tenis', 'cuota': 12000},
        5: {'id': 5, 'nombre': 'Atletismo', 'cuota': 8000},
        6: {'id': 6, 'nombre': 'Artes Marciales', 'cuota': 7000},
        7: {'id': 7, 'nombre': 'Ciclismo', 'cuota': 6000},
        8: {'id': 8, 'nombre': 'Gimnasio', 'cuota': 6000},
        9: {'id': 9, 'nombre': 'Boxeo', 'cuota': 9000}}
    
    disciplina_activa = disciplinas[disciplina_id]

    if request.method == "GET":
        form = DisciplinaForm(initial={'nombre': disciplina_activa['nombre'], 'cuota': disciplina_activa['cuota']})
    
    elif request.method == "POST":
        form = DisciplinaForm(request.POST)
        
        if form.is_valid():
            messages.success(request, 'La Disciplina fue modificada con éxito')
            return redirect('disciplinas_listado')
        
        else:
            for complete_error in form.errors:
                for error in form.errors[complete_error]:
                    messages.error(request, error)

    context = {
        'form': form,
        'disciplina_activa': disciplina_activa}
    return render(request, 'club/disciplina_modificar.html', context)


def profesores(request):
    context = {'test': 'Test'}
    return render(request, 'club/profesores.html', context)


def socios(request):
    context = {'test': 'Test'}
    return render(request, 'club/socios.html', context)