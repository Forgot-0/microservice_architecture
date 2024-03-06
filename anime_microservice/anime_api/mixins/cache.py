from django.core.cache import cache
from functools import wraps
from rest_framework.response import Response


def key_method_builder(self, request, *args, **kwargs):
    return f'{self.basename}_{self.action}_{kwargs.get("pk", "")}'



def cache_method(expire):

    def wrapper(func):

        @wraps(func)
        def inner(self, request,  *args, **kwargs): 
            if request.GET:
                return func(self, request, *args, **kwargs)

            cache_key = key_method_builder(self, request,  *args, **kwargs)
            data = cache.get(cache_key)
            
            if data:
                return Response(data)

            response = func(self, request, *args, **kwargs)


            cache.set(cache_key, response.data, timeout=expire) 
            return response
        
        return inner
    
    return wrapper