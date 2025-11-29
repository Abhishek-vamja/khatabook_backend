from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.transacction.views import TransactionViewSet

router = DefaultRouter()
router.register(
    r"", TransactionViewSet, basename="transaction"
)

urlpatterns = [
    path("", include(router.urls)),
]
