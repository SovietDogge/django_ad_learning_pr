import json

from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from ads.models import User, Location
from ads.serializers.users import UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return JsonResponse([{'username': user.username, 'role': user.role}
                             for user in self.object_list], safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse(UserSerializer(user).data)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location_id']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        updated_data = json.loads(request.body)

        self.object.first_name = updated_data.get('first_name') or self.object.first_name
        self.object.last_name = updated_data.get('last_name') or self.object.last_name
        self.object.username = updated_data.get('username') or self.object.username
        self.object.password = updated_data.get('password') or self.object.password
        self.object.role = updated_data.get('role') or self.object.role
        self.object.age = updated_data.get('age') or self.object.age
        self.object.location_id = Location(updated_data.get('location_id')) or self.object.location_id
        self.object.save()

        return JsonResponse({'first_name': self.object.first_name,
                             'last_name': self.object.last_name,
                             'username': self.object.username,
                             'password': self.object.password,
                             'role': self.object.role,
                             'age': self.object.age,
                             'location_id': self.object.location_id.id})


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
