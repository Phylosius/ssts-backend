from django.shortcuts import render

from rest_framework import viewsets

from accounts.models import User
from accounts.serializers import UserSerializer


class AccountViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
