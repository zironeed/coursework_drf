from rest_framework import serializers

from spa_app.models import Habit
from spa_app.spa_validators import habit_validator


class HabitSerializer(serializers.BaseSerializer):
    nice_habit = serializers.BooleanField(validators=[habit_validator])
    linked_habit = serializers.CharField(validators=[habit_validator])
    reward = serializers.CharField(validators=[habit_validator])
    duration = serializers.IntegerField(validators=[habit_validator])

    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'nice_habit', 'linked_habit',
                  'frequency', 'reward', 'duration', 'published',)
