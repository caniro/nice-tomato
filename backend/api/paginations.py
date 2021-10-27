from rest_framework.pagination import PageNumberPagination

class SensorPageNumberPagination(PageNumberPagination):
    page_size = 100
