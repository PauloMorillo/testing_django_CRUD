from django.shortcuts import render
from rest_framework import viewsets
from .models import Passenger
from .serializers import PassengerSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bot_id', 'session_id']


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
