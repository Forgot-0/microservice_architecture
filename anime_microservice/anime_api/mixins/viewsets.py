from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.core.cache import cache
from .cache import cache_method

class RetrieveModelMixin:
    # @cache_method(10)
    def retrieve(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset()).filter(pk=kwargs['pk'])
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data[0])


class CustomModelViewSet(RetrieveModelMixin, ModelViewSet):
    
    # @cache_method(100)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        cache.delete(f'{self.basename}_list_')
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        cache.delete(f'{self.basename}_retrieve_{self.kwargs["pk"]}')
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        cache.delete(f'{self.basename}_retrieve_{self.kwargs["pk"]}')
        return super().partial_update(request, *args, **kwargs)