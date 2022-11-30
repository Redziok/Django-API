from rest_framework import permissions
from rest_framework.response import Response


class view_person(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user in permissions.SAFE_METHODS:
            return True
class can_view_other_persons(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Lads_and_blokes'):
            return Response('true')
        return Response('no permission')
