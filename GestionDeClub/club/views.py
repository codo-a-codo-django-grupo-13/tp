from django.shortcuts import render, redirect
from .forms import SocioForm
from .models import Socio

def home(request):
    context = {
        'test': 'Test',
    }

    return render(request, 'club/home.html', context)


def disciplinas(request):
    context = {
        'test': 'Test',
    }

    return render(request, 'club/disciplinas.html', context)

def socios(request):
    context = {
        'test': 'Test',
    }

    return render(request, 'club/socios.html', context)

# club/views.py
def inscripcion_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estado_socios')
    else:
        form = SocioForm()
    return render(request, 'club/inscripcion_socio.html', {'form': form})

def estado_socios(request):
    socios = Socio.objects.all()
    return render(request, 'club/estado_socios.html', {'socios': socios})