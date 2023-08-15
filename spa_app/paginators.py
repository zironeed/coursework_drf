from rest_framework import pagination


class HabitPagination(pagination.PageNumberPagination):
    """Paginator for Habit objects"""
    page_size = 5
