from rest_framework.routers import DefaultRouter
from .viewsets import AnimeViewSet, SeasonViewSet, EpisodeViewSet, TagViewSet, YearViewSet


router = DefaultRouter()
router.register(r'animes', AnimeViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'episodes', EpisodeViewSet)
router.register(r'tags', TagViewSet)
router.register(r'years', YearViewSet)

urlpatterns = router.urls