from django.urls import path
from . import views as v

app_name = 'core'

urlpatterns = [
    path('<slug:slug>', v.get_pokemon, name='get_pokemon'),
]