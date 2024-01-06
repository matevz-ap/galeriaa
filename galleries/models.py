import uuid

from django.contrib.auth.models import User
from django.db import models


class Gallery(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="galleries")
    folder = models.CharField(default="", max_length=33)
    data = models.JSONField(default=dict)
    name = models.CharField(default="", max_length=33)

    @property
    def spaced(self, cols=3) -> list[list[str]]:
        s: list[list[str]] = [[], [], []]
        for i, photo in enumerate(self.data):
            s[i % cols].append(photo)
        return s
