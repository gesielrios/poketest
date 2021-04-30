# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

import requests
from django.http import JsonResponse

def index(request):
    return render(request,'core/index.html')

def formulario(request):
    if request.method == 'POST':
        pokemon = request.POST.get('pokemon')
        return redirect('api/pokemon/' + pokemon)

def get_pokemon(request, slug):

    base_url =  'https://pokeapi.co/api/v2/pokemon/'

    if slug:
        url = base_url + slug.lower()
        result = requests.get(url)
        
        if result.status_code == 200:
            all_abilities_json = result.json()['abilities']
            
            result_json = {}
            for ability in all_abilities_json:
                ability_name = ability['ability']['name']
                ability_effect_description_url = ability['ability']['url']

                ability_effect_result = requests.get(ability_effect_description_url)

                if ability_effect_result.status_code == 200:
                    effect_entries = ability_effect_result.json()['effect_entries']

                    for effect_entry in effect_entries:
                        if effect_entry['language']['name'] == 'en':
                            result_json[ability_name] = effect_entry['effect']
            
            sorted_result_json = {}
            
            sorted_keys = list(result_json.keys())
            sorted_keys.sort()
            
            for sorted_key in sorted_keys:
                sorted_result_json[sorted_key] = result_json[sorted_key]
            
            return JsonResponse(
                sorted_result_json
            )
            
    return JsonResponse({'message': 'Pokemon not found or not specified.'})





    

    





