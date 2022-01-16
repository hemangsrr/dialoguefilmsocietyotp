from django.conf import settings
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posterurl = models.URLField(blank=True)
    registerurl = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def admin_image(self):
        return self.posterurl
    admin_image.allow_tags = True
