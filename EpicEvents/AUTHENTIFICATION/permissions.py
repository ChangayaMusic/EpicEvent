from rest_framework.permissions import BasePermission


class SalesPermissions(BasePermission):
    """
    Sales permissions
    A sales user can:
        - Add new clients
        - Add an event for a contract
        - Display and update only clients assigned to them
        - Display and update only the client's contract assigned to them
    """

    def has_permission(self, request, view):
        user = request.user
        role = user.role
        if view.action in ["list", "retrieve"]:
            return True
        elif view.action in ["create", "destroy"]:
            if not role == 3:
                return False
            return True

        elif view.action in ["update", "partial_update"]:
            if role == 1 or role == 3:
                return True
            return False


class SupportPermissions(BasePermission):
    """
    Support permissions
    A support user can:
        - Display and update events assigned to them
        - Display clients (for the client's events assigned to them)
    """

    def has_permission(self, request, view):
        user = request.user
        role = user.role

        if view.action in ["list", "retrieve"]:
            return True

        if view.action in ["update", "partial_update"]:
            if role == 2:
                return True

        elif view.action in ["create", "destroy"]:
            if not role == 3:
                return False
            return True


class ManagerPermissions(BasePermission):
    """
    Manager permissions:
    Only a manager can create accounts.
    """

    message = "Acces reserved for managers."

    def has_permission(self, request, view):

        user = request.user
        role = user.role

        if not role == 1:
            return False
        return True
