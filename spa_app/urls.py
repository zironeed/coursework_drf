from django.urls import path

from spa_app.views import HabitUpdateView, HabitRetrieveView, HabitDestroyView, HabitCreateView, \
    HabitPublishListView, HabitPrivateListView

from spa_app.apps import SpaAppConfig

app_name = SpaAppConfig.name


urlpatterns = [
    path('habits/publish/', HabitPublishListView.as_view(), name='habit_publish'),
    path('habits/my/', HabitPrivateListView.as_view(), name='habit_private'),
    path('habits/update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('habits/retrieve/<int:pk>/', HabitRetrieveView.as_view(), name='habit_retrieve'),
    path('habits/destroy/<int:pk>/', HabitDestroyView.as_view(), name='habit_destroy'),
    path('habits/create/', HabitCreateView.as_view(), name='habit_create'),
]
