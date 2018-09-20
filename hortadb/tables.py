import django_tables2 as tables
import itertools


from .models import Species

class SpeciesTable(tables.Table):
    binomial_name = tables.Column(order_by=('genus', 'species', 'subspecies'))

    class Meta:
        model = Species
        exclude = ('species', 'subspecies', 'id')
        sequence = ('common_name', 'binomial_name', 'order', 'family', 'genus')
        template_name = 'django_tables2/bootstrap.html'
