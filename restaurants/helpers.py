import requests

from .constants import RESTAURANT_API_KEY
from .dictionary import DESCRIPTION


def get_city_id(city_name):
    location_url = "https://developers.zomato.com/api/v2.1/locations?query={}".format(city_name)
    headers = {"User-agent": "curl/7.43.0", "Accept": "application/json",
               "user_key": "{}".format(RESTAURANT_API_KEY)}
    city_response = requests.get(location_url, headers=headers)
    city_info = city_response.json()
    if not city_info['location_suggestions']:
        return False
    result = {
        'entity_id': city_info['location_suggestions'][0]['entity_id'],
        'entity_type': city_info['location_suggestions'][0]['entity_type']
    }
    return result


def get_city_details(city_id, city_type):
    location_url = \
        "https://developers.zomato.com/api/v2.1/location_details?entity_id={}&entity_type={}".format(
            city_id, city_type)
    headers = {"User-agent": "curl/7.43.0", "Accept": "application/json",
               "user_key": "{}".format(RESTAURANT_API_KEY)}
    city_response = requests.get(location_url, headers=headers)
    return city_response.json()


def get_restaurants_details(all_restaurants):
    all_restaurants_details = []
    for restaurant_id in all_restaurants:
        location_url = "https://developers.zomato.com/api/v2.1/restaurant?res_id={}".format(restaurant_id)
        headers = {"User-agent": "curl/7.43.0", "Accept": "application/json",
                   "user_key": "{}".format(RESTAURANT_API_KEY)}
        details_response = requests.get(location_url, headers=headers)
        restaurant_details_single = details_response.json()
        all_restaurants_details.append(restaurant_details_single)
    return all_restaurants_details


def get_single_restaurant_details(restaurant_id):
    location_url = "https://developers.zomato.com/api/v2.1/restaurant?res_id={}".format(restaurant_id)
    headers = {"User-agent": "curl/7.43.0", "Accept": "application/json",
               "user_key": "{}".format(RESTAURANT_API_KEY)}
    details_response = requests.get(location_url, headers=headers)
    return details_response.json()


def add_cuisine_description(cuisines_list):
    cuisines_with_description = []
    for cuisine in cuisines_list:
        cuisine_as_string = cuisine.upper().replace(' ', '_')
        print(cuisine_as_string)
        if cuisine_as_string in DESCRIPTION.keys():
            description = DESCRIPTION[cuisine_as_string]
        else:
            description = 'No food description found'
        cuisines_with_description.append({'name': cuisine, 'description': description})
    return cuisines_with_description
