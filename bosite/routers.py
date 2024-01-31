from rest_framework.routers import DefaultRouter
from players.viewsets import PlayerViewSet,PlayerGernericViewSet

router = DefaultRouter()
# router.register('players-abc', PlayerViewSet, basename='players')
router.register('players-abc', PlayerGernericViewSet, basename='players')
# print(router.urls)
urlpatterns = router.urls