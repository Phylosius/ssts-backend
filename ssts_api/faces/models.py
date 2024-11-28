from django.contrib.postgres.fields import ArrayField
from django.db import models


class Face(models.Model):

    account = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    # field for store face encoding given by face_recognition
    encoding = ArrayField(  # only supported by a Postgresql database
        models.FloatField(),
        size=128,
    )
    recording_date = models.DateTimeField(auto_now_add=True)
