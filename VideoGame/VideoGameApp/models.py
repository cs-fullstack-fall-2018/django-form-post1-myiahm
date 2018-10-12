from django.db import models

class VideoGame(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)


