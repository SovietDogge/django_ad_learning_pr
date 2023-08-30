import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ads.models import Ad
from ads.serializers.ads import AdsSerializer, AdsCreateSerializer


class AdsView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer


class CreateAdView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsCreateSerializer


class AdsDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdsUpdateView(UpdateView):
    model = Ad
    fields = ['price', 'name', 'description', 'is_published']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad = self.get_object()
        new_ad: dict = json.loads(request.body)

        ad.name = new_ad.get('name') or ad.name
        ad.price = new_ad.get('price') or ad.price
        ad.description = new_ad.get('description') or ad.description
        ad.is_published = new_ad.get('is_published') or ad.is_published

        ad.save()

        return JsonResponse({'id': ad.id,
                             'name': ad.name,
                             'price': ad.price,
                             'description': ad.description,
                             'image': ad.image.url,
                             'is_published': ad.is_published,
                             'category_id': ad.category_id.id,
                             'author_id': ad.author_id.id}
                            )


@method_decorator(csrf_exempt, name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


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
