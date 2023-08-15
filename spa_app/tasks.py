from celery import shared_task
from spa_app.services import tg_update, habit_schedule


@shared_task(name='habit_checker')
def habit_checker():
    """Sending notifications to users"""
    tg_update()
    habit_schedule()
