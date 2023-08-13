from rest_framework import serializers

from spa_app.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        new_habit = Habit.objects.create(**validated_data)

        if new_habit.duration > 120:
            raise serializers.ValidationError("Duration cannot be more than 120 sec")

        if new_habit.nice_habit is False:
            if not new_habit.reward:
                if not new_habit.linked_habit:
                    raise serializers.ValidationError("Default habit must has reward or nice habit")

            else:
                if new_habit.linked_habit:
                    raise serializers.ValidationError("Common habit cannot have linked habit and reward simultaneously")

            return new_habit

        else:
            if new_habit.reward:
                raise serializers.ValidationError("Nice habit cannot have linked habit or reward")
            return new_habit

    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'nice_habit', 'linked_habit',
                  'frequency', 'reward', 'duration', 'published',)
