from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class EventAPIView(APIView):

    # Get only auth user events
    def get(self, request):
        queryset = Event.objects.filter(creator=request.user)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    # Create user event and become participant
    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


