from django.db import models
from config.settings import AUTH_USER_MODEL
from django.utils.timezone import now

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey('AUTH_USER_MODEL', on_delete=models.CASCADE, verbose_name='user', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='place')
    time = models.TimeField(default=now, verbose_name='habit starts')
    action = models.TextField(verbose_name='action')
    nice_habit = models.BooleanField(default=False, verbose_name='is nice habit')
    linked_habit = models.ForeignKey('self', on_delete=models.CASCADE,
                                     verbose_name='linked habit (only for nice habit)', **NULLABLE)
    frequency = models.TextChoices() #ZAPOLNI
    reward = models.CharField(max_length=100, verbose_name='reward (only for default habit)', **NULLABLE)
    duration = models.IntegerField(**NULLABLE, verbose_name='duration')
    published = models.BooleanField(default=False, verbose_name='is published')

