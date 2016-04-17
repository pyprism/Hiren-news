from django.db import models


class Bunny(models.Model):
    comment_url = models.URLField(unique=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment={0}, Date={1}'.format(self.comment_url, self.time)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

