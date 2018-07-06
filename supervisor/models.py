import uuid

from django.contrib.postgres.fields import HStoreField
from django.db import models


class Quest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=24)
    rejections = HStoreField()
