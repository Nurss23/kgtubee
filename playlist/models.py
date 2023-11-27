from django.db import models
from django.contrib.auth.models import User
from core.models import Profile


class UserPlayList(models.Model):
    # file_path = models.FileField(upload_to="playlist/")
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)
    videos_qty = models.IntegerField(default=0)
    views_qty = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )

    def __str__(self):
        return self.name