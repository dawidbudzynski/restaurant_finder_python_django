import requests

from .constants import RESTAURANT_API_KEY, GOOGLE_API_KEY
from .dictionary import DESCRIPTION


def get_coordinates_from_address(number=None, street=None, city=None):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={}+{},+{}&key={}".format(
        number, street, city, GOOGLE_API_KEY)
    api_response = requests.get(url)
    api_result = api_response.json()
    if api_result['status'] == 'ZERO_RESULTS':
        return None
    coordinates = {'lat': api_result['results'][0]['geometry']['location']['lat'],
                   'lon': api_result['results'][0]['geometry']['location']['lng']}
    return coordinates


def get_location_details_from_coordinates(lon, lat):
    url = 'https://developers.zomato.com/api/v2.1/geocode?lat={}&lon={}'.format(lat, lon)
    headers = {"User-agent": "curl/7.43.0", "Accept": "application/json",
               "user_key": "{}".format(RESTAURANT_API_KEY)}
    api_response = requests.get(url, headers=headers)
    location_details = api_response.json()
    if location_details.get('status') == 'Bad Request':
        return None
    return location_details


def get_single_restaurant_details(restaurant_id):
    location_url = "https://developers.zomato.com/api/v2.1/restaurant?res_id={}".format(restaurant_id)
    headers = {"User-agent": "curl/7.43.0", "Accept": "application/json",
               "user_key": "{}".format(RESTAURANT_API_KEY)}
    details_response = requests.get(location_url, headers=headers)
    restaurant_details = details_response.json()
    return restaurant_details


def add_cuisine_description(cuisines_list):
    cuisines_with_description = []
    for cuisine in cuisines_list:
        cuisine_as_string = cuisine.upper().replace(' ', '_')
        if cuisine_as_string in DESCRIPTION.keys():
            description = DESCRIPTION[cuisine_as_string]
        else:
            description = 'No description found'
        cuisines_with_description.append({'name': cuisine, 'description': description})
    return cuisines_with_description
