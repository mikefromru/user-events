from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Event
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token

import logging

logger = logging.getLogger(__name__)
User = get_user_model()

class TestAppView(APITestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user(username='user_1', password='qwerty')
        self.token = Token.objects.get_or_create(user=self.user_1)
        self.user_2 = User.objects.create_user(username='user_2', password='qwerty')
        self.token = Token.objects.get_or_create(user=self.user_2)

        Event.objects.create(
            id=1,
            title='First',
            body='Hello world',
            creator=self.user_1,
        ).participants.add(self.user_1)

        Event.objects.create(
            id=2,
            title='Second',
            body='Hello world',
            creator=self.user_2,
        ).participants.add(self.user_2)

    def test_url(self):
        logger.debug('Starting test url access')
        self.client.credentials(HTTP_AUTHORIZATION='TOKEN ' + str(self.token[0]))
        response = self.client.get(reverse('event-user-list'))
        self.assertEquals(response.status_code, 200)

    def test_check_all_events(self):
        self.client.credentials(HTTP_AUTHORIZATION='TOKEN ' + str(self.token[0]))
        response = self.client.get(reverse('event-list'))
        self.assertEquals(response.status_code, 200)

    def test_create_event(self):
        self.client.credentials(HTTP_AUTHORIZATION='TOKEN ' + str(self.token[0]))
        payload = {
            'title': 'Title_1',
            'body': 'Hellow World',
            'creator': 1,
            'participants': 1,
        }
        response = self.client.post(reverse('event-user-list'), data=payload)
        self.assertEquals(response.status_code, 201)

    def test_create_event_another_one(self):
        self.client.credentials(HTTP_AUTHORIZATION='TOKEN ' + str(self.token[0]))
        payload = {
            'title': 'Title_2',
            'body': 'Hellow World',
            'creator': 1,
            'participants': 1,
        }
        response = self.client.post(reverse('event-user-list'), data=payload)
        self.assertEquals(response.status_code, 201)

    def test_count_events(self):
        events = Event.objects.all()
        self.assertEquals(events.count(), 2)

    def test_remove_event(self):
        self.client.credentials(HTTP_AUTHORIZATION='TOKEN ' + str(self.token[0]))
        response = self.client.delete(reverse('event', args=[2]))
        self.assertEquals(response.status_code, 204)

    def test_stop_being_participate(self):
        self.client.credentials(HTTP_AUTHORIZATION='TOKEN ' + str(self.token[0]))
        event = Event.objects.get(id=1)
        response = self.client.patch(reverse('event', args=[2]))
        if event.participants.filter(id=2).exists():
            event.participants.remove(2)
            self.assertEquals(response.status_code, 204)
        else:
            event.participants.add(2)
            self.assertEquals(response.status_code, 200)


    
       
       