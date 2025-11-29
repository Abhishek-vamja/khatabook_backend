from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class BaseResponseMixin:
    """A base response mixin to standardize API responses."""

    def initialize_response_vars(self):
        """Initialize default internal response variables."""
        self._status_code = status.HTTP_200_OK
        self._message = ""
        self._data = None
        self._errors = None

    def get_response(self):
        """
        Build response using the internal variables:
        self._status_code, self._message, self._data, self._errors.
        """
        if self._errors is not None:
            if self._status_code == status.HTTP_200_OK:
                self._status_code = status.HTTP_400_BAD_REQUEST

        payload = {
            "data": self._data,
        }
        # include errors only when present (optional)
        if self._errors is not None:
            payload["errors"] = self._errors
            return Response(payload, status=self._status_code)
        else:
            return Response(payload["data"], status=self._status_code)


class BaseModelViewSet(BaseResponseMixin, ModelViewSet):
    """
    Base viewset: mixin first in MRO so its helpers are available.
    """

    permission_classes = [IsAuthenticated]

    def initial(self, request, *args, **kwargs):
        """
        Called before any action handler — initialize response vars automatically.
        """
        # call mixin initializer first
        self.initialize_response_vars()
        # then run DRF's initial processing (auth, throttle, etc.)
        return super().initial(request, *args, **kwargs)
