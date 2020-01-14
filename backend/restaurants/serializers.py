from rest_framework import serializers


class RestaurantsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    featured_image = serializers.CharField()
