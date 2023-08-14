from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spa_app.models import Habit
from spa_app.serializers import HabitSerializer
from spa_app.paginators import HabitPagination
from permissions import IsOwner, CanDelete


class HabitPublishListView(ListAPIView):
    """Контроллер для списка публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(published=True)
    pagination_class = HabitPagination
    ordering_fields = ['pk']

    def get_queryset(self):
        habit_list = Habit.objects.all()
        habit_list_filtered = []

        for habit in habit_list:
            if habit.published:
                habit_list_filtered.append(habit)

        return habit_list_filtered


class HabitPrivateListView(ListAPIView):
    """Контроллер для списка непубличных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]
    ordering_fields = ['pk']

    def get_queryset(self):
        user = self.request.user
        habit_list = Habit.objects.all()
        habit_list_filtered = []

        for habit in habit_list:
            if habit.user == user:
                habit_list_filtered.append(habit)

        return habit_list_filtered


class HabitCreateView(CreateAPIView):
    """Контроллер для создания привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveView(RetrieveAPIView):
    """Контроллер для просмотра отдельных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateView(UpdateAPIView):
    """Контроллер для обновления привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyView(DestroyAPIView):
    """Контроллер для удаления привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner, CanDelete]
