from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DisciplinaForm


def home(request):
    context = {
        'test': 'Test',
    }
    return render(request, 'club/home.html', context)

def disciplinas(request):
    disciplinas = {
        'Fútbol',
        'Baloncesto',
        'Natación',
        'Tenis',
        'Atletismo',
        'Artes Marciales',
        'Ciclismo',
        'Gimnasio',
        'Boxeo',
    }

    context = {
        'disciplinas': disciplinas,
    }
    return render(request, 'club/disciplinas.html', context)

def profesores(request):
    context = {
        'test': 'Test',
    }
    return render(request, 'club/profesores.html', context)

def socios(request):
    context = {
        'test': 'Test',
    }
    return render(request, 'club/socios.html', context)


def disciplina_crear(request):
    if request.method == "GET":
        form = DisciplinaForm()
    
    elif request.method == "POST":
        form = DisciplinaForm(request.POST)
        
        if form.is_valid():            
            messages.success(request, 'El alumno fue dado de alta con éxito')

            return redirect('disciplinas')

    context = {
        'form': form,
    }
    return render(request, 'club/disciplina_crear.html', context)
