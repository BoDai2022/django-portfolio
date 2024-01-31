from rest_framework import permissions

class IsManagerPlayerEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    # def has_permission(self, request, view):
    #     print(request.user.get_all_permissions())
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         if user.has_perm("players.view_player") & :
    #             return True
    #     return False
    #     # return super().has_permission(request, view)
    # # def has_object_permission(self, request, view, obj):
    # #     return super().has_object_permission(request, view, obj)