# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .constants import GOOGLE_API_KEY_EMBEDDED
from .forms import GetCityForm
from .helpers import (add_cuisine_description,
                      get_coordinates_from_address,
                      get_location_details_from_coordinates,
                      get_single_restaurant_details)


class RestaurantList(View):
    def get(self, request, city_not_found=False, all_fields_empty=False):
        """displays form and optional errors"""
        form = GetCityForm()
        ctx = {
            'form': form,
            'city_not_found': city_not_found,
            'all_fields_empty': all_fields_empty
        }
        return render(request,
                      template_name='base.html',
                      context=ctx)

    def post(self, request):
        """gets data from form and sends details about location to template"""
        form = GetCityForm(request.POST)
        if form.is_valid():
            """get data from form"""
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            """show error message when all fields are unfilled"""
            if city == '' and street == '':
                return HttpResponseRedirect(reverse('all_fields_empty', kwargs={'all_fields_empty': True}))
            """clear form before displaying again"""
            form = GetCityForm()
            coordinates = get_coordinates_from_address(street, city)
            """show error message when Google API can't find location"""
            if not coordinates:
                return HttpResponseRedirect(reverse('restaurant_not_found', kwargs={'city_not_found': True}))
            """get details about found location and send it to template"""
            location_details = get_location_details_from_coordinates(coordinates['lon'], coordinates['lat'])
            """show error message when Zomato API can't find location"""
            if not location_details:
                return HttpResponseRedirect(reverse('restaurant_not_found', kwargs={'city_not_found': True}))
            city_top_cuisines_with_description = \
                add_cuisine_description(location_details['popularity']['top_cuisines'])
            ctx = {'form': form,
                   'city_top_cuisines_with_description': city_top_cuisines_with_description,
                   'location_details': location_details}
            return render(request,
                          template_name='restaurant_list.html',
                          context=ctx)


class RestaurantDetails(View):
    def get(self, request, restaurant_id):
        """gets restaurant ID and sends details about restaurant to template"""
        form = GetCityForm()
        restaurant_details = get_single_restaurant_details(restaurant_id)
        ctx = {'form': form,
               'restaurant': restaurant_details,
               'api_key': GOOGLE_API_KEY_EMBEDDED}
        return render(request,
                      template_name='restaurant_details.html',
                      context=ctx)
