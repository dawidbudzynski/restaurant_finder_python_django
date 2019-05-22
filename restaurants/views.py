from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.utils.translation import ugettext as _

from .constants import GOOGLE_API_KEY_EMBEDDED
from .forms import GetCityForm
from .helpers import (
    add_cuisine_description,
    get_coordinates_from_address,
    get_location_details_from_coordinates,
    get_single_restaurant_details
)


class RestaurantListView(View):
    def get(self, request):
        return render(
            request,
            template_name='base.html',
            context={'form': GetCityForm()}
        )

    def post(self, request):
        form = GetCityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            coordinates = get_coordinates_from_address(street, city)
            if not coordinates:
                """Google Geocoding API can't find location"""
                messages.add_message(request, messages.WARNING, _('Location not found'))
                return HttpResponseRedirect(reverse('restaurant-list'))
            location_details = get_location_details_from_coordinates(coordinates)
            if not location_details:
                """Zomato API can't find location"""
                messages.add_message(request, messages.WARNING, _('No restaurants found'))
                return HttpResponseRedirect(reverse('restaurant-list'))
            ctx = {
                'form': form,
                'location_details': location_details,
                'city_top_cuisines_with_description': add_cuisine_description(
                    location_details['popularity']['top_cuisines']
                )
            }
            return render(
                request,
                template_name='restaurant_list.html',
                context=ctx
            )


class RestaurantDetailsView(View):
    def get(self, request, restaurant_id):
        """gets restaurant ID and sends details about restaurant to template"""
        ctx = {
            'form': GetCityForm(),
            'restaurant': get_single_restaurant_details(restaurant_id),
            'api_key': GOOGLE_API_KEY_EMBEDDED
        }
        return render(
            request,
            template_name='restaurant_details.html',
            context=ctx
        )
