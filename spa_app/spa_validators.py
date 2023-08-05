from rest_framework import validators


def habit_validator(new_habit):
    if new_habit.duration > 120:
        raise validators.ValidationError("Duration cannot be more than 120 sec")

    if new_habit.nice_habit:
        if new_habit.linked_habit or new_habit.reward:
            raise validators.ValidationError("Nice habit cannot have linked habit or reward")

    else:
        if new_habit.linked_habit and new_habit.reward:
            raise validators.ValidationError("Common habit cannot have linked habit and reward simultaneously")

    if new_habit.linked_habit and not new_habit.nice_habit:
        raise validators.ValidationError("Linked habit must be nice")


