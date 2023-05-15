from rest_framework.permissions import IsAdminUser


class IsPremium(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_premium or request.user.is_superuser)
