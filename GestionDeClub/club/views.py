from django.shortcuts import render, redirect, get_object_or_404
from .models import Socio, Pago
from .forms import SocioForm, PagoForm
from django.db.models import Sum

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

def editar_socio(request, socio_id):
    socio = get_object_or_404(Socio, pk=socio_id)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('estado_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'club/editar_socio.html', {'form': form, 'socio': socio})
def listar_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'club/listar_pagos.html', {'pagos': pagos})

def agregar_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pagos')
    else:
        form = PagoForm()
    return render(request, 'club/agregar_pago.html', {'form': form})

def reporte_pagos(request):
    pagos_totales = Pago.objects.values('socio__nombre').annotate(total=Sum('monto')).order_by('-total')
    return render(request, 'club/reporte_pagos.html', {'pagos_totales': pagos_totales})

def eliminar_socio(request, socio_id):
    socio = get_object_or_404(Socio, pk=socio_id)
    socio.delete()
    return redirect('estado_socios')
