from django.shortcuts import render


def star_home(request):

    return render(request, 'star/star_home.html', {'star': star})