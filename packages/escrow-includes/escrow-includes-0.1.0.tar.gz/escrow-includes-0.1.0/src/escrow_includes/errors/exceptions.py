from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class NotFoundException(APIException):
    """
    Exception for when a resource is not found
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("Resource Not Found.")
    default_code = "not_found"


class DatabaseException(APIException):
    """
    Exception for when a database error occurs
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _("Internal Server Error. Contact Administrator")
    default_code = "database_error"


class ExistingDataException(APIException):
    """
    Exception for when a data already exists
    """

    status_code = status.HTTP_409_CONFLICT
    default_detail = _("Resource Already Exists.")
    default_code = "already_exists"


class BadRequest(APIException):
    """
    Exception for when a request is bad
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Validation Error.")
    default_code = "validation_error"


class PermissionDenied(APIException):
    """
    Exception for when a user does not have permission to perform an action
    """

    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _("Inadequate Permission To Perform Action.")
    default_code = "permission_denied"


class UnAuthorizedError(APIException):
    """
    Exception for when a user is unauthorized to perform an action
    """

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _("User is not authorized to perform this action.")
    default_code = "unauthorized"


class ServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _("Internal Server Error. Contact Administrator")
    default_code = "server_error"
