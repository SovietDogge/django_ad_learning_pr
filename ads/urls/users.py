from django.urls import path

import ads.views.users as users_view

urlpatterns = [
    path('users', users_view.UserView.as_view()),
    path('users/<int:pk>', users_view.UserDetailView.as_view()),
    path('users/<int:pk>/delete', users_view.UserDeleteView.as_view()),
    path('users/<int:pk>/update', users_view.UserUpdateView.as_view()),
    path('users/create', users_view.UserCreateView.as_view()),
    path('users/ads', users_view.UserAdsDetailView.as_view())
]
