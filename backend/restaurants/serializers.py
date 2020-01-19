from rest_framework.serializers import Serializer, CharField, IntegerField


class RestaurantsSerializer(Serializer):
    id = CharField()
    name = CharField()
    cuisines = CharField()
    address = CharField()
    city_district = CharField()
    featured_image = CharField()
    rating = CharField()
    average_cost_for_two = CharField()
