from django.shortcuts import render


def home(request):
    context = {
        'test': 'Test',
    }

    return render(request, 'club/home.html', context)