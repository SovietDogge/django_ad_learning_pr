from rest_framework import serializers

from ads.models import User, Location


class UserSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location_id']


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location_id = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location_id', 'id']

    def is_valid(self, *, raise_exception=False):
        self._location_id = self.initial_data.pop('location_id')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        location_obj, _ = Location.objects.get_or_create(name=self._location_id)
        user.location = location_obj

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20, required=False)
    username = serializers.CharField(max_length=20, required=False)
    password = serializers.CharField(max_length=100, required=False)
    role = serializers.CharField(max_length=100, required=False)
    age = serializers.IntegerField(required=False)
    location_id = serializers.SlugRelatedField(required=False,
                                               queryset=Location.objects.all(),
                                               slug_field='name')

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location_id')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        location_obj, _ = Location.objects.get_or_create(name=self._location)
        user.location = location_obj

        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
