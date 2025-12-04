from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'link', 'image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la noticia'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Contenido de la noticia...'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ejemplo.com (opcional)'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'link': 'Enlace (opcional)',
            'image': 'Imagen (opcional)',
        }
        help_texts = {
            'link': 'URL relacionada con la noticia (opcional)',
            'image': 'Imagen que acompañará la noticia (opcional)',
        }
