# -*- coding: utf-8 -*-
import requests

def get_pokemon_from_pokeapi(pokemon):
    if pokemon:
        base_url = 'https://pokeapi.co/api/v2/pokemon/'

        url = base_url + pokemon.lower()
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
            
            sorted_keys = list(result_json.keys())
            sorted_keys.sort()
            
            sorted_result_json = { sorted_key: result_json[sorted_key] for sorted_key in sorted_keys }
                
            return sorted_result_json


    return None