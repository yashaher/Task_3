from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50