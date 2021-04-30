from django.urls import path
from . import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('form_submit', v.form_submit, name='form_submit'),
    path('api/pokemon/<slug:slug>', v.get_pokemon, name='get_pokemon'),
    
]