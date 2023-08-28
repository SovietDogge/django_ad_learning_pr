import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

import lesson27.settings
from ads.models import Ad, Category, User


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        all_ads = self.object_list.order_by('-price')

        paginator = Paginator(all_ads, lesson27.settings.TOTAL_PAGE_ON)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({'id': ad.id,
                        'name': ad.name,
                        'price': ad.price,
                        'description': ad.description,
                        'image': ad.image.url,
                        'is_published': ad.is_published,
                        'category_id': ad.category_id.id,
                        'author_id': ad.author_id.id}
                       )

        response = {'items': ads, 'total': all_ads.count(), 'num_pages': paginator.num_pages}
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CreateAdView(CreateView):
    model = Ad
    fields = ['name', 'price', 'description', 'image', 'is_published', 'category_id', 'author_id']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(
            name=data.get('name'),
            price=data.get('price'),
            description=data.get('description'),
            image=data.get('image'),
            is_published=data.get('is_published'),
            category_id=get_object_or_404(Category, pk=data.get('category_id')),
            author_id=get_object_or_404(User, pk=data.get('author_id')),
        )
        return JsonResponse({
            'name': new_ad.name,
            'author': new_ad.author_id.id,
            'price': new_ad.price,
            'description': new_ad.description,
            'is_published': new_ad.is_published})


@method_decorator(csrf_exempt, name='dispatch')
class AdsDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        add = self.get_object()
        return JsonResponse({'id': add.id,
                             'name': add.name,
                             'author': add.author,
                             'price': add.price,
                             'description': add.description,
                             'address': add.address,
                             'is_published': add.is_published}
                            )


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
