from django.db import models

# Create your models here.
class Announcements(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    name = models.CharField(max_length=200)
    # image = models.ImageField()
    #Note : Add upload option and a choice menu for specifying if item should be added to home screen rotation or not

    def __str__(self):
        return self.title
