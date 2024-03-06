from rest_framework import viewsets
from persons.models import Person
from .serializers import PersonSerializer, PersonDetailSerializer
from rest_framework.response import Response
from mixins.viewsets import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class PersonViewSet(CustomModelViewSet):
    queryset = Person.objects.prefetch_related('anime__genres', 'anime__topics', 'anime__years').select_related('anime').all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('anime', 'gender', 'height', 'weight', 'dead', 'old')
    search_fields = ('title', 'slug')


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PersonDetailSerializer
        return PersonSerializer
