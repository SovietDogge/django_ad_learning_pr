from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.serializers.ads import AdsSerializer, AdsCreateSerializer, AdsUpdateSerializer, AdsDestroySerializer


class AdsView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer

    def get(self, request, *args, **kwargs):
        ad_category = request.GET.getlist('category', None)
        ad_q = None
        for category in ad_category:
            if not ad_q:
                ad_q = Q(category__id__contains=category)
            else:
                ad_q |= Q(category__id__contains=category)

        text = request.GET.get('text', None)
        if text:
            if not ad_q:
                ad_q = Q(name__icontains=text)
            else:
                ad_q |= Q(name__icontains=text)

        location = request.GET.get('location', None)
        if location:
            if not ad_q:
                ad_q = Q(author__location__name__icontains=location)
            else:
                ad_q |= Q(author__location__name__icontains=location)

        price_from, price_to = request.GET.get('price_from'), request.GET.get('price_to')
        if price_to and price_from:
            if not ad_q:
                ad_q = Q(price__gte=price_from)
                ad_q &= Q(price__lte=price_to)
            else:
                ad_q |= Q(price__gte=price_from)
                ad_q &= Q(price__lte=price_to)

        if ad_q:
            self.queryset = self.queryset.filter(ad_q)

        return super().get(request, *args, **kwargs)


class CreateAdView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsCreateSerializer


class AdsDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]


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


