import requests

from .constants import GOOGLE_API_KEY_GEOCODING, RESTAURANT_API_KEY
from .dictionary import DESCRIPTION


def get_coordinates_from_address(street=None, city=None):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={},+{}&key={}".format(
        street, city, GOOGLE_API_KEY_GEOCODING
    )
    api_response = requests.get(url)
    api_result = api_response.json()
    if api_result['status'] == 'ZERO_RESULTS':
        return None
    return {
        'lat': api_result['results'][0]['geometry']['location']['lat'],
        'lon': api_result['results'][0]['geometry']['location']['lng']
    }


def get_location_details_from_coordinates(coordinates):
    url = 'https://developers.zomato.com/api/v2.1/geocode?lat={lat}&lon={lon}'.format(
        lat=coordinates['lat'],
        lon=coordinates['lon'],
    )
    headers = {
        "User-agent": "curl/7.43.0", "Accept": "application/json",
        "user_key": "{}".format(RESTAURANT_API_KEY)
    }
    api_response = requests.get(url, headers=headers)
    location_details = api_response.json()
    if location_details.get('status') == 'Bad Request':
        return None
    return location_details


def get_single_restaurant_details(restaurant_id):
    location_url = "https://developers.zomato.com/api/v2.1/restaurant?res_id={}".format(restaurant_id)
    headers = {
        "User-agent": "curl/7.43.0", "Accept": "application/json",
        "user_key": "{}".format(RESTAURANT_API_KEY)
    }
    details_response = requests.get(location_url, headers=headers)
    return details_response.json()


def add_cuisine_description(cuisines_list):
    cuisines_with_description = []
    for cuisine in cuisines_list:
        cuisine_str = cuisine.upper().replace(' ', '_')
        if cuisine_str in DESCRIPTION.keys():
            description = DESCRIPTION[cuisine_str]
        else:
            description = 'No description found'
        cuisines_with_description.append({'name': cuisine, 'description': description})
    return cuisines_with_description
