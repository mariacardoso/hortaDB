from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Species, Cultivar, Seed, Seed_Packet
from .forms import SpeciesForm

import locale
# this reads the environment and inits the right locale
locale.setlocale(locale.LC_ALL, "")



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


class SpeciesView(generic.ListView):
    template_name = 'hortadb/species.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        return sorted(Species.objects.all(), key=lambda s: locale.strxfrm(s.common_name)) 


def species_new(request):
    form = SpeciesForm()
    return render(request, 'hortadb/species_edit.html', {
        'form': form})


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
    
