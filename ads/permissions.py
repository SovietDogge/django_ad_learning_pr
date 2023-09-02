from rest_framework import permissions

from ads.models import Selection, ADMIN, MODERATOR


class SelectionDetailViewPermission(permissions.BasePermission):
    message = 'You can\'t see that selection because you are not an owner'

    def has_permission(self, request, view):
        selection = Selection.objects.get(pk=view.kwargs['pk'])
        user_id = request.user.id
        return selection.id == user_id or request.user.role in (ADMIN, MODERATOR)
