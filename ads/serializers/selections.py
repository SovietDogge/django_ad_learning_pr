from rest_framework import serializers

from ads.models import Selection, Ad, User


class SelectionViewSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
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
