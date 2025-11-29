from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from apps.core import viewsets
from apps.user.models import User
from apps.user.serializers import UserProfileSerializer, UserSignUpSerializer


class UserProfileViewSet(viewsets.BaseModelViewSet):
    """
    A viewset for viewing and editing user profile instances.
    """
    http_method_names = ["get", "patch"]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        """Retrieve the user profile for the authenticated user."""
        return User.objects.filter(id=self.request.user.id)
    
    @action(methods=['get'], detail=False, url_path='me')
    def me(self, request, *args, **kwargs):
        """Retrieve the authenticated user's profile."""
        instance = self.get_queryset().first()
        serializer = self.get_serializer(instance)
        
        self._status_code = 200
        self._data = serializer.data

        return self.get_response()


class UserSingUpViewset(viewsets.BaseModelViewSet):
    """
    A viewset for user sign-up.
    """
    http_method_names = ["post"]
    serializer_class = UserSignUpSerializer  # Assuming a different serializer for sign-up
    permission_classes = [AllowAny]  # Allow any user to sign up

    def create(self, request, *args, **kwargs):
        """Handle user sign-up."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        self._status_code = status.HTTP_201_CREATED
        self._data = serializer.data

        return self.get_response()
