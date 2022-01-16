from django.conf import settings
from django.db import models


class Screening(models.Model):
    place = models.CharField(max_length=200)
    screeningDateTime = models.DateTimeField()

    def __str__(self):
        return self.place
