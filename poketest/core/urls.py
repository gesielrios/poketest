from django.urls import path
from . import views as v

app_name = 'core'

urlpatterns = [
    path('', v.get_pokemon, name='get_pokemon'),
]