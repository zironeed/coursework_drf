from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import datetime, timedelta
import json
import requests
from datetime import datetime

from config.settings import TG_TOKEN
from spa_app.models import Habit
from users.models import User


def tg_update():
    url = f"https://api.telegram.org/bot{TG_TOKEN}/getUpdates"
    response = requests.get(url)

    if response.status_code == 200:
        for users in response.json()['result']:
            chat_id = users['message']['from']['id']
            tg_name = users['message']['from']['username']

            user = User.objects.get(tg_name=tg_name)

            if user.chat_id is None:
                user.chat_id = chat_id
                user.save()


def habit_schedule():
    now = datetime.now()

    for habit in Habit.objects.filter(nice_habit=False):
        if habit.frequency == 'DAILY':
            if habit.time.strftime('%H:%M') == now.strftime('%H:%M'):
                chat_id = habit.user.chat_id

                if habit.reward:
                    message = f'I will {habit.action} at {habit.time} in {habit.place}. My reward is {habit.reward}'
                else:
                    message = f'I will {habit.action} at {habit.time} in {habit.place}.'

                url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url)
