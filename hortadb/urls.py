from django.urls import path
from . import views

app_name = 'hortadb'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

    # SPECIES

    path('species/', views.SpeciesView.as_view(), name='species'),
    path('species/<int:sid>/', views.detail, name='detail'),
    path('species/new/', views.species_new, name='species_new'),
    #path('species/', views.species, name='species'),
    #path('species/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # CULTIVARS

    path('cultivar/<int:cid>/', views.cultivar, name='cultivar'),

    # RESOURCES

    path('resources', views.resources, name='resources'),

    # tiago

    path('tiago/', views.tiago, name='tiago'),

]