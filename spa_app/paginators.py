from rest_framework import pagination


class HabitPagination(pagination.PageNumberPagination):
    page_size = 5
