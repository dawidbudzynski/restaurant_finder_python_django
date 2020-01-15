from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import View
from rest_framework import views
from rest_framework.response import Response

from .constants import GOOGLE_API_KEY_EMBEDDED
from .forms import GetCityForm
from .helpers import (
    add_cuisine_description,
    get_coordinates_from_address,
    get_location_details_from_coordinates,
    get_single_restaurant_details
)
from .serializers import RestaurantsSerializer


class GetRestaurantListAPIView(views.APIView):

    def get(self, request, city, street):
        coordinates = get_coordinates_from_address(city, street)
        location_details = get_location_details_from_coordinates(coordinates)
        nearby_restaurant_list = location_details['nearby_restaurants']
        restaurant_data = []
        for restaurant in nearby_restaurant_list:
            restaurant = restaurant['restaurant']
            restaurant_data.append({
                'id': restaurant['id'],
                'name': restaurant['name'],
                'featured_image': restaurant['featured_image']
            })
        results = RestaurantsSerializer(restaurant_data, many=True).data
        return Response(results)


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
