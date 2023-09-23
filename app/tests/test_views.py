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


    def test_url(self):
        logger.debug('Starting test url access')
        self.client.credentials(HTTP_AUTHORIZATION='TOKEN ' + str(self.token[0]))
        response = self.client.get(reverse('event-list'))
        self.assertEquals(response.status_code, 200)

