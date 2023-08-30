from rest_framework import serializers

from ads.models import Ad, User, Category


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'


class AdsCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.CharField()
    author_id = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    category_id = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._category = self.initial_data.pop('category_id')
        self._author = self.initial_data.pop('author_id')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)

        author_obj = User.objects.get(username=self._author)
        category_obj = Category.objects.get(name=self._category)
        ad.author_id = author_obj
        ad.category_id = category_obj

        ad.save()
        return ad


class AdsUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False, max_length=150)
    price = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    is_published = serializers.BooleanField(required=False)
    image = serializers.CharField(required=False)
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    def is_valid(self, *, raise_exception=False):
        self._category = self.initial_data.pop('category_id') if 'category_id' in self.initial_data else None
        self._author = self.initial_data.pop('author_id') if 'author_id' in self.initial_data else None
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        try:
            author_obj = User.objects.get(username=self._author)
            ad.author_id = author_obj

            category_obj = Category.objects.get(name=self._category)
            ad.category_id = category_obj
        finally:
            ad.save()
            return ad

    class Meta:
        model = Ad
        fields = '__all__'

