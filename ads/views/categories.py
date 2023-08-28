import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, CreateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ads.models import Category
from ads.serializers.categories import CategoriesSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class DetailCategoryView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


@method_decorator(csrf_exempt, name='dispatch')
class CreateCategoryView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data.get('name')
        )

        return JsonResponse({
            'id': category.id,
            'name': category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)

        self.object.name = category_data.get('name') or self.object.name
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name
        })
