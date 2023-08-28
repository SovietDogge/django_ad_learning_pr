from rest_framework import serializers

from ads.models import User


class UserSerializer(serializers.ModelSerializer):
    # location_id = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location_id']
