from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    pass
    # def get_paginated_response(self, data):
    #     return Response(data)