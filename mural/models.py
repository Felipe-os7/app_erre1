from django.db import models


class Mural(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='murals/', blank=True, null=True)
	location = models.CharField(max_length=200, blank=True)
	technique = models.CharField(max_length=200, blank=True)
	dimensions = models.CharField(max_length=200, blank=True)
	year = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Mural'
		verbose_name_plural = 'Murales'

	def __str__(self):
		return self.title
