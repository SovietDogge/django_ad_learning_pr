from rest_framework import serializers

from ads.models import Category


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id']

