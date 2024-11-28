from django.shortcuts import render

from rest_framework import viewsets

from faces.models import Face
from faces.serializers import FaceSerializer


class FacesViewSet(viewsets.ModelViewSet):

    queryset = Face.objects.all()
    serializer_class = FaceSerializer
