from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from spa_app.models import Habit
from spa_app.serializers import HabitSerializer
from spa_app.paginators import HabitPagination
from permissions import IsOwner


class HabitPublishListView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination

    def get_queryset(self):
        habit_list = Habit.objects.all()
        habit_list_filtered = []

        for habit in habit_list:
            if habit.published:
                habit_list_filtered.append(habit)

        return habit_list_filtered


class HabitPrivateListView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        habit_list = Habit.objects.all()
        habit_list_filtered = []

        for habit in habit_list:
            if habit.user == user:
                habit_list_filtered.append(habit)

        return habit_list_filtered


class HabitCreateView(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]
