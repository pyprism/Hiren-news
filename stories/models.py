from django.db import models
from django.contrib.auth.models import User
from urlparse import urlparse

class Stroy(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField()
	points = models.IntegerField()
	moderator = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	@property
	def domain(self):
		return urlparse(self.url).netloc
