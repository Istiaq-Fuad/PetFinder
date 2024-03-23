from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
    IsAuthenticated,
    IsAdminUser,
)


class PetsWritePermission(BasePermission):
    message = "Editing pets is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # if not request.user.is_shelter:
        #     return False

        return request.user.is_staff
