import uuid
from django.db import models
from django.contrib.auth.models import User

class Gallery(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="galleries")
    folder = models.CharField(default="", max_length=33)
    data = models.JSONField(default=dict)