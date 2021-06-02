from django.test import TestCase
from django.urls import reverse
import json

class CoreViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.success_response_for_pokemon_ditto = json.dumps({
            "imposter": "This Pokémon transforms into a random opponent upon entering battle.  This effect is identical to the move transform.",
            "limber": "This Pokémon cannot be paralyzed.\n\nIf a Pokémon is paralyzed and acquires this ability, its paralysis is healed; this includes when regaining a lost ability upon leaving battle."
        })
        cls.failure_response_for_pokemon_ditto = json.dumps({'message': 'Pokemon not found or not specified.'})

    def test_load_index_page(self):    
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
    
    def test_success_endpoint(self):    
        response = self.client.get('/api/pokemon/ditto')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            json.dumps(response.json()), 
            self.success_response_for_pokemon_ditto
        )
    
    def test_failure_endpoint(self):    
        response = self.client.get('/api/pokemon/JohnDoe')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            json.dumps(response.json()), 
            self.failure_response_for_pokemon_ditto
        )
    
    def test_success_form_submit(self):
        response = self.client.post('/form_submit', data={'pokemon': 'ditto'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse('core:get_pokemon', kwargs={'slug': 'ditto'})
        )
    
    def test_failure_form_submit(self):
        response = self.client.get('/form_submit', data={'pokemon': 'ditto'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,reverse('core:index'))