from rest_framework.permissions import BasePermission


# Можно добавить и владельцев
# class IsOwner(BasePermission):
#     """Владельцы."""
#     def has_object_permission(self, request, view, obj):
#         if obj.owner == request.user or request.user.is_superuser:
#             return True
#
#         return False


class IsActiveStaff(BasePermission):
    """Активные сотрудники."""
    def has_permission(self, request, view):
        if request.user.is_active and request.user.is_staff or request.user.is_superuser:
            return True

        return False
