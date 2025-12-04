from django.db import models
from galeria.models import Painting


class SiteSetting(models.Model):
	artist_bio = models.TextField(blank=True)
	featured_painting = models.ForeignKey(Painting, null=True, blank=True, on_delete=models.SET_NULL)
	featured_video_url = models.URLField(blank=True)
	instagram_url = models.URLField(blank=True, verbose_name='URL de Instagram')
	youtube_url = models.URLField(blank=True, verbose_name='URL de YouTube')

	def __str__(self):
		return "Site Settings"


class News(models.Model):
	title = models.CharField(max_length=200, verbose_name='Título')
	content = models.TextField(blank=True, verbose_name='Contenido')
	# Optional image for the news item. Uploaded files go to MEDIA_ROOT/news_images/
	image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name='Imagen')
	link = models.URLField(blank=True, verbose_name='Enlace')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

	def __str__(self):
		return self.title
