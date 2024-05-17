from django.shortcuts import render


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
