from rest_framework import serializers

from apps.transacction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for the Transaction model."""

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at", "user")
