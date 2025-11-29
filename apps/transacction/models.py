from django.db import models

from apps.user.models import User
from apps.core.models import BaseModel


class Transaction(BaseModel):
    """Model representing a financial transaction."""
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    TRANSACTION_TYPE = (
        (CREDIT, "Credit"),
        (DEBIT, "Debit"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    entry_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=255, choices=TRANSACTION_TYPE)

    def __str__(self):
        return f"Transaction {self.id}: {self.amount}"
