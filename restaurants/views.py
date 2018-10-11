# Create your views here.

from decouple import config
from django.shortcuts import render
from django.views import View

from .forms import GetCityForm
from .helpers import get_city_id, get_city_details, get_restaurants_details

RESTAURANT_API_KEY = config('restaurant_api_key')
IP_API_KEY = config('ip_api_key')


class RestaurantList(View):
    def get(self, request):
        form = GetCityForm()
        ctx = {
            'form': form
        }

        return render(request,
                      template_name='restaurant_search.html',
                      context=ctx)

    def post(self, request):
        form = GetCityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            city_id_and_type = get_city_id(city_name)
            city_info = get_city_details(city_id_and_type[0], city_id_and_type[1])
            city_name = city_info['city']
            city_top_cuisines = city_info['top_cuisines']
            nearby_restaurants = city_info['nearby_res']
            ctx = {'form': form,
                   'city_name': city_name,
                   'city_top_cuisines': city_top_cuisines,
                   'all_restaurants_details': get_restaurants_details(nearby_restaurants)}
            return render(request,
                          template_name='restaurant_details.html',
                          context=ctx)
