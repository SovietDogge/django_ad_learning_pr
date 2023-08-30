from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Category
from ads.serializers.categories import CategoriesSerializer, CategoryDeleteSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class DetailCategoryView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
