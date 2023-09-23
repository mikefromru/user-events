from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status

User = get_user_model()

class EventAPIView(APIView):

    # Get only auth user events
    def get(self, request):
        # queryset = Event.objects.all()
        queryset = Event.objects.filter(creator=request.user)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create user event and become participant
    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetailAPIView(APIView):

    def delete(self, request, pk, format=None):
        event = get_object_or_404(Event.objects.all(), pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


