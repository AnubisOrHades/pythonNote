from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from .serializers import *


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 20


class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
    pagination_class = Pagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
