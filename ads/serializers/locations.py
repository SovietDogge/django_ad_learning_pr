from rest_framework import serializers

from ads.models import Location


class LocationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
