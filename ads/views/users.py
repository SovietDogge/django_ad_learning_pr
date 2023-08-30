from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView

from ads.models import User
from ads.serializers.users import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserDestroySerializer


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):  # does not work
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserAdsDetailView(View):
    def get(self, request):
        user_data = User.objects.annotate(ads=Count('ad'), filter=Q(ad__is_published=True))
        users_data = [user for user in user_data]

        return JsonResponse([{'username': user.username, 'ads': user.ads} for user in users_data], safe=False)
