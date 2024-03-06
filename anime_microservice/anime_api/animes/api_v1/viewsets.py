from animes.models import Anime, Season, Episode, Tag, Year
from .serializers import AnimeDetailSerializer, AnimeSerializer, SeasonSerializer, TagSerializer, EpisodeSerializer, YearSerializer
from mixins.viewsets import CustomModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class AnimeViewSet(CustomModelViewSet):
    queryset = Anime.objects.prefetch_related('genres', 'topics', 'years',).all()
    # permission_classes = (DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('genres', 'topics', 'years')
    search_fields = ['title', 'slug']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AnimeDetailSerializer
        return AnimeSerializer


class SeasonViewSet(CustomModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    # permission_classes = (DjangoModelPermissions, )


class EpisodeViewSet(CustomModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    # permission_classes = (DjangoModelPermissions,)
    
    def list(self, request, *args, **kwargs):
        return Response({"list": "Method \"GET\" not allowed."})



class TagViewSet(CustomModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (DjangoModelPermissions,)



class YearViewSet(CustomModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer