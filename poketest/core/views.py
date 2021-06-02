# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from .service import get_pokemon_from_pokeapi

def index(request):
    return render(request,'core/index.html')

def form_submit(request):
    if request.method == 'POST':
        pokemon = request.POST.get('pokemon')
        return redirect('api/pokemon/' + pokemon)
    
    messages.warning(request, "It is necessary to specify the pokemon to discover its abilities.")
    return redirect('/')

def get_pokemon(request, slug):
    if slug:
        sorted_result_json = get_pokemon_from_pokeapi(slug)
        if sorted_result_json is not None:
            
            return JsonResponse(
                sorted_result_json
            )
            
    return JsonResponse({'message': 'Pokemon not found or not specified.'})





    

    





