import requests

from decouple import config

RESTAURANT_API_KEY = config('restaurant_api_key')
IP_API_KEY = config('ip_api_key')


def get_city_id(city_name):
    location_url = "https://developers.zomato.com/api/v2.1/locations?query={}".format(city_name)
    headers = {"User-agent": "curl/7.43.0", "Accept": "application/json",
               "user_key": "{}".format(RESTAURANT_API_KEY)}
    city_response = requests.get(location_url, headers=headers)
    city_info = city_response.json()
    entity_type = city_info['location_suggestions'][0]['entity_type']
    entity_id = city_info['location_suggestions'][0]['entity_id']
    return [entity_id, entity_type]


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
