from rest_framework import serializers

from ads.models import Selection, Ad


class SelectionViewSerializer(serializers.ModelSerializer):
    ad = serializers.SlugRelatedField(
        queryset=Ad.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ['id']


class SelectionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'
