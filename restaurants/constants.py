from decouple import config

RESTAURANT_API_KEY = config('RESTAURANT_API_KEY', cast=str)
GOOGLE_API_KEY_EMBEDDED = config('GOOGLE_API_KEY_EMBEDDED', cast=str)
GOOGLE_API_KEY_GEOCODING = config('GOOGLE_API_KEY_GEOCODING', cast=str)
