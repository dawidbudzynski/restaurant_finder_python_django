from decouple import config

RESTAURANT_API_KEY = config('restaurant_api_key', cast=str)
GOOGLE_API_KEY = config('google_api_key', cast=str)
