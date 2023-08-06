from django.urls import path

from spa_app.views import HabitUpdateView, HabitRetrieveView, HabitDestroyView, HabitCreateView, \
    HabitPublishListView, HabitPrivateListView

from spa_app.apps import SpaAppConfig

app_name = SpaAppConfig.name


urlpatterns = [
    path('spa/habits/publish/', HabitPublishListView.as_view(), name='habit_publish'),
    path('spa/habits/my/', HabitPrivateListView.as_view(), name='habit_private'),
    path('spa/habits/update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('spa/habits/retrieve/<int:pk>/', HabitRetrieveView.as_view(), name='habit_retrieve'),
    path('spa/habits/destroy/<int:pk>/', HabitDestroyView.as_view(), name='habit_destroy'),
    path('spa/habits/create/', HabitUpdateView.as_view(), name='habit_create'),
]
