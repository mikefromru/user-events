from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Event

User = get_user_model()

class TestAppModel(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user(username='user_1', password='qwerty')
        self.user_2 = User.objects.create_user(username='user_2', password='qwerty')

    def test_create_user(self):
        self.user_3 = User.objects.create_user(username='user_3', password='qwerty')
        self.assertFalse(self.user_2.is_superuser)
        count_users = User.objects.all().count()
        self.assertEqual(count_users, 3)
    
    def test_create_even(self):
        self.event = Event.objects.create(title='My Event', body='Some text', creator=self.user_1)
        self.event.participants.add(self.user_2)
        self.assertEqual(self.event.creator, self.user_1)
        self.assertEqual(self.event.participants.count(), 1)
