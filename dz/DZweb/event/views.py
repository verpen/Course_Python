import json
from django.shortcuts import render
from .models import Part
from .forms import PartForm
from django.views.generic import DetailView
from .models import Rating


def event_home(request):
    event = Part.objects.order_by('title')
    return render(request, 'event/event_home.html', {'event': event})


class EventDetailView(DetailView):
    model = Part
    template_name = 'event/details_view.html'
    context_object_name = 'cinema'


def rating(request):
    hvar = 'rating'
    films = Rating.objects.all()
    result = 0.0
    for film in films:
        result += float(film.ozenka)
    result /= films.count()
    res_string = str(result)
    return render(request, 'event/rating.html', {'result': res_string})


def create(request):
    form = PartForm()
    data = {
        'form': form
    }
    return render(request, 'event/create.html', data)
