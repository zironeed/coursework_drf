from django.db import models
from config.settings import AUTH_USER_MODEL
from datetime import datetime

NULLABLE = {'null': True, 'blank': True}


class FrequencyChoices(models.TextChoices):
    """Choices for Habit -> frequency field"""
    Daily = 'DAILY'
    Mo = 'MONDAY'
    Tu = 'TUESDAY'
    We = 'WEDNESDAY'
    Th = 'THURSDAY'
    Fr = 'FRIDAY'
    Sa = 'SATURDAY'
    Su = 'SUNDAY'


class Habit(models.Model):
    """Model for default and nice habits"""
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='user', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='place')
    time = models.TimeField(default=datetime.now().time(), verbose_name='habit starts')
    action = models.TextField(verbose_name='action')
    nice_habit = models.BooleanField(default=False, verbose_name='is nice habit')
    linked_habit = models.ForeignKey('self', on_delete=models.CASCADE,
                                     verbose_name='linked habit (only for nice habit)', **NULLABLE)
    frequency = models.CharField(choices=FrequencyChoices.choices, default=FrequencyChoices.Daily,
                                 verbose_name='frequency')
    reward = models.CharField(max_length=100, verbose_name='reward (only for default habit)', **NULLABLE)
    duration = models.IntegerField(**NULLABLE, verbose_name='duration')
    published = models.BooleanField(default=False, verbose_name='is published')

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'

    def __str__(self):
        return f"""Action: {self.action}
        Place: {self.place}
        Time: {self.time}"""

