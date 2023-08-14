from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APITestCase, APIClient

from spa_app.models import Habit, FrequencyChoices
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User(
            email='test@mail.ru',
            tg_name='test',
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
        self.user.set_password('12345')
        self.user.save()

        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        self.public_habit = Habit.objects.create(
            place="TestPublic",
            time="14:00:00",
            action="TestPublic",
            nice_habit=False,
            frequency=FrequencyChoices.Fr,
            reward="The bag of chips",
            duration=10,
            published=True,
            user=self.user
        )

        self.private_habit = Habit.objects.create(
            place="TestDefault",
            time="14:00:00",
            action="TestDefault",
            nice_habit=False,
            frequency=FrequencyChoices.Fr,
            reward="The bag of chips",
            duration=10,
            published=False,
            user=self.user
        )

        self.public_id = self.public_habit.id
        self.private_id = self.private_habit.id

    def test_create_habit(self):
        """Test for HabitCreateView"""
        data = {
            "id": 5,
            "place": "TestCreate",
            "time": "14:00:00",
            "action": "TestCreate",
            "nice_habit": "False",
            "frequency": "SUNDAY",
            "reward": "The bag of chips",
            "duration": 10,
            "published": "True",
            "user": self.user
            }

        url = reverse('spa_app:habit_create')
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Habit.objects.filter(place='TestCreate').exists()
        )

    def test_public_list_habit(self):
        """Test for HabitPublishListView"""
        url = reverse('spa_app:habit_publish')

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['count'],
            1
        )

    def test_private_list_habit(self):
        """Test for HabitPrivateListView"""
        url = reverse('spa_app:habit_private')

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_detail_habit(self):
        """Test for HabitRetrieveView"""
        url = reverse('spa_app:habit_retrieve', kwargs={'pk': self.private_habit.pk})

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        """Test for HabitUpdateView"""
        update_data = {
            "place": "TestUpdate",
            "action": "TestUpdate",
            }

        response = self.client.put(reverse('spa_app:habit_update', kwargs={'pk': self.private_habit.pk},
                                           ), data=update_data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertTrue(
            Habit.objects.filter(place='TestUpdate').exists()
        )

    def test_destroy_habit(self):
        """Test for HabitDestroyView"""
        habit = Habit.objects.create(
            id=2,
            place='TestCreate',
            action='TestCreate',
            frequency='MONDAY',
            reward='The bag of chips',
            duration=20,
            published=False,
            user=self.user,
        )

        url = reverse('spa_app:habit_destroy', kwargs={'pk': habit.id})

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_validate_duration(self):
        """Test for duration validating"""
        data = {
            'place': 'TestCreate',
            'action': 'TestCreate',
            'frequency': FrequencyChoices.Mo,
            'reward': 'The bag of chips',
            'duration': 121,
            'published': False,
            'user': self.user
        }

        url = reverse('spa_app:habit_create')
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_validate_nice_habit(self):
        """Test for nice_habit validating"""
        data = {
            'place': 'TestCreate',
            'action': 'TestCreate',
            'nice_habit': True,
            'frequency': FrequencyChoices.Mo,
            'reward': 'The bag of chips',
            'duration': 121,
            'published': False,
            'user': self.user
        }

        url = reverse('spa_app:habit_create')
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_validate_default_habit(self):
        """
        Test for default habit validating
        (checking for reward and linked_habit)
        """
        default_data = {
            'place': 'TestCreate',
            'action': 'TestCreate',
            'linked_habit': self.private_habit,
            'frequency': FrequencyChoices.Mo,
            'reward': 'The bag of chips',
            'duration': 121,
            'published': False,
            'user': self.user
        }

        url = reverse('spa_app:habit_create')
        response = self.client.post(url, default_data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
