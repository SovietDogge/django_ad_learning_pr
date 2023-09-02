from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Selection
from ads.permissions import SelectionDetailViewPermission
from ads.serializers.selections import SelectionViewSerializer, SelectionDeleteSerializer, SelectionCreateSerializer


class SelectionView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionViewSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionViewSerializer
    permission_classes = [IsAuthenticated, SelectionDetailViewPermission]


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated, SelectionDetailViewPermission]


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDeleteSerializer
    permission_classes = [IsAuthenticated, SelectionDetailViewPermission]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionViewSerializer
    permission_classes = [IsAuthenticated, SelectionDetailViewPermission]

