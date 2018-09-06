from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Cultivar, Species


class IndexView(generic.ListView):
    template_name = 'hortadb/index.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        return Species.objects.order_by('family')[:5]


class DetailView(generic.DetailView):
    model = Species
    template_name = 'hortadb/detail.html'

    def get_queryset(self):
        """
        Excludes any species that aren't published yet.
        """
        return Species.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Species
    template_name = 'hortadb/results.html'
    

def vote(request, species_id):
    species = get_object_or_404(Species, pk=species_id)
    try:
        selected_cultivar = species.cultivar_set.get(pk=request.POST['cultivar'])
    except (KeyError, Cultivar.DoesNotExist):
        # Redisplay the cultivar voting form.
        return render(request, 'hortadb/detail.html', {
            'species': species,
            'error_message': "You didn't select a variety.",
        })
    else:
        selected_cultivar.votes += 1
        selected_cultivar.save()
        return HttpResponseRedirect(reverse('hortadb:results', args=(species.id,)))