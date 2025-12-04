from django.db import models


class Collection(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Colección'
		verbose_name_plural = 'Colecciones'

	def __str__(self):
		return self.title


class Painting(models.Model):
	CATEGORY_CHOICES = [
		('pintura', 'Pintura'),
		('ilustracion', 'Ilustración'),
	]
	
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='paintings/', blank=True, null=True)
	collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True, related_name='paintings')
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='pintura', verbose_name='Categoría')
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	technique = models.CharField(max_length=200, blank=True)
	dimensions = models.CharField(max_length=200, blank=True)
	year = models.IntegerField(null=True, blank=True)
	is_for_sale = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Pintura'
		verbose_name_plural = 'Pinturas'

	def __str__(self):
		return self.title


def submission_image_upload_to(instance, filename):
	# store submissions in uploads/paintings or uploads/murals
	category = instance.category if hasattr(instance, 'category') else 'painting'
	if category == 'mural':
		return f'uploads/murals/{filename}'
	return f'uploads/paintings/{filename}'


class Submission(models.Model):
	CATEGORY_CHOICES = (('painting','Pintura'),('mural','Mural'))
	title = models.CharField(max_length=200, verbose_name='Título')
	description = models.TextField(blank=True, verbose_name='Descripción')
	image = models.ImageField(upload_to=submission_image_upload_to, blank=True, null=True, verbose_name='Imagen')
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='painting', verbose_name='Categoría')
	technique = models.CharField(max_length=200, blank=True, verbose_name='Técnica')
	dimensions = models.CharField(max_length=200, blank=True, verbose_name='Dimensiones')
	year = models.IntegerField(null=True, blank=True, verbose_name='Año')
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Precio')
	is_for_sale = models.BooleanField(default=True, verbose_name='En venta')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	approved = models.BooleanField(default=False, verbose_name='Aprobado')

	class Meta:
		verbose_name = 'Envío público'
		verbose_name_plural = 'Envíos públicos'

	def __str__(self):
		return f"{self.title} ({self.category})"
