from rest_framework import serializers

from ads.models import Ad, User, Category


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'


class AdsCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._author_id = self.initial_data('author_id')
        self._category_id = self.initial_data('category_id')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)

        author_obj, _ = User.objects.get_or_create(name=self._author_id)
        category_obj, _ = Category.objects.get_or_create(name=self._category_id)

        ad.author_id.add(author_obj)
        ad.category_id.add(category_obj)

        ad.save()
        return ad


