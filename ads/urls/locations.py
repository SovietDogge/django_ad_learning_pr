from rest_framework import routers

from ads.views.locations import LocationsViewSet

location_router = routers.SimpleRouter()
location_router.register('locations', LocationsViewSet)
