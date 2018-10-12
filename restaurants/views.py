# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .constants import GOOGLE_API_KEY
from .forms import GetCityForm
from .helpers import (add_cuisine_description,
                      get_city_id, get_city_details,
                      get_restaurants_details,
                      get_single_restaurant_details)


class RestaurantList(View):
    def get(self, request, city_found=True):
        form = GetCityForm()
        ctx = {
            'form': form,
            'city_found': city_found
        }
        return render(request,
                      template_name='base.html',
                      context=ctx)

    def post(self, request):
        form = GetCityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            city_basic_info = get_city_id(city_name)
            if not city_basic_info:
                return HttpResponseRedirect(reverse('restaurant_not_found', kwargs={'city_found': False}))
            city_details = get_city_details(city_basic_info['entity_id'], city_basic_info['entity_type'])
            city_name = city_details['city']
            city_top_cuisines = add_cuisine_description(city_details['top_cuisines'])
            nearby_restaurants = city_details['nearby_res']
            ctx = {'form': form,
                   'city_name': city_name,
                   'city_top_cuisines': city_top_cuisines,
                   'all_restaurants_details': get_restaurants_details(nearby_restaurants)}
            return render(request,
                          template_name='restaurant_list.html',
                          context=ctx)


class RestaurantDetails(View):
    def get(self, request, restaurant_id):
        form = GetCityForm()
        restaurant_details = get_single_restaurant_details(restaurant_id)
        ctx = {'form': form,
               'restaurant': restaurant_details,
               'api_key': GOOGLE_API_KEY}
        return render(request,
                      template_name='restaurant_details.html',
                      context=ctx)
