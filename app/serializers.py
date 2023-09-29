from rest_framework import serializers
from .models import Event

from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = ('id', 'first_name', 'last_name')


class EventSerializer(serializers.ModelSerializer):

    participants = UserSerializer(many=True, read_only=False)

    class Meta:
        model = Event
        fields = ('id', 'title', 'body', 'created_at', 'creator', 'participants')