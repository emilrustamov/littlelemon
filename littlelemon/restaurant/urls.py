from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import booking_view, bookings_api, BookingViewSet, MenuItemViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'menu', MenuItemViewSet)

urlpatterns = [
    path('booking/', booking_view, name='booking'),
    path('bookings/', bookings_api, name='bookings_api'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
