from django.db import models


class Bunny(models.Model):
    comment_url = models.URLField(unique=True)
    time = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

