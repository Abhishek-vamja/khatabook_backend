from rest_framework import serializers

from apps.user.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for User Profile"""
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number', 'imges', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']


class UserSignUpSerializer(serializers.Serializer):
    """Serializer for User Sign-Up"""
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_confirm_password(self, value):
        """Ensure the password and confirm_password match."""
        if 'password' in self.initial_data and value != self.initial_data['password']:
            raise serializers.ValidationError("Passwords do not match.")
        return value

    def create(self, validated_data):
        """Create a new user with the provided data."""
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
