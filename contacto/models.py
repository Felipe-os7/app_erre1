from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'

    def __str__(self):
        return f"{self.name} <{self.email}> - {self.created_at:%Y-%m-%d}"


class MuralQuote(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Correo electrónico')
    technique = models.CharField(max_length=200, verbose_name='Técnica', help_text='Ej: Pintura acrílica, aerosol, etc.')
    dimensions = models.CharField(max_length=200, verbose_name='Dimensiones', help_text='Ej: 3m x 2m, 5m x 4m, etc.')
    message = models.TextField(verbose_name='Mensaje', help_text='Describe tu proyecto o cualquier detalle adicional')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Cotización de Mural'
        verbose_name_plural = 'Cotizaciones de Murales'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} <{self.email}> - {self.created_at:%Y-%m-%d}"


