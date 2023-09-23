from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Event

User = get_user_model()

class TestUser(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user(username='user_1', password='qwerty')

    def test_create_user(self):
        user = User.objects.create_user(username='user_2', password='qwerty')
        self.assertFalse(user.is_superuser)
        count_users = User.objects.all().count()
        self.assertEqual(count_users, 2)
    


class TestEvent(TestCase):
    pass

