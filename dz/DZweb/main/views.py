from django.shortcuts import render


def gipsy(request):
    data = {
        'title': 'Главная страница',
        'array': [''],
    }

    return render(request, 'main/gipsy.html', data)

def lv(request):
    return render(request, 'main/lv.html')