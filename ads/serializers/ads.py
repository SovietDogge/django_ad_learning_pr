from rest_framework import serializers

from ads.models import Ad


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'
