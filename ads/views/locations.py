from rest_framework.viewsets import ModelViewSet

from ads.models import Location
from ads.serializers.locations import LocationViewSerializer


class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationViewSerializer
