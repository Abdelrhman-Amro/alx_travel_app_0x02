from rest_framework.routers import DefaultRouter

from .views import BookingsViewSet, ListingsViewSet, ReviewsViewSet

router = DefaultRouter()
router.register(r"listings", ListingsViewSet, basename="listing")
router.register(r"bookings", BookingsViewSet, basename="bookings")
router.register(r"reviews", ReviewsViewSet, basename="reviews")
urlpatterns = router.urls
