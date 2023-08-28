from django.urls import path

import ads.views.categories as category_view

urlpatterns = [
    path('categories', category_view.CategoryView.as_view()),
    path('categories/<int:pk>', category_view.DetailCategoryView.as_view()),
    path('categories/create/', category_view.CreateCategoryView.as_view()),
    path('categories/<int:pk>/update', category_view.CategoryUpdateView.as_view()),
]
