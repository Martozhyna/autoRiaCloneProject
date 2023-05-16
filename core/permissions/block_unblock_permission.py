from rest_framework.permissions import IsAdminUser


class BlockUnblockUserPermission(IsAdminUser):

    def has_object_permission(self, request, view, obj):
        return not obj.is_staff or request.user.is_superuser
