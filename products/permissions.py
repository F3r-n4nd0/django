from rest_framework.permissions import BasePermission

class ProductPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['list', 'metadata']:
            return True
        elif view.action in ['create']:
            return request.user.is_authenticated()
        else:
            return request.user.is_authenticated() and request.user.is_staff()
