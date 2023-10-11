from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Event
from ..serializers import EventSerializer, EventPostSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from rest_framework.generics import ListAPIView

User = get_user_model()


class EventAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class EventListAPIView(ListAPIView):

    pagination_class = EventAPIListPagination
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventAPIView(APIView):

    # Get only auth user events
    def get(self, request):
        queryset = Event.objects.filter(creator=request.user)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create user event and become participant
    def post(self, request, *args, **kwargs):
        serializer = EventPostSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            # serializer.save()
            serializer.save(participants=[self.request.user])
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetailAPIView(APIView):

    # Stop or take part as a participant in event
    def patch(self, request, pk, format=None):
        event = get_object_or_404(Event.objects.all(), pk=pk)
        if event.participants.filter(id=request.user.id).exists():
            # Leave participant event
            event.participants.remove(request.user.id)
        else:
            # Become participat of event
            event.participants.add(request.user.id)
            # event.participants.add(request.user.username)
            # event.participants.add(request.user.username)
        event.save()
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete user event
    def delete(self, request, pk, format=None):
        event = get_object_or_404(Event.objects.all(), pk=pk, creator=request.user)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


