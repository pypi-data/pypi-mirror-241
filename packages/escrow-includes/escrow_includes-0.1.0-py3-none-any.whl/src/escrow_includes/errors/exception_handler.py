from datetime import datetime
from typing import Any, Dict, TypedDict

from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework.response import Response

from . import exceptions


class ErrorResponseDict(TypedDict):
    error_code: str
    message: str
    details: list[dict]
    timestamp: datetime


def api_exception_handler(exc, context: Dict[str, Any]):
    """Custom API exception handler."""

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if auth_header := getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = auth_header
        if wait := getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % wait

        message = exc.default_detail
        if exc.detail and isinstance(exc.detail, str):
            message = exc.detail

        error_response = ErrorResponseDict(
            error_code=exc.code or exc.default_code,
            message=message,
            details=exc.get_full_details(),
            timestamp=timezone.now().timestamp(),
        )
        return Response(error_response, status=exc.status_code, headers=headers)
    raise exceptions.APIException("Error occurred during error handling")
