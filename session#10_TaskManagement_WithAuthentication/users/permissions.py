from rest_framework.permissions import BasePermission
from users.models import Role

class IsTaskOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN