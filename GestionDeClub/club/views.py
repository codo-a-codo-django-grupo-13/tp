from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DisciplinaForm


def home(request):
    context = {'test': 'Test'}
    return render(request, 'club/home.html', context)


def disciplinas(request):
    disciplinas = {
        1: {'nombre': 'Fútbol', 'cuota': 8000},
        2: {'nombre': 'Baloncesto', 'cuota': 6000},
        3: {'nombre': 'Natación', 'cuota': 13000},
        4: {'nombre': 'Tenis', 'cuota': 12000},
        5: {'nombre': 'Atletismo', 'cuota': 8000},
        6: {'nombre': 'Artes Marciales', 'cuota': 7000},
        7: {'nombre': 'Ciclismo', 'cuota': 6000},
        8: {'nombre': 'Gimnasio', 'cuota': 6000},
        9: {'nombre': 'Boxeo', 'cuota': 9000}}

    context = {'disciplinas': disciplinas}
    return render(request, 'club/disciplinas.html', context)

def disciplina_crear(request):
    if request.method == "GET":
        form = DisciplinaForm()
    
    elif request.method == "POST":
        form = DisciplinaForm(request.POST)
        
        if form.is_valid():            
            messages.success(request, 'La Disciplina fue dado de alta con éxito')

            return redirect('disciplinas')

    context = {'form': form}
    return render(request, 'club/disciplina_crear.html', context)

def disciplina_editar(request, disciplina_id):
    disciplinas = {
        1: {'nombre': 'Fútbol', 'cuota': 8000},
        2: {'nombre': 'Baloncesto', 'cuota': 6000},
        3: {'nombre': 'Natación', 'cuota': 13000},
        4: {'nombre': 'Tenis', 'cuota': 12000},
        5: {'nombre': 'Atletismo', 'cuota': 8000},
        6: {'nombre': 'Artes Marciales', 'cuota': 7000},
        7: {'nombre': 'Ciclismo', 'cuota': 6000},
        8: {'nombre': 'Gimnasio', 'cuota': 6000},
        9: {'nombre': 'Boxeo', 'cuota': 9000}}
    
    disciplina = disciplinas[disciplina_id]

    if request.method == "GET":
        form = DisciplinaForm(initial={'nombre': disciplina['nombre'], 'cuota': disciplina['cuota']})
    
    elif request.method == "POST":
        form = DisciplinaForm(request.POST)
        
        if form.is_valid():            
            messages.success(request, 'El alumno fue dado de alta con éxito')

            return redirect('disciplinas')

    context = {'form': form}
    return render(request, 'club/disciplina_editar.html', context)


def profesores(request):
    context = {'test': 'Test'}
    return render(request, 'club/profesores.html', context)


def socios(request):
    context = {'test': 'Test'}
    return render(request, 'club/socios.html', context)