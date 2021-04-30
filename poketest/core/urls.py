from django.urls import path
from . import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('formulario', v.formulario, name='formulario'),
    path('api/pokemon/<slug:slug>', v.get_pokemon, name='get_pokemon'),
    
]