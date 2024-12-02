from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from faces.models import Face
from faces.serializers import FaceSerializer

User = get_user_model()

class FacesViewSet(viewsets.ModelViewSet):

    queryset = Face.objects.all()
    serializer_class = FaceSerializer

class FacesView(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):

        user_id = request.get('user_id')
        reference_image = request.FILES.get("reference_image")

        # verifying data
        if not user_id or not reference_image:
            return Response(
                {"error": "Both 'user_id' and 'reference_image' are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # verifying if the user exist
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": f"No user found with id {user_id}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # creating face object
        Face.create_face(user=user, reference_image=reference_image)

        return Response(
            {"message": "Face object created successfully", "face_id": face.id},
            status=status.HTTP_201_CREATED,
        )

