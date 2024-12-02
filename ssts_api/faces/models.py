import uuid

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import UUIDField

from faces.services import get_encodings_from_uploaded_file


class Face(models.Model):

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # field for store face encoding given by face_recognition
    encoding = ArrayField(  # only supported by a Postgresql database
        models.FloatField(),
        size=128,
    )
    recording_date = models.DateTimeField(auto_now_add=True)
    reference_image = models.ImageField(upload_to='faces/reference_images/', null=True, blank=True)

    @classmethod
    def create_face(cls, user, reference_image):
        face_encodings = get_encodings_from_uploaded_file(reference_image)

        face = cls(user=user, reference_image=reference_image, encoding=face_encodings)
        face.save()

        return face

    def __str__(self):
        return f"Face of {self.user.username}"
