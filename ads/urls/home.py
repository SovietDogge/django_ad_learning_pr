from django.urls import path

import ads.views.home as home_view

urlpatterns = [
    path('', home_view.HomePage.as_view())
]
