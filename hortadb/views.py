from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Species, Cultivar, Seed, Seed_Packet


class IndexView(generic.ListView):
    template_name = 'hortadb/index.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        return Species.objects.order_by('family')


class DetailView(generic.DetailView):
    model = Species, Cultivar, Seed
    template_name = 'hortadb/detail.html'

    def get_queryset(self):
        """
        Excludes any species that aren't published yet.
        """
        return Species.objects.all()
    
    def get_range(self):
        return range(1,12)


class SpeciesView(generic.ListView):
    template_name = 'hortadb/species.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        return Species.objects.order_by('family')


def cultivar(request, cid):
    return render(request, 'hortadb/cultivar.html', {
        'cultivar': Cultivar.objects.get(pk=cid),
        'months':   list(range(1,13)),
    })


# tiago

def tiago(request):
    return render(request, 'tiago.html', {
        'species': Species.objects.all()
    })

def detail(request, sid):
    
    return render(request, 'hortadb/detail.html', {
        'species': Species.objects.get(pk=sid),
        'months':  list(range(1,13)),
    })
