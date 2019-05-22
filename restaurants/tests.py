from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from .forms import GetCityForm


class MainTests(TestCase):

    def test_restaurant_form(self):
        response = self.client.get(reverse('restaurant-list'))
        self.assertEquals(response.status_code, 200)

        form = GetCityForm()
        self.assertFalse(form.is_valid())

        data = {'city': '', 'street': ''}
        form = GetCityForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'city': ['To pole jest wymagane.'],
            'street': ['To pole jest wymagane.']
        })

        data = {
            'city': 'Warszawa',
            'street': 'Aleje Jerozolimskie'
        }
        form = GetCityForm(data=data)
        self.assertTrue(form.is_valid())

    def test_restaurant_list_valid(self):
        response = self.client.post(
            reverse('restaurant-list'),
            {'city': 'Warszawa', 'street': 'Aleje Jerozolimskie'}
        )
        self.assertIsNotNone(response.context.get('location_details'))
        self.assertIsNotNone(response.context.get('city_top_cuisines_with_description'))
        self.assertEquals(response.status_code, 200)

    def test_restaurant_list_non_existent_city(self):
        response = self.client.post(
            reverse('restaurant-list'),
            {'city': 'NonExistentCity123123123', 'street': 'NonExistentStreet123123123'}
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response['location'], '/pl/restaurant_list')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].message, 'Location not found')
