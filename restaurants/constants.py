from decouple import config

RESTAURANT_API_KEY = config('RESTAURANT_API_KEY', cast=str)
GOOGLE_API_KEY = config('GOOGLE_API_KEY', cast=str)
