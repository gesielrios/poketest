import requests
from django.http import JsonResponse

def get_pokemon(request):

    base_url =  'https://pokeapi.co/api/v2/pokemon/'
    pokemon = request.GET.get('pokemon')

    if pokemon:
        url = base_url + pokemon
        result = requests.get(url)
        
        if result.status_code == 200:
            abilities = result.json()['abilities']
            abilities_result = []

            for ability in abilities:
                abilities_result.append(ability['ability']['name'])

            abilities_result.sort()

            return JsonResponse(
                {
                    'pokemon': pokemon,
                    'abilities': abilities_result
                }
            )
            
    return JsonResponse({'message': 'Pokemon not found.'})





    

    





