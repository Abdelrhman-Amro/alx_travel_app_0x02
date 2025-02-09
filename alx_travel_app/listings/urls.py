from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookingsViewSet, ListingsViewSet, PaymentView, ReviewsViewSet

router = DefaultRouter()
router.register(r"listings", ListingsViewSet, basename="listing")
router.register(r"bookings", BookingsViewSet, basename="bookings")
router.register(r"reviews", ReviewsViewSet, basename="reviews")
urlpatterns = [
    router.urls,
    path("initiate-payment/", PaymentView.as_view(), name="initiate-payment"),
    path("verify-payment/", PaymentView.as_view(), name="verify-payment"),
]
