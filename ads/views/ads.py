from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ad
from ads.serializers.ads import AdsSerializer, AdsCreateSerializer, AdsUpdateSerializer, AdsDestroySerializer


class AdsView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer


class CreateAdView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsCreateSerializer


class AdsDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer


class AdsUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsUpdateSerializer


class AdsDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsDestroySerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdsUploadImage(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'image': self.object.image.url
        })
