from django import forms
from .models import Painting


class SubmissionForm(forms.ModelForm):
    """Form para envío de obras: en lugar de crear un objeto Submission,
    creará una instancia de `Painting` al guardarse (publicada inmediatamente).
    """
    class Meta:
        model = Painting
        fields = ('title', 'description', 'image', 'technique', 'dimensions', 'year', 'price')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la obra'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Descripción de la obra'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'technique': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Técnica utilizada'
            }),
            'dimensions': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dimensiones (ej: 50cm x 70cm)'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Año'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio (opcional)'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'image': 'Imagen',
            'technique': 'Técnica',
            'dimensions': 'Dimensiones',
            'year': 'Año',
            'price': 'Precio',
        }
        help_texts = {
            'price': 'Deja en blanco si no está en venta',
        }

    def save(self, commit=True):
        # Guardar directamente como Painting (publicado)
        painting = super().save(commit=False)
        if commit:
            painting.save()
        return painting
