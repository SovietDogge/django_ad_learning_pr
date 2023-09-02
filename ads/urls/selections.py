from django.urls import path

import ads.views.selections as selection_view

urlpatterns = [
    path('selections/', selection_view.SelectionView.as_view()),
    path('selections/<int:pk>/', selection_view.SelectionDetailView.as_view()),
    path('selections/create/', selection_view.SelectionCreateView.as_view()),
    path('selections/<int:pk>/delete/', selection_view.SelectionDeleteView.as_view()),
    path('selections/<int:pk>/update/', selection_view.SelectionUpdateView.as_view())
]
