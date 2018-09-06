from django.contrib import admin

from django.utils.html import format_html

from .models import Species, Cultivar, Seed, Seed_Packet

## SEED PACKETS

class SeedPacketInLine(admin.TabularInline):
    model  = Seed_Packet
    fields = ('date_packing', 'date_validity', 'weight')
    extra  = 0


## SEEDS

class SeedInLine(admin.TabularInline):
    model = Seed
    extra = 0
    show_change_link = True

    fieldset = [
        (None, {
            'fields': ('plant_seed', 'brand',)
        }),
        ('Date information', {
            'classes': ('collapse',),
            'fields': [('date_sowo_ini', 'date_sowo_end'),
                       ('date_sowi_ini', 'date_sowi_end'),
                       ('date_tran_ini', 'date_tran_end'),
                       ('date_harv_ini', 'date_harv_end'),
            ]
        }),
    ]
    

class SeedAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('plant_seed', 'brand',),
        }),
        ('Season information', {
            'classes': ('collapse',),
            'fields': [('date_sowo_ini', 'date_sowo_end'),
                       ('date_sowi_ini', 'date_sowi_end'),
                       ('date_tran_ini', 'date_tran_end'),
                       ('date_harv_ini', 'date_harv_end'),
            ]
        }),
    ]
    inlines = [SeedPacketInLine]
    list_display = ['plant_seed', 'brand', 'get_seed_name', 'get_seed_variety', 'brand', 'get_seed_species']
    list_display_links = ('get_seed_name', 'get_seed_variety')
    

    def get_seed_species(self, obj):
        return obj.plant_seed.species.species
    get_seed_species.short_description = ('species')

    def get_seed_name(self, obj):
        return obj.plant_seed.species.common_name
    get_seed_name.short_description = ('common name')

    def get_seed_variety(self, obj):
        return obj.plant_seed.variety
    get_seed_variety.short_description = ('variety')

## CULTIVARS

class CultivarInLine(admin.TabularInline):
    model  = Cultivar
    fields = ('variety', 'life_cycle')
    extra  = 0
    show_change_link = True


class CultivarAdmin(admin.ModelAdmin):
    fields       = ('species', 'variety', 'life_cycle')
    inlines      = [SeedInLine]
    list_display = ('get_name', 'variety', 'get_species', 'life_cycle',)
    list_display_links = ['variety']
    list_filter  = ['species__species']

## SPECIES

class SpeciesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': (('common_name', 'species'),)
        }),
        ('Taxonomy information', {
            'classes': ('collapse',),
            'fields': ('order', 'family', 'genus', ),
        }),
    ]
    inlines = [CultivarInLine]
    list_display  = ('common_name', 'species', 'genus', 'family', 'count_varieties',)
    list_filter   = ['family']
    search_fields = ['common_name']

    def count_varieties(self, obj):
        """
        Returns the number of varieties of a given species.
        """
        return obj.cultivar_set.count()
    count_varieties.short_description = ('Number of varieties')
    

admin.site.register(Cultivar, CultivarAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Seed, SeedAdmin)
