from django.contrib import admin

# Register your models here.
from apps.transacction.models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Admin interface for Transaction model."""
    list_display = ('id', 'user', 'entry_name', 'amount', 'type', 'created_at')
    list_filter = ('type', 'user')
    search_fields = ('entry_name', 'user__username', 'user__email')
    ordering = ('-created_at',)
