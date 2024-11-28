import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import UUIDField


class Face(models.Model):

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    account = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    # field for store face encoding given by face_recognition
    encoding = ArrayField(  # only supported by a Postgresql database
        models.FloatField(),
        size=128,
    )
    recording_date = models.DateTimeField(auto_now_add=True)
