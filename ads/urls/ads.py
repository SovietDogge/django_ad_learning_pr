from django.urls import path

import ads.views.ads as ads_views

urlpatterns = [
    path('ad', ads_views.AdsView.as_view()),
    path('ad/<int:pk>', ads_views.AdsDetailView.as_view()),
    path('ad/<int:pk>/update', ads_views.AdsUpdateView.as_view()),
    path('ad/create/', ads_views.CreateAdView.as_view()),
    path('ad/<int:pk>/delete', ads_views.AdsDeleteView.as_view()),
    path('ad/<int:pk>/upload_img', ads_views.AdsUploadImage.as_view()),
]
