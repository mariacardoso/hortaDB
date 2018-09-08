from django.urls import path
from . import views

app_name = 'hortadb'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('tiago/', views.tiago, name='tiago'),
    
    path('species/', views.SpeciesView.as_view(), name='species'),
    #path('species/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('species/<int:sid>/', views.detail, name='detail'),
]