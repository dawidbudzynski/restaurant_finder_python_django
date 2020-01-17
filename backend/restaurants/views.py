from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import View
from rest_framework import status, views
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
        if not coordinates:
            """Google Geocoding API could't find location"""
            content = {'Google Geocoding error': 'Google Geocoding API could\'t find location'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        location_details = get_location_details_from_coordinates(coordinates)
        if not location_details:
            """Zomato API could't find information about restaurants"""
            content = {'Zomato API error': 'Zomato API API could\'t find information about restaurants'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        restaurant_data = self.prepare_restaurants_data(location_details['nearby_restaurants'])
        serialized_data = RestaurantsSerializer(restaurant_data, many=True).data
        return Response(serialized_data)

    @staticmethod
    def prepare_restaurants_data(raw_restaurant_data):
        restaurant_data = []
        for restaurant in raw_restaurant_data:
            restaurant = restaurant['restaurant']
            restaurant_data.append({
                'id': restaurant['id'],
                'name': restaurant['name'],
                'cuisines': restaurant['cuisines'],
                'address': restaurant['location']['address'],
                'city_district': restaurant['location']['locality'],
                'featured_image': restaurant['featured_image'],
                'rating': restaurant['user_rating']['aggregate_rating'],
                'average_cost_for_two': restaurant['average_cost_for_two']
            })
        return restaurant_data


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
