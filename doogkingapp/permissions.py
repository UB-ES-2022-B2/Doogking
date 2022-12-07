from rest_framework import permissions


"""
Class to check if the user that makes the request
 is the same as the one passed as the obj parameter.
 This is used to let a user modify itself but not the others
"""


class IsOwnerOfProfile(permissions.BasePermission):
    def has_object_permission(self, request: object,
            view: object, obj: object) -> object:
        return obj == request.user
