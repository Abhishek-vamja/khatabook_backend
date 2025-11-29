from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from apps.user.views import UserProfileViewSet, UserSingUpViewset

router = DefaultRouter()
router.register(
    r'profile', UserProfileViewSet, basename='user-profile'
)

urlpatterns = [
    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', UserSingUpViewset.as_view({'post': 'create'}), name='user-sign-up'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]