import json

from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from ads.models import User, Location
from ads.serializers.users import UserSerializer


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):  # does not work
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location_id']

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            username=user_data.get('username'),
            password=user_data.get('password'),
            role=user_data.get('role'),
            age=user_data.get('age'),
            location_id=Location(user_data.get('location_id')),
        )

        return JsonResponse({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': user.password,
            'role': user.role,
            'age': user.age,
            'location_id': user.location_id.id,
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserAdsDetailView(View):
    def get(self, request):
        user_data = User.objects.annotate(ads=Count('ad'), filter=Q(ad__is_published=True))
        users_data = [user for user in user_data]

        return JsonResponse([{'username': user.username, 'ads': user.ads} for user in users_data], safe=False)
