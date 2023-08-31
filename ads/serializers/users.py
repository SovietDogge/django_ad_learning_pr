from rest_framework import serializers

from ads.models import User, Location


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        try:
            self._location_id = self.initial_data.pop('location_id')
        except KeyError:
            pass
        finally:
            return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        location_obj, _ = Location.objects.get_or_create(name=self._location_id)
        user.location = location_obj

        user.set_password(validated_data.get('password'))

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20, required=False)
    username = serializers.CharField(max_length=20, required=False)
    password = serializers.CharField(max_length=100, required=False)
    age = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(required=False,
                                            queryset=Location.objects.all(),
                                            slug_field='name')

    def is_valid(self, *, raise_exception=False):
        self._location = None
        if 'location_id' in self.initial_data.keys():
            self._location = self.initial_data.pop('location_id')

        self._password = None
        if 'password' in self.initial_data.keys():
            self._password = self.initial_data.pop('password')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        if self._location:
            location_obj, _ = Location.objects.get_or_create(name=self._location)
            user.location = location_obj

        if self._password:
            user.set_password(self._password)

        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
