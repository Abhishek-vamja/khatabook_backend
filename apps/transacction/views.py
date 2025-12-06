from django.db.models import Sum

from rest_framework.decorators import action

from apps.transacction.models import Transaction
from apps.transacction.serializers import TransactionSerializer
from apps.core.viewsets import BaseModelViewSet


class TransactionViewSet(BaseModelViewSet):
    """ViewSet for managing financial transactions."""
    http_method_names = ["get", "post", "delete"]
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        """Retrieve authenticated user transactions."""
        transaction_type = self.request.query_params.get("type", None)
        
        qs =Transaction.objects.filter(user=self.request.user)

        if transaction_type:
            qs = qs.filter(type=transaction_type)

        return qs.order_by("-created_at")

    def perform_create(self, serializer):
        """Associate the transaction with the authenticated user."""
        serializer.save(user=self.request.user)

    @action(methods=["get"], detail=False, url_path='kpi')
    def kpi(self, request, *args, **kwargs):
        """Calculate and return transaction KPIs for the authenticated user."""
        transactions = self.get_queryset()
        
        total_credit_amount = transactions.filter(
            type=Transaction.CREDIT
        ).aggregate(total=Sum('amount'))['total'] or 0
        total_debit_amount = transactions.filter(
            type=Transaction.DEBIT
        ).aggregate(total=Sum('amount'))['total'] or 0

        kpi_data = {
            "total_credit_amount": total_credit_amount,
            "total_debit_amount": total_debit_amount,
        }

        self._status_code = 200
        self._data = kpi_data

        return self.get_response()