import uuid

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import UUIDField


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

    def __str__(self):
        return f"Face of {self.account.username}"
